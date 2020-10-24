#!/usr/bin/env python
#Lembrar de no Python3
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import random
import string

def insertIntoTables(senha):
    try:
        connection = mysql.connector.connect(host='localhost',
					     database='alfa',
					     user='root',
					     password='h0w4rd')
        cursor = connection.cursor()
        mysql_insert_query = """INSERT INTO identificacao(DSCSENHA)
                                                   VALUES(%s)"""

        recordTuple = (senha,) #Para criar uma tupla com único elemento, colocar vírgula
        cursor.execute(mysql_insert_query, recordTuple)
        connection.commit()
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def randomString(stringLength=10):
    """Generate a random string of fixed length"""
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for i in range(stringLength))


for i in range(10):
    insertIntoTables(randomString())


