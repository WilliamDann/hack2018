from html.parser import HTMLParser
import urllib.request

class NewsHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.description = ''
        self.image_url = ''
        self.title = ''

    def handle_starttag(self, tag, attrs):
        #print("Encountered a start tag:", tag)
        if tag == 'meta':
            desc = ''
            img = ''
            title = ''
            imggood = False
            descgood = False
            titlegood = False
            for attr, data in attrs:
                if (attr == 'property' or attr == 'name') and 'description' in data:
                    descgood = True
                elif attr == 'content':
                    desc = data
                if (attr == 'property' or attr == 'name') and 'image' in data:
                    imggood = True
                elif attr == 'content':
                    img = data
                if (attr == 'property' or attr == 'name') and 'title' in data:
                    titlegood = True
                elif attr == 'content':
                    title = data
            if descgood and desc != '':
                if (len(desc) > len(self.description)):
                    self.description = desc
            if imggood and img != '':
                if (len(img) > len(self.image_url)):
                    self.image_url = img
            if titlegood and title != '':
                if (len(title) > len(self.title)):
                    self.title = title

    def handle_endtag(self, tag):
        pass
        #print("Encountered an end tag :", tag)

    def handle_data(self, data):
        pass
        #print("Encountered some data  :", data)

class NewsParser:
    def parseArticle(url):
        try:
            f = urllib.request.urlopen(url)
            parser = NewsHTMLParser()
            parser.feed(f.read().decode())
            print(parser.description, parser.image_url, parser.title)
            return (parser.description, parser.image_url, parser.title)
        except:
            return ('','')