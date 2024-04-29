from flask import Blueprint, jsonify, request
from entidades.Usuario import Usuario, validar_data, validar_dado_entrada
from pony.orm import select
from servicos.ServicoConsulta import ConsultaService

bp = Blueprint('main', __name__)

@bp.route('/usuarios', methods=['GET'])
def get_usuarios():
    
    usuarios = ConsultaService.get_usuarios()
    return jsonify(usuarios)

@bp.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario_id(id):
    return jsonify(ConsultaService.get_usuario_id(id))


@bp.route('/atendimentos', methods=['GET'])
def get_atendimentos():
    data_atendimento = request.args.get('data_atendimento')
    condicao_saude = request.args.get('condicao_saude')
    
    if data_atendimento and validar_data(data_atendimento):
        return jsonify({"Erro" : "Formato de data_atendimento é inválido. Use o Formato 'YYYY-mm-dd'"}), 400
    
    if condicao_saude and validar_dado_entrada(condicao_saude):
        return jsonify({"Erro" : "Condição de saúde inválida. Use uma das seguintes opções: hipertensao, diabetes, ferida vascular, dengue, tuberculose."}), 400
    
    atendimentos = ConsultaService.get_atendimentos_and_condicao_saude(data_atendimento, condicao_saude)
    return jsonify(atendimentos)

@bp.route('/usuarios', methods=['POST'])
def adicionar_usuario():
    novo_usuario_post = request.json
    
    data_atendimento = novo_usuario_post['data_atendimento']
    condicao_saude = novo_usuario_post['condicao_saude']
    
    if data_atendimento and validar_data(data_atendimento):
        return jsonify({"Erro" : "Formato de data_atendimento é inválido. Use o Formato 'YYYY-mm-dd'"}), 400
    
    if condicao_saude and validar_dado_entrada(condicao_saude):
        return jsonify({"Erro" : "Condição de saúde inválida. Use uma das seguintes opções: hipertensao, diabetes, ferida vascular, dengue, tuberculose."}), 400
    
    usuarios = ConsultaService.adicionarUsuarios(novo_usuario_post)
    return jsonify({"mensagem" : "Usuário adicionado com sucesso"}), 201


@bp.route('/usuarios', methods=['PUT'])    
def atualizar_usuario():
    usuario_atualizado = request.json
    
    data_atendimento = usuario_atualizado['data_atendimento']
    condicao_saude = usuario_atualizado['condicao_saude']
    
    if data_atendimento and validar_data(data_atendimento):
        return jsonify({"Erro" : "Formato de data_atendimento é inválido. Use o Formato 'YYYY-mm-dd'"}), 400
    
    if condicao_saude and validar_dado_entrada(condicao_saude):
        return jsonify({"Erro" : "Condição de saúde inválida. Use uma das seguintes opções: hipertensao, diabetes, ferida vascular, dengue, tuberculose."}), 400
    
    usuarios = ConsultaService.atualizarUsuarios(usuario_atualizado)
    return jsonify(usuarios)

@bp.route('/usuarios/<int:id>', methods=['DELETE'])
def excluir_usuario(id):
    return ConsultaService.excluirUsuario(id)







