import sqlite3

arquivo_banco = 'banco.db'


#Iniciar conexão
def iniciar_conexao():
  conexao = None
  try:
    conexao = sqlite3.connect(arquivo_banco)
    print("Conexão Sucedida!!")
    
  except sqlite3.Error as e:
    print("OPs...Deu erro iniciando a conexão: ", e)
    
  return conexao

#Encerrar conexão
  
def fechar_conexao(conexao):
  if conexao:
    conexao.close()


    
#Criação de tabela
def criar_tabela(conexao, sql_criar_tabela):
  
  try:
    cursor = conexao.cursor()
    cursor.execute(sql_criar_tabela)
    print("Criação sucedida!")

  except sqlite3.Error as e:
    print('Erro!', e)


    
#Inserir Usuário
    
def inserir_user(conexao, sql_inserir_user):
  try:
    cursor = conexao.cursor()
    cursor.execute(sql_inserir_user)
    conexao.commit()
    print("Inserção Sucedida!")

  except sqlite3.Error as e:
    print('Não deu certo Animal!! ', e)


#Buscar User

def buscar_user(conexao, sql_buscar_user):
  user = None
  try:
    cursor = conexao.cursor()
    cursor.execute(sql_buscar_user)
    user = cursor.fetchall()

  except sqlite3.Error as e:
    print("Deu erro ", e)

  finally:
    return user


def deletar_atividade(conexao, sql_deletar_atividade):

  try:
    cursor = conexao.cursor()
    cursor.execute(sql_deletar_atividade)
    conexao.commit()
    print("Deu!")

  except sqlite3.Error as e:
    print("Não deu!", e)
