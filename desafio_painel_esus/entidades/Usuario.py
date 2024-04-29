from pony.orm import Required, PrimaryKey, Optional, Database, Set
from config import Config
import re

db = Database()

db.bind(provider='mysql', host=Config.DB_HOST, user=Config.DB_USER, 
        password=Config.DB_PASSWORD, database=Config.DB_NAME)


def validar_data(data):
    if not re.match(r'\d{4}-\d{2}-\d{2}', data):
        raise ValueError('Formato de data inválido, Use YYYY-mm-dd.')
    
def validar_dado_entrada(str):
    dados_permitidos = ['hipertensao', 'diabetes', 'ferida vascular', 'dengue', 'tuberculose']
    if str not in dados_permitidos:
        raise ValueError(f'Condição de saúde inválida. As opções permitidas são: {", ".join(dados_permitidos)}')

class Usuario(db.Entity):
    _table_ = "Usuario"
    id = PrimaryKey(int, auto=True)
    nome = Required(str)
    nascimento = Required(str)
    cns = Optional(int, size=64)
    cpf = Optional(str)
    unidade = Optional(str)
    data_atendimento = Optional(str)
    condicao_saude = Optional(str)

db.generate_mapping(create_tables=True)
