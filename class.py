class Student :
    def __init__ (self , name,cpga):
        self.name=name
        self.cpga=cpga

details = Student("Rahul", 8)  
details1=Student("Dipanshu",8.5)
print(details1.name)
print("Name:",details.name)
print("CPGA:",details.cpga)
   
