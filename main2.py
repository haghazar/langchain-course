from typing import List

from pydantic import BaseModel, Field 

from dotenv import load_dotenv

load_dotenv()


from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
#from tavily import TavilyClient
from langchain_tavily import TavilySearch 


class Source(BaseModel):
    """Schema for a source used by the agent"""
    
    url: str = Field(description="The URL of the source")
class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""
    
    answer: str = Field(description="The agent's answer to the user's query")
    sources: List[Source] = Field(default_factory=list, description="List of sources used by the agent to generate the answer")

#tavily = TavilyClient() 

#@tool
#def search(query: str) -> str:
#    """Search for weather information by city name."""
#    print(f"Searching for: {query}")
#    return tavily.search(query=query)



#llm = ChatOpenAI(model="gpt-5.5", temperature=0)
llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=0)
#tools = [search]

tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)



def main():
    print("Hello from langchain-course!")
    #result = agent.invoke({"messages": HumanMessage(content="What is the weather in Tokyo?")})
    result = agent.invoke({"messages": HumanMessage(content="search for 3 job postings for an ai engineer using langchain in Yerevan, Armenia on linkedin and list their details")})
    print(result)

if __name__ == "__main__":
    main()