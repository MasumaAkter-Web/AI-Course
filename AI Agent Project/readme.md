# Research Agent Using LangChain & Groq LLM

## Project Overview

This project is a **Research Agent** built using **LangChain**, **Groq LLM**, and Python. It is designed to gather, analyze, and summarize information from online sources in a structured and detailed way. The agent can:

- Understand a user query.
- Fetch relevant data from **Wikipedia** and simulated **web search** results.
- Summarize the topic with background information, key concepts, examples, facts, statistics, and modern relevance.
- Return a **structured JSON output** following a defined Pydantic schema.
- Save the output to a local file for reference.

**Technologies Used:**

- Python 3.13+
- [LangChain](https://www.langchain.com/)  
- [LangChain-Groq](https://github.com/groq-ai/langchain-groq)
- Pydantic (for structured output)
- Wikipedia REST API
- dotenv (for environment variables)

## Features

1. **Query Understanding:** Reads and interprets the user’s query intelligently.
2. **Tool Integration:**
   - Wikipedia Summary
   - Simulated Web Search
3. **Structured Output:** Produces a JSON object containing:
   - `topic`
   - `summary`
   - `sources`
   - `tools_used`
4. **File Saving:** Saves the research summary to `researchoutput.txt`.
5. **Graph-based Workflow:** Uses a state graph to handle query processing and LLM reasoning.

## How to run:

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
2.Create a virtual environment and activate it:

python -m venv myenv
# Windows
myenv\Scripts\activate
# Linux/macOS
source myenv/bin/activate


3.Install the required packages:

pip install -r requirements.txt

4.Set Up API Keys:

Your agent may need API keys for external services like Groq LLM or a real search engine.

a.Groq LLM API Key:

Sign up for a Groq account: https://www.groq.ai

Generate an API key in your account dashboard.

b.Google Search API:

Sign up for a Google Cloud account: https://cloud.google.com/

Enable the Custom Search API and generate an API key.

Replace the search_tool in tools.py with real API calls.

c.Store API Keys in .env file:

4.Create a .env file if you need to store API keys or environment variables:

touch .env

## Usage:

1.Run the main script:


python main.py


2.Input your query when prompted:


What can I help you research? Computer


3.The agent will:
Retrieve data from Wikipedia and simulated web search.

Generate a structured research summary.

Print the final JSON output in the terminal.

Save it to researchoutput.txt


## Output:

PS C:\Users\Mr Aqeel SB\OneDrive\Desktop\AI_Lab_Agent> & "C:/Users/Mr Aqeel SB/OneDrive/Desktop/AI_Lab_Agent/myenv/Scripts/Activate.ps1"
(myenv) PS C:\Users\Mr Aqeel SB\OneDrive\Desktop\AI_Lab_Agent> python Main.py
What can I help you research? Computer

✔ FINAL STRUCTURED OUTPUT:
 topic='Computer' summary='A computer is an electronic device that can store, process, and communicate information. It consists of hardware and software components, including a central processing unit (CPU), memory, input/output devices, and operating system. Computers have revolutionized the way people live, work, and communicate, with applications in various fields such as education, healthcare, finance, and entertainment. The history of computers dates back to the early 19th century, with the development of mechanical computers, followed by the invention of electronic computers in the mid-20th century. Today, computers are an essential part of modern life, with advancements in technology leading to the development of smaller, faster, and more powerful devices.' sources=['https://www.britannica.com/technology/computer', 'https://en.wikipedia.org/wiki/Computer'] tools_used=['Search Engine', 'Wikipedia API']

✅ Research output saved to researchoutput.txt
(myenv) PS C:\Users\Mr Aqeel SB\OneDrive\Desktop\AI_Lab_Agent>

<img width="1035" height="326" alt="Screenshot" src="https://github.com/user-attachments/assets/43afc24c-387f-4aa6-b464-902f0bfd7e19" />


