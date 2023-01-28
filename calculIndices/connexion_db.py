import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
def conn(host="localhost",user="root",password="20171987"):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )

        db = conn.cursor()
        myDataBase = "mydatabas"
        db.execute("SHOW DATABASES")
        lst = db.fetchall()
        if (myDataBase,) not in lst:
            db.execute(f"CREATE DATABASE {myDataBase}")
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")