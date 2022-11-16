#Bibliotecas e módulos
from conexao import*
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import time
import user

conexao = iniciar_conexao()

class Planner:
  def __init__(self, atividade, data):
    self.atividade = atividade
    self.data = data

  #metodo 1
  def adicionar_atividade(self, nome_user):

    def destruir_janela():
      self.atividade = atividade.get()
      self.data = data.get()
      print(nome_user)
      sql_inserir_atv = "INSERT INTO "+nome_user+"(nome_atv, dia) VALUES ('" + self.atividade + "', '" + self.data + "')"
      
      inserir_user(conexao, sql_inserir_atv)
      janela.destroy()
      menu_planner(nome_user)
    janela = Tk()
    janela.title("Planner")
    janela.config(background="pink")
    
    label1 = Label(text="Atividade")
    label1.place(x = "100", y="70" )
    
    atividade = Entry(janela)
    atividade.place(x = '100', y = '90')

    label1 = Label(text="Data")
    label1.place(x = "100", y="110" )
    
    data = Entry(janela)
    data.place(x = '100', y = '130')

    botao = Button(janela, command = destruir_janela, text="Ir")
    botao.place(x = '150', y = '250')
    janela.mainloop()

  #metodo 2
  def exibir_atividade(self, nome):
    window = Tk() 
    window.geometry("600x350") 
    window.config(background="pink")
    
    def destruir_janela():
      window.destroy()
      menu_planner(nome)
    
    sql_buscar_dados = "SELECT * FROM "+nome
    
    aux = buscar_user(conexao, sql_buscar_dados)
    print(aux)
    treev = ttk.Treeview(window) 
    
    treev["columns"] = ("1", "2", "3") 
    
    treev['show'] = 'headings'
    
    treev.column("1", width = 90, anchor ='c') 
    treev.column("2", width = 90, anchor ='se') 
    treev.column("3", width = 90, anchor ='se') 
    
    treev.heading("1", text ="Id") 
    treev.heading("2", text="Nome")
    treev.heading("3", text ="Data") 

    treev.pack()

    botao = Button(window, command = destruir_janela, text="Sair")
    botao.place(x = '150', y = '350')
    
    for index in range(len(aux)):
      for busca in range(1):
        lista = aux[index]
        
        treev.insert("", 'end', values =(lista[busca], lista[busca+1], lista[busca+2])) 
        time.sleep(2)
            
    
  def excluir_atividade(self,nome):
    window = Tk() 
    window.geometry("600x350")
    window.config(background="pink")

    def destruir_janela():
      atv = desejo.get()
      sql_deletar_atividade = "DELETE from "+nome+" WHERE id = "+atv
      deletar_atividade(conexao, sql_deletar_atividade)
      window.destroy()
      menu_planner(nome)
    
    sql_buscar_dados = "SELECT * FROM "+nome
    
    aux = buscar_user(conexao, sql_buscar_dados)
    
    treev = ttk.Treeview(window) 
    
    treev["columns"] = ("1", "2", "3") 
    
    treev['show'] = 'headings'
    treev.pack()
    
    treev.column("1", width = 150, anchor ='c') 
    treev.column("2", width = 150, anchor ='se') 
    treev.column("3", width = 150, anchor="se")
    
    treev.heading("1", text ="Id") 
    
    treev.heading("2", text ="Nome") 

    treev.heading("3", text ="Data") 
    
    label_desejo = Label(text="Digite o ID da atividade que deseja excluir:")
    label_desejo.place(x = "100", y="250" )
    
    desejo = Entry(window)
    desejo.place(x = '100', y = '270')
    
    botao = Button(window, command = destruir_janela, text="Excluir")
    botao.place(x = '150', y = '300')
    
    for index in range(len(aux)):
      for busca in range(1):
        lista = aux[index]
        
        treev.insert("", 'end', values =(lista[busca], lista[busca+1], lista[busca+2])) 
        time.sleep(2)
            
    
#

 
def menu_planner(nome_def):
  sql_criar_tabela = "CREATE TABLE IF NOT EXISTS '"+nome_def+"'( id integer PRIMARY KEY AUTOINCREMENT, nome_atv text NOT NULL, dia text NOT NULL );"

  criar_tabela(conexao, sql_criar_tabela)
  
  janela = Tk()
  janela.title("Planner")
  janela.geometry("310x310")
  janela.config(background="#87CEEB")
  nome_user = nome_def

  def destruir_janela():
    opcao = int(desejo.get())
    usuario = Planner("",0)
    
    if opcao == 1:
      janela.destroy()
      usuario.adicionar_atividade(nome_user)

    elif opcao == 2:
      janela.destroy()
      usuario.exibir_atividade(nome_user)

    elif opcao == 3:
      janela.destroy()
      usuario.excluir_atividade(nome_user)

    elif opcao == 4:
      janela.destroy()
      user.inicio_user()

  label = Label(text="Bem Vindo ao Planner!")
  label.place(x = '100', y = '70')
  
  label = Label(text="Selecione uma opção")
  label.place(x = '100', y = '90')
  
  label1 = Label(text="1. Adicionar Atividade")
  label1.place(x = '100', y = '120')

  label1 = Label(text="2. Exibir Atividades")
  label1.place(x = '100', y = '140')


  label1 = Label(text="3. Excluir Atividade")
  label1.place(x = '100', y = '160')

  label1 = Label(text="4. Sair")
  label1.place(x = '100', y = '180')
  
  desejo = Entry(janela)
  desejo.place(x = '100', y = '210')

  opcao = desejo.get()
  
  botao = Button(janela, command = destruir_janela, text="Ir")
  botao.place(x = '150', y = '250')
  janela.mainloop()
