from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI

db = SQLDatabase.from_uri("sqlite:///Chinook.db")
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
db = SQLDatabase.from_uri("sqlite:///Chinook.db", include_tables=["Album", "Employee"])


chain = create_sql_query_chain(llm, db)

# print(table_info)
response = chain.invoke(
    {
        "question": "Can you pull up our canadian staff?",
    }
)
print(response)
print(db.run(response))
