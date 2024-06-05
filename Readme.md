# Introduction

This is a repository that shows the usage of a few different libraries that people are using to perform text 2 sql.

We can use the `chinook.db` file which is a simple sqlite database to play with langchin's agent, chain as well as llama index itself.

To see information on the chinook dataset, see this [link](https://database.guide/2-sample-databases-sqlite/)

## Running the code

To run the code

1. Install requirements.txt in a virtual environment

```
pip3 install -r requirements.txt
```

2. Run the scripts

- `langchain_agent.py` : This runs the agent equivalent of a sql query
- `langchain_chain.py` : This uses a chain to execute queries against the chinookdb
- `llama_index_query` : This uses llama-index to run queries against the chinook.db file
