from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    String,
    Integer,
    select,
    column,
)
from llama_index.core.query_engine import NLSQLTableQueryEngine
from llama_index.core import SQLDatabase
from sqlalchemy import insert

engine = create_engine("sqlite:///Chinook.db")

sql_database = SQLDatabase(engine)
query_engine = NLSQLTableQueryEngine(
    sql_database=sql_database,
    # tables=["city_stats"],
)
query_str = "How many clothes did we sell in Vivocity last year?"
response = query_engine.query(query_str)
print(response)
