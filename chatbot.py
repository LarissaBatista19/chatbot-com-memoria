# 1. Instala a dependência zstd exigida pela nova versão do instalador
# !apt-get update && apt-get install -y zstd
# print("Instalação zstd concluída.")

# 2. Instala o Ollama
# !curl -fsSL https://ollama.com/install.sh | sh
# print("Instalação ollama concluído.")

# 3. Inicia o servidor em segundo plano
import subprocess
import time

try:
    subprocess.Popen(['ollama', 'serve'])
    print("Servidor Ollama iniciando...")
except Exception as e:
    print(f"Erro ao iniciar servidor: {e}")

# 4. Pausa para o servidor estabilizar e baixa o modelo
# time.sleep(10)
# !ollama pull orca-mini

import requests

#Configuração do Modelo
MODEL_CONFIG = {
    "model_name": "orca-mini",
    "temperature": 0.7,
    "max_tokens": 800
}

#Configuração da API Local Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"

# Gestão de Contexto
def TRUNCATE_HISTORY(history, limit):
    if len(history) > limit:
        # Mantém o System Prompt fixo e remove mensagens antigas se necessário
        history.pop(1)
    return history

# Chamada de Inferência com Ollama Local
def CALL_LLM_API(config, payload):
    # Constrói o prompt a partir do histórico
    prompt = ""
    for msg in payload:
        if msg["role"] == "system":
            prompt += f"Sistema: {msg['content']}\n"
        elif msg["role"] == "user":
            prompt += f"Você: {msg['content']}\n"
        else:
            prompt += f"IA: {msg['content']}\n"

    prompt += "IA: "

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": config["model_name"],
            "prompt": prompt,
            "temperature": config["temperature"],
            "max_tokens": config["max_tokens"],
            "stream": False
        }
    )

    if response.status_code != 200:
        raise Exception(f"Erro Ollama: {response.text}")

    return response.json()["response"]

# Agente Conversacional
def CONVERSATIONAL_AGENT(user_input, history, config):
    history.append({"role": "user", "content": user_input})
    payload = TRUNCATE_HISTORY(history, config["max_tokens"])

    api_response = CALL_LLM_API(config, payload)

    reply_text = api_response
    history.append({"role": "assistant", "content": reply_text})

    return reply_text, history

if __name__ == "__main__":
    chat_history = [{"role": "system", "content": "Você é um programador."}]       # Define o papel da IA
    print("--- Sistema Pronto ---")

    while True:
        entrada = input("\nDigite uma pergunta: ")
        if entrada.lower() == "sair": break

        try:
            res, chat_history = CONVERSATIONAL_AGENT(entrada, chat_history, MODEL_CONFIG)
            print(f"Resposta da IA: {res}")
        except Exception as e:
            print(f"Erro de Conexão: {e}")
