class ItemData:
    def __init__(self, type1, title, price, link):
        self.type1 = type1
        self.title = title
        #self.spec = spec
        self.price = price
        self.link = link

    @property
    def getType(self):
        return self.type1

    @property
    def getTitle(self):
        return self.title
    
    @property
    def getSpec(self):
        return self.spec

    @property
    def getPrice(self):
        return self.price
    
    @property
    def getLink(self):
        return self.link
    
    @property
    def setType(self, text):
        self.type1 = text
    
    @property
    def setTitle(self, text):
        self.title = text

    @property
    def setSpec(self, text):
        self.spec = text

    @property
    def setPrice(self, text):
        self.price = text
    
    @property
    def setLink(self, text):
        self.link = text