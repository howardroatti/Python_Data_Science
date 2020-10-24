#!/usr/bin/env python
#Conector para o MySQL
import mysql.connector
#Conector para o Postgres
import psycopg2

#Cria conexao com o MySQL
mysqldb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="h0w4rd",
  database="alfa"
)

#Cria conexao com o Postgres
postgresdb = psycopg2.connect(
    host="localhost",
    port="5432",
    database="sigma",
    user="postgres",
    password="1234"
)

#Cria o cursor com a conexao MySQL
mysqlcursor = mysqldb.cursor()

#Cria o cursor com a conexao Postgres
postgrescursor = postgresdb.cursor()


#Executa consulta no MySQL
mysqlcursor.execute("SELECT CODIDENTIFICACAO, DSCSENHA FROM identificacao")

#Armazena em uma lista de tuplas o resultad da consulta
mysqlresult = mysqlcursor.fetchall()

#Fecha conexao com o cursor MySQL
mysqlcursor.close()

#Fecha conexao com o banco MySQL
mysqldb.close()

#Limpa a tabela
postgrescursor.execute("DELETE FROM identificacao;")
postgresdb.commit()

#Insere os dados da consulta do MySQL no Postgres
for x in mysqlresult:
    postgrescursor.execute("INSERT INTO identificacao(CODIDENTIFICACAO, DSCSENHA) VALUES(%s, %s) ON CONFLICT DO NOTHING;", x)

#Realiza o Commit no Postgres
postgresdb.commit()

#Fecha a conexao com o cursor Postgres
postgrescursor.close()

#Fecha a conexao com o banco Postgres
postgresdb.close()
