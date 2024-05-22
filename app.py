import streamlit as st
import requests

backend_url = "https://malinha.onrender.com/submit_form"  # Certifique-se de substituir pela URL correta

def create_form():
    st.title("Monte sua Malinha")
    
    st.write("Explore a moda no conforto da sua casa!")
    st.write("Enviamos diretamente para você, em São Paulo, uma malinha personalizada com peças escolhidas especialmente para seu estilo e necessidades. Preencha o formulário, receba sua seleção e descubra peças perfeitas para você!")
    
    nome = st.text_input("Nome*")
    telefone_ddd = st.text_input("Telefone com ddd*")
    email = st.text_input("Email*")
    tamanho_roupas = st.selectbox("Quais tamanhos você geralmente utiliza em suas Roupas", ["P", "M", "G", "GG"])
    tamanho_pijamas = st.selectbox("Quais tamanhos você geralmente utiliza em seus Pijamas", ["P", "M", "G", "GG", "XG"])
    ocasioes = st.selectbox("Ocasiões", ["Casual", "Trabalho", "Eventos formais", "Atividades de lazer"])
    estilos_preferidos = st.selectbox("Estilos preferidos", ["Clássico", "Moderno", "Esportivo", "Boho"])
    cep = st.text_input("CEP*")
    numero = st.text_input("Número*")
    numero_unidade = st.text_input("Número da unidade (Caso haja)")
    
    if st.button("Enviar"):
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
            st.success("Formulário enviado com sucesso!")
            st.write("Email enviado com sucesso!")
        else:
            st.error("Ocorreu um erro ao processar o formulário.")
            st.write(response.json().get("message", "Erro desconhecido"))

if __name__ == "__main__":
    create_form()

