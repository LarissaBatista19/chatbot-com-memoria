# Chatbot com memória 🤖

**Disciplina:** Inteligência Artificial - Turma 01 (2025.2)  
**Professor:** Hendrik Macedo  
**Instituição:** Universidade Federal de Sergipe (UFS) / Departamento de Computação (DCOMP)  


## 👥 Equipe
* Ellen Karolliny dos Santos
* Ellen Vitoria Menezes Lima
* João Santos Rocha
* Larissa Batista dos Santos
* Tasso Marcel de Oliveira

  
## 🎯 Sobre o Projeto
Este repositório contém o **Aplicativo 2 (Unidade 4)** solicitado na disciplina de Inteligência Artificial. O objetivo é demonstrar a aplicação prática do uso de **LLMs** para a resolução de problemas.


## 🚀 Como Executar o Projeto

### ✅ Opção 1: Direto no Navegador (Recomendado)
A forma mais rápida e fácil de testar a aplicação e visualizar o chat conversacional é acessando o deploy oficial na nuvem. Não requer nenhuma instalação ou configuração:

👉 **[Acessar a Aplicação no Streamlit](https://chatbot-com-memoria.streamlit.app/)**

### 💻 Opção 2: Execução Local (Computador)

#### 1️⃣ Clone o repositório

```bash
git clone https://github.com/LarissaBatista19/chatbot-com-memoria.git
cd chatbot-com-memoria
```

#### 2️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

#### 3️⃣ Configure sua chave da API Gemini

Crie um arquivo .env na raiz do projeto contendo:

```bash
GEMINI_API_KEY=sua_chave_aqui
```

A chave pode ser obtida em: **https://aistudio.google.com/**

#### 4️⃣ Execute o aplicativo

Troque o seguite parte de app.py:

```bash
api_key = st.secrets["GEMINI_API_KEY"]
```

Por:

```bash
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
```

Salve e execute no terminal:

```bash
streamlit run app.py
```

### 🌐 Opção 3: Execução no Google Colab com ngrok

Caso deseje rodar a aplicação no Colab com interface web:

#### 1️⃣ Instale as dependências

```bash
!pip install streamlit pyngrok google-genai python-dotenv
```

#### 2️⃣ Configure sua chave Gemini como na versão local

#### 3️ Execute o app com túnel público

```bash
from pyngrok import ngrok
import subprocess

ngrok.set_auth_token("SEU_AUTHTOKEN_NGROK")

public_url = ngrok.connect(8501)
print("Abra este link:", public_url)

subprocess.Popen(["streamlit", "run", "app.py"])
```

⚠️ É necessário criar conta gratuita em: **https://ngrok.com**

E gerar um Authtoken no dashboard.

## 🖥️ Versão com Ollama (Execução Local com Modelo Offline)

Além da versão utilizando a API Gemini, o repositório também disponibiliza uma versão do chatbot utilizando Ollama, permitindo a execução local de um modelo de linguagem sem dependência de API externa. Comece clonando o repositório.

#### 1️⃣ Instale o Ollama

Faça o download em:

👉 **https://ollama.com/**

#### 2️⃣ Baixe o modelo Orca Mini

```bash
ollama pull orca-mini
```

#### 3️⃣ Execute o modelo

```bash
ollama run orca-mini
```

#### 4️⃣ Execute a versão do app com Ollama

```bash
python chatbot.py
```

Essa versão permite:

Execução totalmente local

Sem custo por requisição

Independência de conexão com API externa

⚠️ O desempenho pode variar dependendo do hardware utilizado.

## 📚 Google Colab

Também é possível executar o projeto diretamente no Google Colab:

👉 **[Abrir no Google Colab](https://colab.research.google.com/drive/16510k0r98ikDSv6uwD80TpthXrqt2GoP?usp=sharing#scrollTo=VEOGG6cFlrds)**


