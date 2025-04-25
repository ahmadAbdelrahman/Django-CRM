import mysql.connector


database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'helloAhmed76152'

)

curserObject = database.cursor()

curserObject.execute('CREATE DATABASE crmdatabase')

print('All Done!')