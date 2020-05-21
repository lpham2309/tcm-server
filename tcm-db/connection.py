import mysql.connector

config = {
    'user': 'root',
    'password': 'password',
    'host': 'db',
    'port': '3306',
    'database': 'items'
}


connection = mysql.connector.connect(**config)
cursor = connection.cursor()
cursor.execute('SELECT * FROM favorite_colors')
results = [{name: color} for (name, color) in cursor]
cursor.close()
connection.close()