import requests
import sys
import mysql.connector
import json

try:
    mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'quotefetchdb')
except mysql.connector.Error as e:
    sys.exit(e)

mycursor = mydb.cursor()

data = requests.get("https://dummyjson.com/quotes").text

data_info = json.loads(data)

for i in data_info["quotes"]:
    sql = "INSERT INTO `quotes`(`quotes`, `author`) VALUES ('"+i['quote']+"','"+i['author']+"')"
    mycursor.execute(sql)
    mydb.commit()
    print('Inserted !!!')