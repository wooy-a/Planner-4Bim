#Bibliotecas
from tkinter import*
from conexao import*
from user import*

#conexao com o Banco
conexao = iniciar_conexao()

sql_criar_tabela = "CREATE TABLE IF NOT EXISTS usuarios( id integer PRIMARY KEY AUTOINCREMENT, nome text NOT NULL, senha integer NOT NULL );"


criar_tabela(conexao, sql_criar_tabela)

inicio_user()