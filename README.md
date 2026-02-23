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

```bash
streamlit run app.py
```

### 🌐 Opção 3: Execução no Google Colab com ngrok

Caso deseje rodar a aplicação no Colab com interface web:

#### 1️⃣ Instale as dependências

```bash
!pip install streamlit pyngrok google-genai
```

#### 2️⃣ Configure sua chave Gemini

```bash
import os
os.environ["GEMINI_API_KEY"] = "SUA_CHAVE_AQUI"
```

#### 3️⃣ Execute o app com túnel público

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

