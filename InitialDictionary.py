## Jocelyn Huang
## 12/05/2013
## Load English Dictionary Words Into Database
import mysql.connector
import string

defaultValue = 50
three_letter_words = ['top', 'add', 'who', 'hit', 'all', 'tad', 'why', 'fan', 'art', 'out', 'new', 'old', 'let', 'put', 'mad', 'odd',"bad"]

filename= 'dictionary.txt'
fp = open(filename, 'r')

connection = mysql.connector.connect(user='dev', password='devpass', database='test')
cursor = connection.cursor()

lines = fp.readlines()
for i in range(len(lines)):
    if('\n' in lines[i]):
        word = lines[i][:(lines[i].index('\n'))]
        if len(word) <= 3 and word not in three_letter_words:
            continue
        
        insert_statement = "INSERT INTO dictionary (word, value) VALUES (%s, %s)"
        cursor.execute(insert_statement, (word, defaultValue))

connection.commit()
cursor.close()
connection.close()