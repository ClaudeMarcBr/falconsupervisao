#Copyright (c) 2026 Claude Païssé
#Programa de entrada de ronda para Daniel da Falcon
# Passo a passo do projeto
# Passo 1: Criar a tela do sistema
# Passo 2: Criar o formulário de cadastro de visitas
# Passo 3: Salvar a a visita na base de dados
# Passo 4: Mostrar a base de dados na tela
# Passo 5: Criar o dpipashboard com os gráficos

#requerimentos
import os
import streamlit as st
import pandas as pd
import plotly.express as px

#Passo 1: tela do sistema
st.write("## Sistema de Visitas de supervisão da Falcon")
st.markdown(
    '<h4 style="margin-left: 40px;">by Claude Païssé</p>',
    unsafe_allow_html=True
)

# Passo 2: Criar o formulário de cadastro e, se aruivo não existir, criar um arquivo csv com as colunas
arquivo = "visitas.csv"
colunas = ["Data", "Hora", "Supervisor", "Condomínio", "Funcionário", "Observações"]
if os.path.exists(arquivo):
    tabela = pd.read_csv(arquivo)
    print("Arquivo existente carregado.")
else:
    tabela = pd.DataFrame(columns=colunas)
    tabela.to_csv(arquivo, index=False)
    print("Arquivo criado com uma tabela vazia.")
print(tabela)

    #carregar banco de dados
tabela = pd.read_csv("visitas.csv")

st.sidebar.write("## Cadastrar visita")

data = st.sidebar.date_input("Data")

hora = st.sidebar.time_input("Hora")

with open("Supervisores.txt", "r", encoding="utf-8") as arquivo:    
    supervisores = [linha.strip() for linha in arquivo if linha.strip()]
supervisor = st.sidebar.selectbox("Supervisor", supervisores)   

with open("Condominios.txt", "r", encoding="utf-8") as arquivo:
    condominios = [linha.strip() for linha in arquivo if linha.strip()]
condo = st.sidebar.selectbox("Condomínio", condominios)

with open("Funcionarios.txt", "r", encoding="utf-8") as arquivo:
    funcionarios = [linha.strip() for linha in arquivo if linha.strip()]
funcionario = st.sidebar.selectbox("Funcionário", funcionarios)

obs = st.sidebar.text_area("Observações")

limpeza = st.sidebar.checkbox("Limpeza realizada?")

#botao = st.sidebar.button("Cadastrar visita")

# Passo 3: Salvar a visita na base de dados
if botao:
    nova_visita = [data, hora, supervisor, condo, funcionario, obs]
    tabela.loc[len(tabela)] = nova_visita
    tabela.to_csv("visitas.csv", index=False)
    st.success("Visita cadastrada!")

# Passo 4: Mostrar a base de dados na tela
st.write("## Visitas cadastradas")
st.dataframe(tabela)

# Passo 5: Criar o dashboard
st.write("## Dashboard")

grafico2 = px.pie(tabela, names="Supervisor")
st.plotly_chart(grafico2)
