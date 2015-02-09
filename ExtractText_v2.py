# Jocelyn Huang
# 10/01/2013
# Text Extraction 

from bs4 import BeautifulSoup
import urllib.request
#import urllib.response
import re
import random
from random import randint
import time

def extract():
    #-----<Variables>-----
    book = 12067#930      #Goodreads book ID
    #book = randint(900, 30000)
    allReviews = {}
    extraReviews = {}
    starDict = {1:0, 2:0, 3:0, 4:0, 5:0}
    
    #-----<Looping through books>-----
    for k in range(1):
        # Open page
        url_book = "http://www.goodreads.com/book/show/"+str(book)+"?page=1+&text_only=true"
        print(url_book)
        page = urllib.request.urlopen(url_book)
        soup = BeautifulSoup(page.read())
        
        print(soup.find('title'))
      # Find range of pages with text reviews
        reviews = soup.find (id = 'reviews')
        if reviews is None:     # Check for nonexistent book
             print("hello, there is no book here")
             continue
        
        scope = reviews.find ('div').find ('span')
        
        pageRange = re.compile('.+\(showing (\d+)-(\d+) of ([\d,]+)\).+') #Such as (1-30 of 222)
        span = str(scope).replace("\n", " ")
        m = pageRange.match (span)
        ranges = m.groups()
        start, end, total_pages = ranges            # start == first review no. on the page
        total_pages = total_pages.replace(",", "")  # end == last review no. on the page
                                                    # total_pages == total no. of reviews
        
        for pageNum in range (1, 2):#int(end)-15):#---------------------------_++++++++++************************* FIXXXXXX
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
                if "...more" in reviewText:
                    reviewText = reviewText[reviewText.find("...more")+8 : len(reviewText)-7]
                starNumber = int(stars.text[0])
                
                starDict[starNumber] += 1 # Should add to starDict
                
                #-----------<Sort through reviews to put them in list>-----------------
                if starNumber in [1,2,5]: allReviews[reviewText] = starNumber
                
                else: extraReviews[reviewText] = starNumber # Keeping 3- and 4- star reviews for reference
                
            #-------------------<Pause>------------------------------
            sleepNumber = random.uniform(5,12)              # Made separate for reference
            time.sleep(sleepNumber)
        book += 50
        time.sleep(10)
    
    print("One: ", starDict[1], "\tTwo: ", starDict[2], "\tFive: ", starDict[5])
    return allReviews