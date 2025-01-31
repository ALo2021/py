import mysql.connector

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",      # Change if MySQL is on another server
    user="root",           # Your phpMyAdmin MySQL username
    password="",           # Your phpMyAdmin MySQL password
    database="testdb",     # Change to your actual database name
    port=3306              # Default MySQL port
)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Example: Fetch data from a table named 'users'
cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()

# Display the results
for row in rows:
    print(row)

# Close the connection
cursor.close()
db.close()