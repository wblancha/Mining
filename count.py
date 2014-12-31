import operator
def counting (word):
    word_count = {}
    for item in word:
        count = 1
        item.lower()
        if item in word_count:
            count = word_count[item]
            count +=1
            word_count[item] = count
        else:
            word_count[item] = 1
    for item,count in word_count.iteritems():
        print item + ": " + str(count)  
    sorted_x = sorted(word_count.items(), key=operator.itemgetter(1))
    for i in sorted_x:
        print i
    file = open("sorted.txt", "w")
    file.write(str(sorted_x))
    file.close
#Below is testing code
#list = ["hello", "goodbye", "Peanut", "hello", "cookie", "Peanut"]

#print counting(list)
