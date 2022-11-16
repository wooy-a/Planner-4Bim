#Bibliotecas e Módulos
from conexao import*
from tkinter import*
from tkinter import messagebox
from planner import*
import time


conexao = iniciar_conexao()

class Cadastro:
  #Construtor
  def __init__(self, nome, senha):
    self.nome = nome
    self.senha = senha

  #Metodo 1
    
  def cadastro(self, conexao):
    janela = Tk()
    janela.title("PLANNER PEIXES")
    janela.config(background="#EE82EE")
    janela.geometry("310x300")

    #
    def destruir_janela():
      self.nome = nome.get()
      self.senha = senha.get()
  
      sql_inserir_user = "INSERT INTO usuarios(nome, senha) VALUES ('" + self.nome + "', '" + self.senha + "')"
      
      inserir_user(conexao, sql_inserir_user)
      messagebox.showinfo("Usuário Cadastrado!", "Foi cadastrado!")
      time.sleep(3)
      janela.destroy()
      inicio_user()
    #
      
    label1 = Label(text="Nome")
    label1.place(x = "100", y="70" )
    
    nome = Entry(janela)
    nome.place(x = '100', y = '100')
    
    label2 = Label(text="Senha")
    label2.place(x = "100", y="130" )
    
    senha = Entry(janela)
    senha.place(x = '100', y = '150')

    
    botao = Button(janela, command = destruir_janela, text="Cadastrar")
    botao.place(x = '130', y = '180')

    
    janela.mainloop()

  #Login
    
  def login_user(self):
    janela = Tk()
    janela.title("Planner")
    janela.config(background="pink")
    janela.geometry("310x300")
    
    def destruir_janela():
      
      global confirmNome
      global confirmSenha
      global lista
      lista = []
      confirmNome = 's'
      confirmSenha = 0
      
      self.nome = nome.get()
      self.senha = int(senha.get())
      
      sql_buscar_dados = "SELECT * FROM usuarios"
      
  
      aux = buscar_user(conexao, sql_buscar_dados)
  
      for index in range(len(aux)):
        for busca in range(3):
          lista = aux[index]
          
          if self.nome == lista[busca]:     
            confirmNome = True
            nome_user = self.nome
            time.sleep(2)
  
          
        for index in range(len(aux)):
          for busca in range(3):
            lista = aux[index]
            
            if self.senha == lista[busca]:
              confirmSenha = True
              time.sleep(2)
  
        if confirmNome == True and confirmSenha == True:
          messagebox.showinfo('Dados válidos!!', "Bem Vindo!")
          janela.destroy()
          menu_planner(nome_user)

        elif confirmNome == 's' and confirmSenha == 0:
          messagebox.showinfo("Error", "Usuário não cadastrado!")
          janela.destroy()
          inicio()



    label1 = Label(text="Nome")
    label1.place(x = "100", y="70" )
    
    nome = Entry(janela)
    nome.place(x = '100', y = '100')
    
    label2 = Label(text="Senha")
    label2.place(x = "100", y="130" )
    
    senha = Entry(janela)
    senha.place(x = '100', y = '150')

    
    botao = Button(janela, command = destruir_janela, text="Entrar")
    botao.place(x = '130', y = '180')

    janela.mainloop()

def inicio_user():
  janela = Tk()
  janela.title("Projeto Integrador")
  janela.config(background="#7B68EE")
  janela.geometry("310x300")

  #destruir janela e ir para a opcao desejada
  def destruir_janela():
    opcao = int(x.get())
    janela.destroy()
    
    if opcao == 1:
      usuario.cadastro(conexao)

    elif opcao == 2:
      usuario.login_user()

    else:
      messagebox.showinfo("Error", "Opção inexistente!")
  #

  label = Label(text="OQ DESEJA FAZER?")
  label.place(x = '100', y = '70')
  
  label1 = Label(text="1. Cadastrar conta")
  label1.place(x = '100', y = '90')

  label1 = Label(text="2. Efetuar Login")
  label1.place(x = '100', y = '110')
  
  x = Entry(janela)
  x.place(x = '100', y = '130')
  
  botao = Button(janela, command = destruir_janela, text="Enter")
  botao.place(x = '150', y = '155')

  janela.mainloop()

usuario = Cadastro(0,0)