import streamlit as st
from langchain_ollama import OllamaLLM

# Streamlit Page Config
st.set_page_config(page_title="Emotional Blackhole Chat", page_icon="💬", layout="wide")

# Sidebar settings
st.sidebar.header("Settings")
model_name = st.sidebar.text_input("Model Name", value="phi3:latest")

# Initialize the Ollama model
llm = OllamaLLM(model=model_name)

# Title and description
st.title("💬 Emotional Blackhole Chat")
st.write("This chatbot helps explore thoughts and emotions. Type a message to start.")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# File upload functionality
uploaded_file = st.file_uploader("Upload a file", type=["txt", "pdf", "csv", "json"])
if uploaded_file:
    st.success(f"Uploaded file: {uploaded_file.name}")

# Clear chat button
if st.sidebar.button("Clear Chat"):
    st.session_state["messages"] = []
    st.rerun()

# Display chat history
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.text_area("Ask a question:", height=100)
if st.button("Send") and user_input:
    # Add user message to chat history
    st.session_state["messages"].append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Get response from the model
    try:
        response = llm.invoke(user_input)
    except Exception as e:
        response = "Error: Could not connect to the language model."
        st.error(response)
        st.text(f"Details: {str(e)}")
    
    # Add AI response to chat history
    st.session_state["messages"].append({"role": "assistant", "content": response})
    
    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(response)
