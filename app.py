import streamlit as st
from google import genai

api_key = st.secrets("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY não encontrada no .env")

client = genai.Client(api_key=api_key)

#Configuração do Modelo
MODEL_CONFIG = {
    "model_name": "gemini-2.5-flash",
    "temperature": 0.7,
    "max_tokens": 5000
}

# Gestão de Contexto
def TRUNCATE_HISTORY(history, limit):
    if len(history) > limit:
        # Mantém o System Prompt fixo e remove mensagens antigas se necessário
        history.pop(1)
    return history

def CALL_LLM_API(config, payload):
    # Constrói o prompt a partir do histórico
    contents = []
    for msg in payload:
        if msg["role"] == "user":
          contents.append({
              "role": "user", 
              "parts": [{"text": msg["content"]}] 
          })
        elif msg["role"] == "assistant":
            contents.append({
              "role": "model", 
              "parts": [{"text": msg["content"]}]
            })

    response = client.models.generate_content(
        model=config["model_name"],
        contents=contents,
        config={
            "temperature": config["temperature"],
            "max_output_tokens": config["max_tokens"]
        }
    )

    return response.text

# Agente Conversacional
def CONVERSATIONAL_AGENT(user_input, history, config):
    history.append({"role": "user", "content": user_input})
    payload = TRUNCATE_HISTORY(history, config["max_tokens"])

    api_response = CALL_LLM_API(config, payload)

    reply_text = api_response
    history.append({"role": "assistant", "content": reply_text})

    return reply_text, history

st.set_page_config(page_title="Chatbot Gemini", page_icon=":robot:")

st.title("Chatbot Gemini")
st.caption("Modelo: gemini-2.5-flash")

if "history" not in st.session_state:
    st.session_state.history = [
        {"role": "system", "content": "Você é um programador."}
    ]

for msg in st.session_state.history:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(msg["content"])

user_input = st.chat_input("Digite uma pergunta...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    
    with st.spinner("Pensando..."):
        try:
            resposta, st.session_state.history = CONVERSATIONAL_AGENT(
                user_input,
                st.session_state.history,
                MODEL_CONFIG
            )
            
            with st.chat_message("assistant"):
              st.markdown(resposta)

        except Exception as e:
            st.error(f"Erro de Conexão: {e}")
