import streamlit as st
import requests
import json

backend_url = "https://seu-backend-no-render.com/submit_form"

def create_form():
    st.title("Malinha Form")
    
    st.write("Explore a moda no conforto da sua casa!")
    st.write("Enviamos diretamente para você, em São Paulo, uma malinha personalizada com peças escolhidas especialmente para seu estilo e necessidades. Preencha o formulário, receba sua seleção e descubra peças perfeitas para você!")
    
    nome = st.text_input("Nome*")
    telefone_ddd = st.text_input("Telefone com ddd*")
    email = st.text_input("Email*")
    tamanho_roupas = st.selectbox("Quais tamanhos você geralmente utiliza em suas Roupas", ["Please Select", "PP", "P", "M", "G", "GG"])
    tamanho_pijamas = st.selectbox("Quais tamanhos você geralmente utiliza em seus Pijamas", ["Please Select", "PP", "P", "M", "G", "GG"])
    ocasioes = st.selectbox("Ocasiões", ["Please Select", "Casual", "Trabalho", "Festa", "Esporte"])
    estilos_preferidos = st.selectbox("Estilos preferidos", ["Please Select", "Clássico", "Moderno", "Esportivo", "Elegante", "Despojado"])
    cep = st.text_input("CEP*")
    numero = st.text_input("Número*")
    numero_unidade = st.text_input("Número da unidade (Caso haja)")
    
    if st.button("Enviar"):
        if not nome or not telefone_ddd or not email or not cep or not numero:
            st.error("Por favor, preencha todos os campos obrigatórios.")
        else:
            st.success("Formulário enviado com sucesso!")
            st.write(f"Nome: {nome}")
            st.write(f"Telefone com ddd: {telefone_ddd}")
            st.write(f"Email: {email}")
            st.write(f"Tamanho de roupas: {tamanho_roupas}")
            st.write(f"Tamanho de pijamas: {tamanho_pijamas}")
            st.write(f"Ocasioes: {ocasioes}")
            st.write(f"Estilos preferidos: {estilos_preferidos}")
            st.write(f"CEP: {cep}")
            st.write(f"Número: {numero}")
            st.write(f"Número da unidade: {numero_unidade}")
            
            # Preparar os dados para enviar ao backend
            data = {
                "nome": nome,
                "telefone_ddd": telefone_ddd,
                "email": email,
                "tamanho_roupas": tamanho_roupas,
                "tamanho_pijamas": tamanho_pijamas,
                "ocasioes": ocasioes,
                "estilos_preferidos": estilos_preferidos,
                "cep": cep,
                "numero": numero,
                "numero_unidade": numero_unidade
            }
            
            # Enviar dados para o backend
            response = requests.post(backend_url, json=data)
            
            if response.status_code == 200:
                st.write("Email enviado com sucesso!")
            else:
                st.write("Ocorreu um erro ao processar o formulário.")

if __name__ == "__main__":
    create_form()
