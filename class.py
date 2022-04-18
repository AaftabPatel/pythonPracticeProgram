print("program for class")
class car:
    def __init__(self,b_name,model,types):
        self.b_name=b_name
        self.model=model
        self.types=types
car1=car("Maruti","Ciaz","Sedan")
print("Brand name is:",car1.b_name)
print("model name is:",car1.model)
print("type is:",car1.types)
