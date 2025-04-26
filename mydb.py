import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


# database = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     passwd = 'helloAhmed76152'

# )

print ('HOSt IS: ', os.environ.get('HOST'))
print ('HOSt2 IS: ', os.getenv('HOST'))

database = mysql.connector.connect(
    host = os.getenv('HOST'),
    user =  os.getenv('USER'),
    passwd = os.getenv('PASSWORD'),

)

curserObject = database.cursor()

curserObject.execute('CREATE DATABASE crmdatabase')

print('All Done!')