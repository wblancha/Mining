#Stopwords.py
#tester = ["name", "date", "distance", "and", "or", "the"]
def stop(words):
    filtered = []
    source = open("stopwords.txt")
    stopwords = source.read()
    for word in words:
        if word not in stopwords:
            filtered.append(word)
        else:
            print "Not in list"
    return filtered
    source.close()
#test = stop(tester)
