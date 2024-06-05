import sqlite3
import os

# Delete the existing database if it exists
if os.path.exists('chinook.db'):
    os.remove('chinook.db')

# Create the database
conn = sqlite3.connect('chinook.db')
print("Database created successfully")

# Get the path to the SQL script
script_dir = os.path.dirname(os.path.abspath(__file__))
sql_file = os.path.join(script_dir, 'Chinook_Sqlite.sql')

# Open and read the SQL script
with open(sql_file, 'r') as f:
    script = f.read()

# Execute the SQL script
conn.executescript(script)
print("Database populated successfully")

# Verify the database
cursor = conn.cursor()
cursor.execute("SELECT * FROM Artist LIMIT 10;")
results = cursor.fetchall()
for row in results:
    print(row)

# Close the connection
conn.close()

