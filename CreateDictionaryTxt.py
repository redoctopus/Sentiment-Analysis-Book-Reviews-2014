## Jocelyn Huang
## 03/13/2014
## Use Tables to Create Dictionary .txt File
import mysql.connector
import string

filename = "TestDictionary6.txt"
fp = open(filename, "w")

connection = mysql.connector.connect(user='dev', password='devpass', database='test')
cursor = connection.cursor()

query = "SELECT word, value FROM dictionary WHERE value != 50"
cursor.execute(query)
line = ""

for (word, value) in cursor:
    line = word + " "
    if(value >= 10 and value < 100): line += "0"
    elif(value < 10): line += "00"
    line += str(value) + "\n"
    #print(line + "**")
    fp.write(line)

fp.close()
cursor.close()
connection.close()