
import mysql.connector
import pandas as pd
import datetime
import csv

# Conectar ao banco de dados
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='*****',
    database='covid'
)

df = pd.read_csv(r"C:\Users\Lucas Cruz\Downloads\MICRODADOS.csv",sep=';',encoding='latin-1',low_memory=False)

cursor = db.cursor()

# Criação da tabela de dimensão Localização
create_dim_query = '''CREATE TABLE dim_municipio (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        municipio VARCHAR(255) NOT NULL
                        );'''
cursor.execute(create_dim_query)

# Criação da tabela de dimensão datas
create_dim_query = '''CREATE TABLE dim_data_diagnostico (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        data_diagnostico DATE NOT NULL
                        );'''
cursor.execute(create_dim_query)

# Criação da tabela de dimensão Sexo
create_dim_query = '''CREATE TABLE dim_sexo (
                          id INT AUTO_INCREMENT PRIMARY KEY,
                          sexo VARCHAR(50) NOT NULL
                          );'''
cursor.execute(create_dim_query)

# Criação da tabela de dimensão Comorbidade
create_dim_query = '''CREATE TABLE dim_comorbidade (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        comorbidadePulmao VARCHAR(50) NOT NULL
                        );'''
cursor.execute(create_dim_query)

# Criação da tabela fato 
create_fact_query = '''CREATE TABLE tabela_fato (
                           id INT AUTO_INCREMENT PRIMARY KEY,
                           id_municipio INT NOT NULL,
                           id_data_diagnostico INT NOT NULL,
                           id_sexo INT NOT NULL,
                           id_comorbidadePulmao INT NOT NULL,
                           Casos_confirmados INT NOT NULL,
                           Obitos INT NOT NULL,
                           Valor INT NOT NULL,
                           FOREIGN KEY (id_municipio) REFERENCES dim_municipio (id),
                           FOREIGN KEY (id_data_diagnostico) REFERENCES dim_data_diagnostico (id),
                           FOREIGN KEY (id_sexo) REFERENCES dim_sexo (id),
                           FOREIGN KEY (id_comorbidadePulmao) REFERENCES dim_comorbidade (id)
                           
                           );'''
cursor.execute(create_fact_query)


print("Executado com sucesso!")


with open(r'C:\Users\Lucas Cruz\Downloads\MICRODADOS.csv', newline="", encoding="ISO-8859-1") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";")
        for i, row in df.iterrows():
            insert_query = f"INSERT INTO dim_municipio (municipio) VALUES (%s)"
            cursor.execute(insert_query, (row["Municipio"],))
        print("MUNICIPIOS INSERIDOS COM SUCESSO!")


with open(r'C:\Users\Lucas Cruz\Downloads\MICRODADOS.csv', newline="", encoding="ISO-8859-1") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";")
        for i, row in df.iterrows():
            insert_query = f"INSERT INTO dim_data_diagnostico (data_diagnostico) VALUES (%s)"
            cursor.execute(insert_query, (row["DataDiagnostico"],))
        print("DATAS INSERIDAS COM SUCESSO!")

with open(r'C:\Users\Lucas Cruz\Downloads\MICRODADOS.csv', newline="", encoding="ISO-8859-1") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";")
        for i, row in df.iterrows():
            insert_query = f"INSERT INTO dim_sexo (sexo) VALUES (%s)"
            cursor.execute(insert_query, (row["Sexo"],))
        print("SEXOS INSERIDOS COM SUCESSO!")

with open(r'C:\Users\Lucas Cruz\Downloads\MICRODADOS.csv', newline="", encoding="ISO-8859-1") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";")
        for i, row in df.iterrows():
            insert_query = f"INSERT INTO dim_comorbidade (comorbidadePulmao) VALUES (%s)"
            cursor.execute(insert_query, (row["ComorbidadePulmao"],))
        print("COMORBIDADES INSERIDAS COM SUCESSO!")



print("FINALIZADO")


#Salva mudanças
db.commit()

# Fechar a conexão com o banco de dados
db.close()