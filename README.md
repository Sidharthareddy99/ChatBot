# 🤗💬 HugChat App

Welcome to the **HugChat App**, an AI-powered chatbot built using [Streamlit](https://streamlit.io/) and the [🤗Hugging Face](https://huggingface.co/) API. This app leverages the **zephyr-7b-beta** large language model (LLM) to provide interactive and intelligent conversations.

[Project Link](https://sidharthachatbot.streamlit.app)

## 🚀 Features

- **User-Friendly Interface**: A simple and clean UI built with Streamlit.
- **Persistent Chat History**: Chat history is saved and can be cleared with a single click.
- **Real-time Chat**: Interact with the AI in real-time with smooth streaming of responses.
- **Customizable Models**: Easily switch between different LLMs from Hugging Face.

## 🛠️ Built With

- [Streamlit](https://streamlit.io/): For the web app interface.
- [🤗Hugging Face](https://huggingface.co/): For the AI models.
- **zephyr-7b-beta**: The default LLM model used for chat.
- [Python](https://www.python.org/): The core programming language.
  

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/hugchat-app.git
   cd hugchat-app

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt

3. **Run the app**:
   ```bash
   streamlit run app.py

## 📝 Usage

1. **Launch the app**:
   - Run the app using the following command:
     ```bash
     streamlit run app.py
     ```
   - The app will open in your default web browser.

2. **Interact with the chatbot**:
   - Type your messages in the input box.
   - The AI will respond in real-time, and you can carry on the conversation.

3. **Chat History**:
   - The chat history is automatically saved.
   - You can clear the chat history using the option provided in the sidebar.

## 📂 File Structure

- **app.py**: The main application file.
- **requirements.txt**: Lists all Python dependencies.
- **.env**: Contains environment variables like the Hugging Face API token.
- **chat_history**: Stores chat history using Python's `shelve` module.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## 🧑‍💻 Author

- **Sidhartha Reddy**


