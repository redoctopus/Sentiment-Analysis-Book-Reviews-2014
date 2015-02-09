## Jocelyn Huang
## 10/03/2013
## Main
import MergeWithDictionary
import ExtractText_v2
import TakeReview
#
import mysql.connector

# Grab test reviews
reviews = ExtractText_v2.extract()
text = {}
rating = {}
count = 0
#mergeResults = MergeWithDictionary.mergeWithDictionary()
#dictionary = mergeResults[0]
#set_aside = mergeResults[1]
connection = mysql.connector.connect(user='dev', password='devpass', database='test')
cursor = connection.cursor()

'''for review in reviews:
    text[count] = review
    rating[count] = reviews[review]
    count += 1

for n in range(count):
    print(rating[n], text[n])'''
for review in reviews:
    add_review = "INSERT INTO reviews (rating, review_text) VALUES (%s, %s)"
    cursor.execute(add_review, (reviews[review], review))

connection.commit()
cursor.close()
connection.close()

# Input review
#review = input("Enter your review here: ")
#rating = TakeReview.getRating(review, dictionary)

"""for elt in dictionary:
    if dictionary[elt] < 40 or dictionary[elt] > 60: print(elt, dictionary[elt])"""