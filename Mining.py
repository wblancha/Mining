import urllib2
import strip
url = "https://www.electricarchaeology.ca"

response = urllib2.urlopen(url)
webContent = response.read()

text = strip.StripTags(webContent)
print text
