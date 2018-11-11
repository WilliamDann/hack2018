from html.parser import HTMLParser
import urllib.request

class NewsHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.description = ''

    def handle_starttag(self, tag, attrs):
        #print("Encountered a start tag:", tag)
        if tag == 'meta':
            content = ''
            isgood = False
            for attr, data in attrs:
                if (attr == 'property' or attr == 'name') and 'description' in data:
                    isgood = True
                elif attr == 'content':
                    content = data
            if isgood and content != '':
                if (len(content) > len(self.description)):
                    self.description = content

    def handle_endtag(self, tag):
        pass
        #print("Encountered an end tag :", tag)

    def handle_data(self, data):
        pass
        #print("Encountered some data  :", data)


def parseArticle(url):
    f = urllib.request.urlopen(url)
    parser = NewsHTMLParser()
    parser.feed(f.read().decode())
    return parser.description