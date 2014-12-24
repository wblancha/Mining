import urllib2
import strip
url = "https://www.electricarchaeology.ca"

response = urllib2.urlopen(url)
webContent = response.read()

page = open("ore.txt", "w")
page.write(webContent)
page.close()

refined = strip.StripTags("ore.txt")
page2 = open("refined.txt", "w")
page2.write(refined)
page.close()
#print refined
