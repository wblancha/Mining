#Stopwords.py
#tester = ["name", "date", "distance", "and", "or", "the"]
def stop(words):
    filtered = []
    stopwords =["and", "or", "a", "the", "then"]
    for word in words:
        if word not in stopwords:
            filtered.append(word)
        else:
            print "Not in list"
    return filtered
#test = stop(tester)

