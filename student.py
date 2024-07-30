# Objects, define a class, methods and assign some properties
class Student():
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def changeID(self, id):
        self.id = id
    
    def print(self):
        print(f"{self.name} - {self.id}")

jane = Student("Jane", 155)
jane.print()
jane.changeID(425)
jane.print()


