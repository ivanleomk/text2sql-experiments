from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
db = SQLDatabase.from_uri("sqlite:///Chinook.db")

agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)


agent_executor.invoke(
    {
        "input": "Help me determine what are the best selling clothes in the market this year?"
    }
)
