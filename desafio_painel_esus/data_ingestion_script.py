import csv
import mysql.connector


def conectar_ao_banco():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="urubu100",
        database="desafios_esus"
    )
    
    
def inserir_no_banco(arquivo_csv):
    connection = conectar_ao_banco()
    cursor = connection.cursor()
    
    insert = "INSERT INTO users (NOME, NASCIMENTO, CNS, CPF, UNIDADE, DATA_NASCIMENTO, CONDICAO_SAUDE) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    
    for linha in arquivo_csv:
        cursor.execute(insert, linha)
        
    connection.commit()
    connection.close()
    
    
def main():
    with open('./sql/atendimentos.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Pula o cabeçalho
        data = [row[1:] for row in reader]
        
    inserir_no_banco(data)

if __name__ == "__main__":
    main()