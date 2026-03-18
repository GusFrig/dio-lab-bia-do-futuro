import json
import pandas as pd
import requests
import streamlit as st
from PyPDF2 import PdfWriter

# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# ============ Leitor de PDF ============
# Função para ler o conteúdo de um PDF
def ler_pdf(caminho_arquivo):
    # Abre o arquivo PDF em modo binário de leitura
    with open(caminho_arquivo, 'rb') as arquivo:
        # Cria um objeto Reader
        leitor_pdf = PyPDF2.PdfReader(arquivo)
        
        # Obtém o número total de páginas
        num_paginas = len(leitor_pdf.pages)
        print(f"O PDF tem {num_paginas} páginas.
")
        
        # Extrai o texto de cada página
        conteudo = ""
        for i in range(num_paginas):
            pagina = leitor_pdf.pages[i]
            texto = pagina.extract_text()
            conteudo += f"--- Página {i+1} ---
{texto}
"
        
        return conteudo

# ============ CARREGAR DADOS ============
caminho_1 = "data/07.-Investimento-en-a-es-para-iniciantes-Autor-Fernando-Da-Silva-Franco.pdf"
texto_pdf_1 = ler_pdf(caminho_1)
caminho_2 = "data/13.-Introdu-o-aos-Investimentos-Autor-Portal-do-Investidor.pdf"
texto_pdf_2 = ler_pdf(caminho_2)
caminho_3 = "data/21.-Guia-legal-para-o-investidor-estrangeiro-no-Brasil-Autor-Invest-Export-Brasil.pdf"
texto_pdf_3 = ler_pdf(caminho_3)
caminho_4 = "data/An-lise-de-Investimentos-V-rios-Autores (1).pdf"
texto_pdf_4 = ler_pdf(caminho_4)
caminho_5 = "data/Apostila-Investimentos-Harion-Camargo.pdf"
texto_pdf_5 ler_pdf(caminho_5)
caminho_6 = "data/Da-Pequena-Empresa-ao-Mercado-de-Capitais-V-rios-Autores.pdf"
texto_pdf_6 = ler_pdf(caminho_6)
caminho_7 = "data/Ebook-Guia-de-Investimentos-para-Iniciantes.pdf"
texto_pdf_7 = ler_pdf(caminho_7)
historico_investimentos = pd.read_csv('.data/Tendências da Bolsa de Valores e Ações em Destaque.csv')
perfil_investidor = "https://investimentos.com.br/artigos/perfil-de-investidor/"

# ============ SYSTEM PROMPT ============
SYSTEM_PROMPT = """Você é o GuU, um educador financeiro amigável e didático.

OBJETIVO:
Ensinar conceitos básicos de investimentos, construir perfils de investimentos e indicar investimentos com base em perfis.

REGRAS:
- JAMAIS responda a perguntas fora do tema ensino de investimentos. 
  Quando ocorrer, responda lembrando o seu papel de educador financeiro;
- Use os dados fornecidos para dar exemplos personalizados;
- Linguagem simples, como se explicasse para um amigo;
- Se não souber algo, admita: "Não tenho essa informação, mas posso explicar...";
- Sempre pergunte se o cliente entendeu;
- Responda de forma sucinta e direta, com no máximo 3 parágrafos.
"""

# ============ CHAMAR OLLAMA ============
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ============ INTERFACE ============
st.title("🎓 GuU, o Educador Financeiro")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
