class StringBuilder:
    def __init__(self):
        self.str = ""

    
    def add(self,str):
        self.str +=str
        return self.str

    
    def size(self,str):
        self.str += str
        return len(self.str)

    
    def output(self,str):
        self.str+=str
        return self.str