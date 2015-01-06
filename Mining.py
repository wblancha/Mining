import count
import urllib2
import strip
#url = "http://www.gutenberg.org/files/35/35.txt"
url = raw_input("Please enter a valid url to mine from\n")
response = urllib2.urlopen(url)
webContent = response.read()

text = strip.StripTags(webContent).lower()
final = strip.stripNonAlphaNum(text)
#print text
#print final
#file = open("refined.txt","w")
#file.write(str(final))
#file.close()
#for word in final:
 #   file = open("week-1-readings.txt","a")
  #  file.write("\n" + word)
   # file.close()
counted = count.counting(final)

print counted
