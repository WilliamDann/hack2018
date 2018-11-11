# General media object
class MediaObject:
    def __init__(self, title, image, link, content=""):
        self.title = title
        self.image = image
        self.link = link
        self.content = content