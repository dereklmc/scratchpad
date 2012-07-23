class Format(object):
    def __init__(self, name, stock):
        self.name = name
        self.owned = stock
        self.stock = stock
    
    @property
    def stock():
        def fget(self):
            return self.__stock
        def fset(self,num):
            if not ( 0 < num+stock < self.owned):
                raise ValueError()
            self.__stock += num
    
    @property
    def borrowed(self):
        return self.owned - self.stock      

class Movie(object):
    
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year
    
    def __str__(self):
        return self.title + " " + self.director + " " + self.year
    
    @classmethod
    def build(cls, input):
        inData = input.split(", ")
        return cls(input[0], input[1], int(input[2])

class Classic(Movie):
    
    def __init__(self, title, director, actor, month, year):
        super(Movie, self).__init__(title, director, year)
        self.actor = actors
        self.month = month

    def __cmp__(self, other):
        comparison = self.year - other.year
        if comparison is 0:
            comparison = self.month - other.month
        if comparison is 0:
            comparison = cmp(self.actor, other.actor)
        return comparison
    
    @classmethod
    def build(cls, input):
        inData = input.split(", ")
        adData = inData[2].split(" ")
        actor = " ".join(adData[0:1])
        return cls(input[0], input[1], actor, adData[2], adData[3])

class Drama(Movie):
    
    def __cmp__(self, other):
        comparison = cmp(self.director, other.director)
        if comparison is 0:
            comparison = cmp(self.title, other.title)
        return comparison

class Comedy(Movie):
    
    def __cmp__(self, other):
        comparison = cmp(self.title, other.title)
        if comparison is 0:
            comparison = cmp(self.year, other.year)
        return comparison

class StockedMovie(object):
    
    def __init__(self, item, formats = {"D": Format("DVD", 10)} ):
        self.item = item
        self.formats = formats
    
    def __cmp__(self, other):
        return cmp(self.item, other.item)

class BorrowedMovie(StockedMovie):
    
    def __init__(self, item, formats):
        super(BorrowedMovie, self).__init(item, formats)
        self.borrowed = False;

class Customer(object):
    
    def __init__(self, cID, name):
        self.cID = cID
        self.name = name
        self.items = []

class Show(object):

class History(object):

class Borrow(object):

class Return(object):

genres = {
    "C": {
        "type": Classic,
        "movies": []
    },
    "F": {
        "type": Comedy,
        "movies": []
    },
    "D":  {
        "type": Drama,
        "movies": []
    }
}

customers = {}

with open("<movie input>") as movie_input:
    for line in movie_input:
        line = line.strip()
        movie = genres[line[0]]["type"].build(line[2:])
        genres[line[0]]["movies"].append(StockedMovie(movie))

with open("<customer input>") as customer_input:
    for line in customer_input:
        cID, name = line.strip().split(" ")
        customers[cID] = Customer(cID, name)
