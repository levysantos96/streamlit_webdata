# %%
import pandas as pd
from selenium import  webdriver
from selenium.webdriver.common.by import By
import sqlalchemy as db




# %%
#pip install sqlalchemy

# %%
navegador = webdriver.Chrome()

# %%
navegador.get('https://pt.wikipedia.org/wiki/Lista_das_melhores_universidades_do_mundo')

# %%
posicao = navegador.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[1]/td[1]').text
nome = navegador.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[1]/thead/tr/th[2]').text
pais = navegador.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[1]/thead/tr/th[3]').text
pontos = navegador.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[1]/thead/tr/th[4]').text
tipoinstituicao = navegador.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[1]/thead/tr/th[5]').text

# %%
print(posicao)
print(nome)
print(pais)
print(pontos)
print(tipoinstituicao)

# %%
lista_posicao = []
for i in range(1, 101):
    posicao = navegador.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr['+str(i)+']/td[1]').text
    lista_posicao.append(posicao)
print(lista_posicao)

# %%
lista_nome = []
for i in range(1, 101):
    nome = navegador.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr['+str(i)+']/td[2]').text
    lista_nome.append(nome)
print(lista_nome)
    

# %%
lista_pais = []
for i in range(1, 101):
    pais = navegador.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr['+str(i)+']/td[3]').text
    lista_pais.append(pais)
print(lista_pais)

# %%
lista_pontos = []
for i in range(1, 101):
    pontos = navegador.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr['+str(i)+']/td[4]').text
    lista_pontos.append(pontos)
print(lista_pontos)

# %%
lista_tipoinstituicao = []
for i in range(1, 101):
    tipoinstituicao = navegador.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr['+str(i)+']/td[5]').text
    lista_tipoinstituicao.append(tipoinstituicao)
print(lista_tipoinstituicao)

# %%
df = pd.DataFrame(lista_posicao, columns=['Posição'])
df['Nome da Instituição'] = lista_nome
df['País'] = lista_pais
df['Pontos'] = lista_pontos
df['Tipo de Instituição'] = lista_tipoinstituicao
df




# %%
#df.to_csv('dados_originais.csv', sep=';', index=False)
df.to_csv('../0_bases_originais/dados_originais', sep=';', index=False, encoding='UTF-8')

# %%
df.to_csv('../1_bases_tratadas/dados_tratados', sep=';', index=False, encoding='UTF-8')

# %%
df.to_json('../0_bases_originais/dados_originais.json')

# %%
engine = db.create_engine("sqlite:///banco_univerdidades.db", echo=True)
conn = engine.connect()


# %%
df.to_sql('../banco_univerdidades.db', con=conn)


