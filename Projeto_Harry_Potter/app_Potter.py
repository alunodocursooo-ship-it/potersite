import streamlit as st
import requests

# URL da API com todos os personagens
url = "https://hp-api.onrender.com/api/characters"

# Faz a requisição para pegar os dados
resposta = requests.get(url)
dados = resposta.json()

# Pega apenas os nomes dos personagens , a partir de uma lista vazia
nomes = []
for personagem in dados:
    nomes.append(personagem['name'])


# Ordena os nomes em ordem alfabética
nomes.sort()

# Título do app
st.title('Busca Bruxo - O Lugar onde encontrará todas as informações dos bruxos.')

# Sidebar com a lista de nomes
nome_escolhido = st.selectbox('Escolha um Bruxo',nomes)

# Procura o personagem escolhido na lista de dados
personagem = None
for p in dados:
    if p['name'] == nome_escolhido:
        personagem = p
        break

# Mostra o nome do personagem
st.header(f'Nomes do Personagem{personagem['name']}')

# ===== IMAGEM EM DESTAQUE =====
# Verifica se o personagem tem imagem


# Linha divisória


# Informações principais


# Informações da varinha





# Mostra se está vivo
