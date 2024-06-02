import streamlit as st
import pandas  as pd
import plotly.express as px

st.write('**Pesquisa Universidades**')
st.sidebar.header('Pesquise a universidades')
st.image('https://canaldoensino.com.br/blog/wp-content/uploads/2018/03/como-conseguir-uma-bolsa-de-estudo-integral-numa-universidade-privada_Prancheta-1.jpg')
df = pd.read_csv("dados_tratados.csv")

uni = df['País'].drop_duplicates()
escolha_uni = st.sidebar.selectbox('País', uni)
df2 = df[df['País']==escolha_uni]


fig = px.bar(df2, x='Nome da Instituição', y='Pontos')
st.plotly_chart(fig)

fig2 = px.pie(df, 'País')
st.plotly_chart(fig2)

fig3 = px.box(df,'Pontos')
st.plotly_chart(fig3)
