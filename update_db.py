import sqlite3

# Connect to the database
connection = sqlite3.connect('engagement_data.db')

# Create a cursor object
cursor = connection.cursor()

# Alter the table to add the sentiment column
cursor.execute("ALTER TABLE engagement ADD COLUMN sentiment TEXT;")

# Commit the changes and close the connection
connection.commit()
connection.close()

print("Column 'sentiment' added to 'engagement' table.")
