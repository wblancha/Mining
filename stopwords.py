#Stopwords.py
tester = ["name", "date", "distance", "and", "or", "the"]
def stop(words):
    stopwords =["and", "or", "a", "the", "then"]
    for word in stopwords:
        if word in words:
            words.remove(word)
        else:
            print "Not in list"
test = stop(tester)
print tester
