class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"이름 {self.name} 나이 {self.age}")