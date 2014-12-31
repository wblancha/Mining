import count
import urllib2
import strip
url = "http://www.gutenberg.org/files/35/35.txt"

response = urllib2.urlopen(url)
webContent = response.read()

text = strip.StripTags(webContent).lower()
final = strip.stripNonAlphaNum(text)
#print text
#print final
file = open("refined.txt","w")
file.write(str(final))
file.close()
for word in final:
    file = open("fine.txt","a")
    file.write("\n" + word)
    file.close()
counted = count.counting(final)

print counted
