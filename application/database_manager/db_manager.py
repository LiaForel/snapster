import mysql.connector

cnx = mysql.connector.connect(user='root', password='apples',
                              host='127.0.0.1',
                              database='snapster')
cnx.close()