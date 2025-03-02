# Emotional Blackhole Chat - RAG App

Emotional Blackhole Chat is a Retrieval-Augmented Generation (RAG) application built with Streamlit and Ollama. This chatbot is designed to facilitate deep conversations about emotions and thoughts.

## Features
- **Interactive Chat Interface**: Engage in AI-powered conversations.
- **File Upload Support**: Upload text, PDF, CSV, or JSON files for processing.
- **Retrieval-Augmented Generation (RAG)**: Provides responses based on retrieved context.
- **Customizable Model Selection**: Users can specify the model name.
- **Chat History Maintenance**: Stores and displays previous interactions.
- **Clear Chat Option**: Reset conversations anytime.

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.9+
- Streamlit
- Langchain Ollama

### Clone the Repository
```bash
git clone https://github.com/your-username/emotional-blackhole-chat.git
cd emotional-blackhole-chat
```

### Create a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
To start the application, run:
```bash
streamlit run app.py
```

## File Upload Support
Users can upload `.txt`, `.pdf`, `.csv`, or `.json` files for processing.

## Error Handling
If the model is unavailable or there is a connection issue, an appropriate error message will be displayed.

## Contributing
Feel free to submit pull requests or report issues.

## License
MIT License

## Author
[Zadid Ahsan Nabi]
