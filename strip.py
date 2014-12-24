def StripTags (PageContents):
    startLoc = PageContents.find('<div class="entry-content">')
    endLoc = PageContents.find("</div><!-- .entry-content -->")
    PageContents = PageContents[startLoc:endLoc]
    return PageContents
