# LangChain_Demo_With_Gemma_Model

This repository contains a LangChain-based chatbot application that uses the Ollama model to answer user queries. The application is built with LangChain and Streamlit for a simple, interactive interface.

## Features

- **LangChain Integration**: The app uses LangChain to process natural language queries and generate responses.
- **Ollama Model**: The chatbot utilizes the `gemma:latest` model from Ollama for generating responses.
- **Streamlit Interface**: A simple web interface built with Streamlit allows users to interact with the chatbot.

## Requirements

Before running the application, make sure to install the necessary dependencies:

~~~bash
pip install -r requirements.txt
~~~
Dependencies:

* LangChain

* Streamlit

* dotenv

* Ollama Client

Setup:

1.  Clone the repository:
   ~~~
      git clone https://github.com/yourusername/your-repository.git
   ~~~
2. Create a .env file in the root of the project and add your LangChain API key and project details:
   ~~~
   LANGCHAIN_API_KEY=your-api-key
   LANGCHAIN_PROJECT=your-project-id
   ~~~
3. Install the required dependencies:
   ~~~
   pip install -r requirements.txt
   ~~~
4. Run the Streamlit app:
   ~~~
   streamlit run app.py
   ~~~

The app will be available at http://localhost:8501 in your browser.

# Deployment

If you want to deploy this app using Streamlit sharing or any cloud platform, follow these steps:

# Streamlit Sharing:

Push your code to GitHub.

Sign in to Streamlit Sharing.

Connect your GitHub repository and deploy the app.

# Other Deployment Platforms:

You can also deploy the app on other platforms like Heroku, AWS, or Google Cloud by following their respective deployment guides.

Make sure to configure the environment variables for the API keys and project details.

Usage:

Once the app is running, you can enter any question in the input box, and the chatbot will generate a response using the Ollama model.

# Example:


Question: "What is Generative AI?"

Response: The chatbot will provide a brief explanation of Generative AI.

# License:

This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments

LangChain for providing the framework to interact with language models.

Ollama for providing the powerful models used in this application.

Streamlit for providing an easy-to-use platform for building interactive web apps

# APP PREVIEW
Visit this Website to check out my Application: 
