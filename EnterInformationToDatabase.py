## Jocelyn Huang
## 11/21/2013
## Enter Review Info Into Database
from bs4 import BeautifulSoup
import urllib.request
import re
import random
from random import randint
import time
import mysql.connector

#-----<Variables>-----
#Goodreads book ID
book = randint(1, 13138635) # Try 10462129
connection = mysql.connector.connect(user='dev', password='devpass', database='test')
cursor = connection.cursor()
#
allReviews = {}
starDict = {1:0, 2:0, 3:0, 4:0, 5:0}

#-----<Looping through books>-----
for k in range(5):
    # Open page
    url_book = "http://www.goodreads.com/book/show/"+str(book)+"?page=1+&text_only=true"
    print(url_book)
    page = urllib.request.urlopen(url_book)
    soup = BeautifulSoup(page.read())
        
    # Find range of pages with text reviews
    reviews = soup.find (id = 'reviews')
    # Check for nonexistent books
    if reviews is None:
        print("hello, there is no book here")
        book = randint(900, 13138635)
        continue
    
    info = str(soup.find('title'))
    info = info[7:len(info)-48] # Takes out "reviews and discussions..."
    print(info)
    
    scope = reviews.find ('div').find ('span')
    
    pageRange = re.compile('.+\(showing (\d+)-(\d+) of ([\d,]+)\).+') #Such as (1-30 of 222)
    span = str(scope).replace("\n", " ")
    m = pageRange.match (span)
    ranges = m.groups()
    start, end, total_reviews = ranges            # start == first review no. on the page
    total_reviews = total_reviews.replace(",", "")  # end == last review no. on the page
                                                # total_reviews == total no. of reviews
    if(int(total_reviews) == 0):
        print("No reviews")
        time.sleep(randint(3,7))
        book = randint(1, 13138635)
        continue
    
    print(end, total_reviews, int(total_reviews)//int(end)) ####EDIT RANGE
    
    for pageNum in range (1, int(total_reviews)//int(end)+1):#int(end)):
        url_book = "http://www.goodreads.com/book/show/"+str(book)+"?page="+str(pageNum)+"+&text_only=true"
        print(pageNum, "*********************")
        page = urllib.request.urlopen(url_book)
        soup = BeautifulSoup(page.read())
        
        bookReviews = soup.find (id = "bookReviews")
        reviewSets = bookReviews.findAll("div", {"class" : "section"})
        
        for r in reviewSets:
            review = r.find("span", {"style" : "display:none"})
            stars = r.find("a", {"class" : "staticStars"})
            if stars == None or review == None: continue
            
            reviewText = review.text
            #print(reviewText) # Take out later
            if "...more" in reviewText:
                reviewText = reviewText[reviewText.find("...more")+8 : len(reviewText)-7]
            starNumber = int(stars.text[0])
            
            #-------------<Quick Check for English>--------------
            if(" the " not in reviewText):
                continue
            starDict[starNumber] += 1 # Should add to starDict
            
            
            #-----------<Put reviews in database>-----------------
            insert_review = "INSERT INTO reviews (rating, review_text, book, used) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_review, (starNumber, reviewText, info, 'n'))
                        
        #-------------------<Pause>------------------------------
        sleepNumber = random.uniform(5,9)              # Made separate for reference
        time.sleep(sleepNumber)
    #book += 50
    book = randint(1, 13138635)
    time.sleep(4)

print("One: ", starDict[1], "\tTwo: ", starDict[2], "\tFive: ", starDict[5])

connection.commit()
cursor.close()
connection.close()