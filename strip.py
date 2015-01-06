def StripTags (PageContents):
    startLoc = PageContents.find('<body>')
    endLoc = PageContents.find("</body>")
   #PageContents = PageContents[startLoc:endLoc]
   # return PageContents

    inside = 0
    text = ""

    for char in PageContents:
        if char == "<":
            inside = 1
        elif (inside ==1 and char == ">"):
            inside = 0
        elif inside == 1:
            continue
        else:
            text += char
    return text    

def stripNonAlphaNum(text):
    import re
    return re.compile(r"\W+",re.UNICODE).split(text)
