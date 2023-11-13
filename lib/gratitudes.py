class Gratitudes:
    def __init__(self):
        self.gratitutes = []

    
    def add(self,gratitude):
        gratitude = ""
        self.gratitudes.append(gratitude)

    
    def format(self):
        formatted = "Be grateful for: "
        formatted += ", ".join(self.gratitudes)
        return formatted