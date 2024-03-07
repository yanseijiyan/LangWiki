
# LangWiki: The Langchain Streamlit Interactive Chat

## Description

Dive into the depths of human knowledge with LangWiki, your personal guide to the vast ocean of information that is Wikipedia. This isn't just any chat application; it's a doorway to exploring the unknown, understanding complex topics, and satisfying your curiosity with summaries and in-depth discussions, all powered by cutting-edge artificial intelligence through LangChain.

LangWiki stands out by blending the immediacy of interactive chat with the depth of encyclopedic knowledge, making learning an engaging, conversational experience. Whether you're a trivia enthusiast, a student seeking clarity, or just curious about the world, LangWiki offers a unique way to interact with information, transforming the way we learn and explore.

## Environment Setup

Before embarking on your journey with LangWiki, ensure your environment is ready by following these setup steps:

### 1. Virtual Environment Setup (Optional)

For an isolated and clean working environment, setting up a virtual environment is recommended. Execute the following commands based on your operating system:

```bash
# For Unix/MacOS-based systems
python3 -m venv venv
source venv/bin/activate
```
```bash
# For Windows systems
python -m venv venv
.\venv\Scripts\activate
```
2. Installing Dependencies
WikiWit relies on several key libraries to connect you with the wisdom of Wikipedia and the power of LangChain's AI. Install these dependencies using pip:

```bash
pip install -r requirements.txt
```
## Configuring Environment Variables

For secure and efficient configuration, WikiWit utilizes environment variables to manage sensitive information such as API keys. Follow these steps to set up your environment variables:

### 1. Creating the `.env` File

In the root directory of your project, create a file named `.env`. This file will store your environment variables. Ensure that `.env` is listed in your `.gitignore` file to prevent sharing sensitive information on version control systems.

### 2. Adding Variables to the `.env` File

Open your `.env` file in a text editor and add your environment variables in the format `VARIABLE_NAME=value`. For example, if your project requires an OpenAI API key, you might add the following line:

```plaintext
OPENAI_API_KEY=your_api_key_here
```

## Running the Application
With your scholarly toolkit installed, you're ready to launch WikiWit and begin your adventure in knowledge exploration:

```bash
streamlit run app.py
```
Ensure app.py matches the name of your Streamlit script file, adjusting as necessary.

## Features
- Wikipedia Search: Embark on quests for knowledge by entering topics of interest.
- Content Summarization: Receive distilled wisdom in the form of concise summaries.
- Interactive Chat: Engage in enlightening conversations about your discoveries.
- Search Restart: Venture anew with the option to explore different topics anytime.

 
## Contribution
Join the quest to make knowledge exploration more interactive and engaging! Contributions are warmly welcomed. Please follow the standard GitHub practices for contributions via pull requests.







