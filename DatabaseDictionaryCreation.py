## Jocelyn Huang
## 11/17/2013
## Create Dictionary from Database Reviews
import mysql.connector

#-------<VARIABLES>-----------
num = 0

#-------<Run>-----------------
connection = mysql.connector.connect(user='dev', password='devpass', database='test')
cursor = connection.cursor()

find_review = "SELECT review_text, rating FROM reviews WHERE rating LIKE 2 OR rating LIKE 1"
cursor.execute(find_review)

for (review_text, rating) in cursor:
    num += 1
    print(rating, " : ", review_text)

print(num)
cursor.close()
connection.close()