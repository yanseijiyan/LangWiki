# import the necessary libraries
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from dotenv import load_dotenv, find_dotenv

# Load the environment variables
load_dotenv(find_dotenv())

# Configures the LLM agent with a specific model and temperature for text generation
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

 
def setup_agent():
  # Define the search tool with the maximum number of results
  api_wrapper = WikipediaAPIWrapper(top_k_results=3, doc_content_chars_max=100)
  tool = WikipediaQueryRun(api_wrapper=api_wrapper)
  tools = [tool]
  # Retrieves the specific agent prompt from the LangChain hub
  prompt = hub.pull("hwchase17/react") 
  # Create the agent with the OpenAI functions, the LLM model and the defined tools
  agent = create_react_agent(llm, tools, prompt)
  # Returns the agent's executor, allowing the execution of verbose actions for debugging
  return AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)


def search_wikipedia(executor, query):
    # search Wikipedia for the query
    result = executor.invoke({"input": query})
    return result.get('output', "Error searching Wikipedia.")

def summarize_text(text):
    # summarize the text of the Wikipedia article
    result = executor.invoke({"input": f"Summarize the following text:\n{text}"})
    return result.get('output', "Failed to summarize text.")

def generate_response_with_langchain(question, context):
    # Matches question with context for model input
    response = executor.invoke({"input": f"Based on the following context:{context}\n\nQuestion: {question}\nResponse:"})
    return response.get('output', "Failed to generate response.")

# Create the agent executor
executor = setup_agent()