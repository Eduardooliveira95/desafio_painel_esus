from entidades.Usuario import Usuario, db, validar_dado_entrada, validar_data
from pony.orm import select, db_session
from collections.abc import Mapping
from flask import request
from dto.UsuarioResponse import UsuarioResponseDTO


class ConsultaService:
    def get_usuarios():
        usuarios = select(u for u in Usuario)
        lista_usuarios = [{'id': user.id, 'nome': user.nome, 'nascimento': user.nascimento,
                  'cns': user.cns, 'cpf': user.cpf, 'unidade': user.unidade,
                  'data_atendimento': user.data_atendimento, 'condicao_saude': user.condicao_saude} 
                  for user in usuarios]
        return lista_usuarios
    
    @classmethod
    def get_usuario_id(cls, id):
        usuario = Usuario.get(id=id)
        
        if usuario: 
            usuario_obj = {
                'id': usuario.id,
                'nome': usuario.nome,
                'nascimento': usuario.nascimento,
                'cns': usuario.cns,
                'cpf': usuario.cpf,
                'unidade': usuario.unidade,
                'data_atendimento': usuario.data_atendimento,
                'condicao_saude': usuario.condicao_saude
            } 
            return ({'mensagem': 'Usuário encontrado com sucesso'}, usuario_obj), 200
        return ({'mensagem': 'Usuário não encontrado, por favor verificar se o ID está correto'}), 404
    
    @classmethod
    def get_atendimentos_and_condicao_saude(cls, data_atendimento = None, condicao_saude= None):
        
        if data_atendimento and condicao_saude:
            usuarios_com_atendimento = select(u for u in Usuario if (u.data_atendimento == data_atendimento) and (u.condicao_saude == condicao_saude))
        elif data_atendimento:
            usuarios_com_atendimento = select(u for u in Usuario if u.data_atendimento == data_atendimento)
        elif condicao_saude:
            usuarios_com_atendimento = select(u for u in Usuario if u.condicao_saude == condicao_saude)
        
        lista_atendimentos = [{'id': user.id, 'nome': user.nome, 'nascimento': user.nascimento,
                  'cns': user.cns, 'cpf': user.cpf, 'unidade': user.unidade,
                  'data_atendimento': user.data_atendimento, 'condicao_saude': user.condicao_saude} 
                  for user in usuarios_com_atendimento]
        return lista_atendimentos

    @classmethod
    def adicionarUsuarios(cls, novo_usuario_post):
        
        if isinstance(novo_usuario_post, Mapping):
            nome = novo_usuario_post.get('nome')
            nascimento = novo_usuario_post.get('nascimento')
            cns = novo_usuario_post.get('cns')
            cpf = novo_usuario_post.get('cpf')
            unidade = novo_usuario_post.get('unidade')
            data_atendimento = novo_usuario_post.get('data_atendimento')
            condicao_saude = novo_usuario_post.get('condicao_saude')

        if data_atendimento and validar_data(data_atendimento):
            return ({"Erro": "Formato de data_atendimento é inválido. Use o Formato 'YYYY-mm-dd'"}), 400
    
        if condicao_saude and validar_dado_entrada(condicao_saude):
            return ({"Erro": "Condição de saúde inválida. Use uma das seguintes opções: hipertensao, diabetes, ferida vascular, dengue, tuberculose."}), 400
        
        novo_usuario = Usuario(nome=nome, nascimento=nascimento, cns=cns, cpf=cpf, unidade=unidade, data_atendimento=data_atendimento, condicao_saude=condicao_saude)
        with db_session:
            db.commit()
        return novo_usuario
    
    @classmethod
    def atualizarUsuarios(cls, usuario_atualizado):
        if isinstance(usuario_atualizado, Mapping):
            id = usuario_atualizado.get('id')
        usuario = Usuario.get(id=id)
        
        if usuario:
            usuario.set(**request.json)
            with db_session:
                db.commit()
                
            usuario_obj = {
                'id': usuario.id,
                'nome': usuario.nome,
                'nascimento': usuario.nascimento,
                'cns': usuario.cns,
                'cpf': usuario.cpf,
                'unidade': usuario.unidade,
                'data_atendimento': usuario.data_atendimento,
                'condicao_saude': usuario.condicao_saude
            } 
            return ({'mensagem': 'Usuário atualizado com sucesso'}, usuario_obj), 200
        return ({'mensagem': 'Usuário não encontrado, por favor verificar se o ID está correto'}), 404
    
    @classmethod
    def excluirUsuario(cls, id):
        usuario = Usuario.get(id=id)
        
        if usuario:
            usuario.delete()
            with db_session:
                db.commit()
            return ({'mensagem': 'Usuário excluído com sucesso'})
        return ({'mensagem': 'Usuário não encontrado'}), 404 
                
                
            
            
