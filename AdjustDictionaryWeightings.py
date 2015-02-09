## Jocelyn Huang
## 12/12/2013
## Adjust Dictionary Weightings Based on Reviews
import mysql.connector
import math
import string
import RemovePunctuation
import WeightingMethods

needed_used = 'n'
text_list = []
review_rating = 2

connection = mysql.connector.connect(user='dev', password='devpass', database='test')
cursor = connection.cursor()

word_query = "SELECT EXISTS(SELECT %s FROM dictionary WHERE word LIKE %s)"              # To see if a word exists
value_query = "SELECT value FROM dictionary WHERE word LIKE (%s)"                       # Get value of word
review_query = "SELECT review_text FROM reviews WHERE used LIKE %s AND rating LIKE %s ORDER BY RAND() LIMIT 50"  # Retrieve set of reviews
set_used_query = "UPDATE reviews SET used=%s WHERE review_text LIKE %s"                 # Make the reviews used
set_word_value_query = "UPDATE dictionary SET value=%s WHERE word LIKE %s"              # Update value of word

wordsused = {}
notList = ["not", "didnt", "wasnt", "couldnt", "dont", "cant", "wouldnt", "wasnt"]
veryList = ["very", "really", "extremely", "too", "utter", "especially", "so"]
negated = 0
veried = 1  # Goes to 2 for multiplying next value by this amount

# Get reviews
cursor.execute(review_query, ('n', review_rating))
for result in cursor:
    text = result[0]
    text_list.append(text)
# print(len(text_list))    # Just for testing purposes

review_num = 0
# Set used for the reviews of each
for entry in text_list:
    review_num += 1
    print("*****badum new entry*****", review_num)
    cursor.execute(set_used_query, ('t', entry))
    entry = RemovePunctuation.removePunctuation(entry)  # Self-explanatory
    words = [elt for elt in entry.split(' ')]           # Separate the review into component words
    print(entry)
    
    for elt in words:
        if(len(elt) <= 2): continue
        cursor.execute(word_query, (1, elt))
        exists = cursor.fetchall()[0]
        #print(exists==(1,), exists, elt) # Test for working
        
        # Change the value of the word in dictionary
        if(elt in notList):
            print("negation here! --- ", elt)
            negated = 1
            continue
        if(elt in veryList):
            print("veried here! --- ", elt)
            veried = 2
            continue
        
        if(exists == (1,)):
            wordValue = 0
            
            if(elt not in wordsused):             # If this word has not yet been used
                cursor.execute(value_query, (elt, ))
                wordValue = cursor.fetchall()[0][0]
                #print(elt, cursor.fetchall())
            else: wordValue = wordsused[elt]
            
            weight = WeightingMethods.sigmoid(wordValue)
            
            newValue = 0
            if((negated == 0 and review_rating == 2) or (negated == 1 and review_rating > 3)):
                newValue = wordValue - math.ceil(weight/2*veried)
            elif((negated == 0 and review_rating == 4) or (negated == 1 and review_rating < 3)):
                newValue = wordValue + math.ceil(weight/2*veried)
            elif(review_rating == 1):
                newValue = wordValue - weight*veried
            elif(review_rating == 5):
                newValue = wordValue + weight*veried
            
            if(newValue < 0): newValue = 0
            if(newValue > 100): newValue = 100
            
            wordsused[elt] = newValue   # Updates the wordsused for future reference
            
            #print(elt, ": previously", wordValue, "now", newValue)
            cursor.execute(set_word_value_query, (newValue, elt))   #Test this next time, should work.
            
            if(negated == 1):
                negated = 0
                print(elt, wordValue, newValue)
            
            if(veried == 2):
                veried = 1
                print(elt, wordValue, newValue)

print(len(wordsused))
connection.commit()
cursor.close()
connection.close()