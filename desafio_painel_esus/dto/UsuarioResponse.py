from entidades.Usuario import Usuario

class UsuarioResponseDTO:
    def __init__(self, id, nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude):
        self.id = id
        self.nome = nome
        self.nascimento = nascimento
        self.cns = cns
        self.cpf = cpf
        self.unidade = unidade
        self.data_atendimento = data_atendimento
        self.condicao_saude = condicao_saude
        
    def mapping_usuario(usuario_obj):
        if isinstance(usuario_obj, dict):
            return UsuarioResponseDTO(
                id=usuario_obj.get('id'), 
                nome=usuario_obj.get('nome'), 
                nascimento=usuario_obj.get('nascimento'),
                cns=usuario_obj.get('cns'),
                cpf=usuario_obj.get('cpf'),
                unidade=usuario_obj.get('unidade'),
                data_atendimento=usuario_obj.get('data_atendimento'),
                condicao_saude=usuario_obj.get('condicao_saude')
            )
        elif isinstance(usuario_obj, Usuario):
            return UsuarioResponseDTO(
                id=usuario_obj.id, 
                nome=usuario_obj.nome, 
                nascimento=usuario_obj.nascimento,
                cns=usuario_obj.cns,
                cpf=usuario_obj.cpf,
                unidade=usuario_obj.unidade,
                data_atendimento=usuario_obj.data_atendimento,
                condicao_saude=usuario_obj.condicao_saude
            )
        else:
            raise ValueError("O argumento usuario_obj deve ser um dicionário ou um objeto Usuario.")

        
    #def lista_usuarios(usuarios):
    #        return [UsuarioResponseDTO.from_usuario(usuario) for usuario in usuarios]    

    