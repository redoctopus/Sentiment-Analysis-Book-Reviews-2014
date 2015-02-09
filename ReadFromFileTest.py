## Jocelyn Huang
## Sentiment Analysis Project
## 02.06.2014
## Read from text file
import string
import sys

def removePunctuation(s):
   s = s.replace("-", " ")
   s = s.replace(".", " ")
   s = s.replace("/", " ")
   removal = {ord(char): None for char in string.punctuation}
   s = s.translate(removal).lower()
   return s

#*******************************************************
overall_rating = 0
negated = 0
veried = 0
length = 0

three_letter_words = ['top', 'add', 'who', 'hit', 'all', 'tad', 'why', 'fan', 'art', 'out', 'new', 'old', 'let', 'put', 'mad', 'odd',"bad", "not"] # To keep
notList = ["not", "didnt", "couldnt", "dont", "cant", "wouldnt", "wasnt"]
veryList = ["very", "really", "extremely", "too", "utter", "especially", "so"]

review = sys.argv[1]		# Take input string review
#review = removePunctuation(review)
#print("After punctuation removed", review)
#print(review)
f = open('TestDictionary6.txt', "r")	# The dictionary text file

entries = [entry for entry in f.read().split('\n')]
entries.pop() 			# Gets rid of '' entry
#print(entries)
#dictionary = {entry[0:len(entry)-3]: int(entry[len(entry)-2:]) for entry in entries}
dictionary = {entry[0:len(entry)-4]: int(entry[len(entry)-3:]) for entry in entries} # Form {"word": int}
#print(dictionary)

review_words = [elt for elt in review.split(' ')]
#print("review words: ", review_words)
length = len(review_words)

#=================================================================================
# Removes unneeded words (though not ones like "book", "this"-- the special cases)
#
#Where words in the review are actually checked
for elt in review_words:
   # Special cases
   if(elt in notList):
      length -= 1
      negated = 1
      #overall_rating += 50
      continue
   if(elt in veryList):
      length -= 1
      veried += 1
      #overall_rating += 50
      continue
    
   # Check for excluded
   if(elt not in dictionary):
      length -= 1
      ######print("---There is no ", elt)
      continue
   
   addition = dictionary[elt]
   
   if(veried != 0 and negated == 1):
      if(dictionary[elt] > 50): addition = 100-(addition*0.8)
      else: addition = 100-addition*1.5
      veried = 0
      negated = 0

   elif(veried != 0):
      if(dictionary[elt] >= 50): addition = addition*(1.5**veried)
      else: addition = addition*(0.5**veried)
      veried = 0

   elif(negated == 1):
      addition = 100-addition
      negated = 0

   #######print(elt, addition)
   # Adjust to fit bounds (primative)
   if(addition < 0): addition = 0
   if(addition > 100): addition = 100
   
   overall_rating += addition

#######print("Overall rating is: ", overall_rating, "length is ", length)
if(length == 0):
   print("No usable words, sorry.")
   overall_rating = 50
else:
   overall_rating = overall_rating/(length)
#print(review_words)
print("******************")
#print(overall_rating)
print("{0:3.1f}".format(overall_rating))
if(overall_rating > 80): print("That's extremely positive :D")
elif(overall_rating > 55): print("That's positive. :)")
elif(overall_rating < 20): print("That's extremely negative :'(")
elif(overall_rating < 45): print("That's negative. :(")
else: print("Neutral :I")
#
print("******************")
