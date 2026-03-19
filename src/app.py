import json
import pandas as pd
import requests
import streamlit as st
from PyPDF2 import PdfReader

# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# ============ Leitor de PDF ============
# Função para ler o conteúdo de um PDF
def ler_pdf(caminho_arquivo):
    # Abre o arquivo PDF em modo binário de leitura
    with open(caminho_arquivo, 'rb') as arquivo:
        # Cria um objeto Reader
        leitor_pdf = PdfReader(arquivo)
        
        # Obtém o número total de páginas
        num_paginas = len(leitor_pdf.pages)
        print(f"O PDF tem {num_paginas} páginas.")
        
        # Extrai o texto de cada página
        conteudo = ""
        for i in range(num_paginas):
            pagina = leitor_pdf.pages[i]
            texto = pagina.extract_text()
            conteudo += f"--- Página {i+1} ---{texto}"
        
        return conteudo

# ================== Contexto ============

# 1. Simulando os dados do usuário (Isso viria do seu banco de dados ou inputs do Streamlit)
perfil = {
    'nome': 'Alex',
    'idade': 19,
    'perfil_investidor': 'Conservador (Iniciante)',
    'objetivo_principal': 'Criar reserva de emergência para ter tranquilidade enquanto estuda para a faculdade de Ciência de Dados e futuros concursos públicos.',
    'patrimonio_total': 1500.00,
    'reserva_emergencia_atual': 500.00
}

# 2. Simulando um histórico de transações com Pandas DataFrame
transacoes = pd.DataFrame([
    {'Data': '2026-03-01', 'Tipo': 'Aporte', 'Ativo': 'Tesouro Selic', 'Valor': 200.00},
    {'Data': '2026-03-15', 'Tipo': 'Aporte', 'Ativo': 'CDB Liquidez Diária', 'Valor': 100.00}
])

# 3. Simulando as últimas perguntas que o cliente fez ao GuU
historico = pd.DataFrame([
    {'Data': '2026-02-10', 'Interação': 'Perguntou como começar a investir com 100 reais.'},
    {'Data': '2026-02-28', 'Interação': 'Pediu explicação sobre a diferença entre CDB e Tesouro Direto.'}
])

# 4. Simulando o catálogo de produtos disponíveis em formato de dicionário/JSON
produtos = [
    {
        "nome": "Tesouro Selic 2029", 
        "tipo": "Renda Fixa", 
        "risco": "Muito Baixo", 
        "rentabilidade_esperada": "100% da Selic", 
        "liquidez": "D+0 (Imediata)"
    },
    {
        "nome": "CDB Banco X", 
        "tipo": "Renda Fixa", 
        "risco": "Baixo", 
        "rentabilidade_esperada": "110% do CDI", 
        "liquidez": "Diária"
    }
]

# ============ MONTAR CONTEXTO ============
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

print(contexto)


# ============ CARREGAR DADOS ============
caminho_1 = "dio-lab-bia-do-futuro-main/data/07.-Investimento-en-a-es-para-iniciantes-Autor-Fernando-Da-Silva-Franco.pdf"
texto_pdf_1 = ler_pdf(caminho_1)
caminho_2 = "dio-lab-bia-do-futuro-main/data/13.-Introdu-o-aos-Investimentos-Autor-Portal-do-Investidor.pdf"
texto_pdf_2 = ler_pdf(caminho_2)
caminho_7 = "dio-lab-bia-do-futuro-main/data/Ebook-Guia-de-Investimentos-para-Iniciantes.pdf"
texto_pdf_7 = ler_pdf(caminho_7)
historico_investimentos = pd.read_csv('dio-lab-bia-do-futuro-main/data/Tendências da Bolsa de Valores e Ações em Destaque.csv')
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
def perguntar(msg, historico):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    HISTÓRICO DA CONVERSA:
    {historico}

    Pergunta do Usuário: {msg}
    Resposta do GuU:"""

    try:
        r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
        r.raise_for_status()
        return r.json().get('response', "Erro ao gerar resposta.")
    except Exception as e:
        return f"Erro de conexão com o Ollama: {e}"

# ============ INTERFACE ============
st.set_page_config(page_title="GuU - Educador Financeiro", page_icon="🎓")
st.title("🎓 GuU, o Educador Financeiro")

# Histórico de sessão
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

for msg in st.session_state.mensagens:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.session_state.mensagens.append({"role": "user", "content": pergunta})
    with st.chat_message("user"):
        st.markdown(pergunta)
    
    # Prepara as últimas mensagens para o modelo lembrar do contexto
    historico_str = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.mensagens[-3:]])

    with st.spinner("GuU está analisando seus dados..."):
        resposta = perguntar(pergunta, historico_str)
        
        st.session_state.mensagens.append({"role": "assistant", "content": resposta})
        with st.chat_message("assistant"):
            st.markdown(resposta)

