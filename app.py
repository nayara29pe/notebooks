
import pandas as pd
import plotly.express as px
import streamlit as st
     
st.header('Veículos a venda')

car_data = pd.read_csv('vehicles.csv') # lendo os dados

hist_button = st.button('Criar histograma') # criar um botão
     
if hist_button: # se o botão for clicado
         # escrever uma mensagem
         st.write('Criando um histograma para a comparação de quilometragem entre os carros a venda')
         
         # criar um histograma
         fig = px.histogram(car_data, x="odometer")
     
         # exibir um gráfico Plotly interativo
         st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar dispersão')
     
if scatter_button: # se o botão for clicado
         # escrever uma mensagem
         st.write('Criando um gráfico de dispersão para a comparação de quilometragem e preço entre os carros a venda')
         
         # criar um gráfico de dispersão
         fig = px.scatter(car_data, x="odometer", y="price")
     
         # exibir um gráfico Plotly interativo
         st.plotly_chart(fig, use_container_width=True)



     