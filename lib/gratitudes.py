class Gratitudes:
    def __init__(self):
        self.gratitudes = []

    
    def add(self,gratitude):
        result = self.gratitudes.append(gratitude)
        return result

    
    def format(self):
        formatted = "Be grateful for: "
        formatted += ", ".join(self.gratitudes)
        return formatted