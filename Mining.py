import stopwords
import count
import urllib2
import strip
#following function opens the url, reads it, and calls the strip module to remove html tags, punctuation.  
#It also calls the count module to count the frequency of of the remaining words
def mine(content):
    response = urllib2.urlopen(content)
    webContent = response.read()

    text = strip.StripTags(webContent).lower()
    final = strip.stripNonAlphaNum(text)
    finale = stopwords.stop(final)  
    counted = count.counting(finale)

#address = raw_input("Please enter a valid url to mine from\n")
#mine(address)
