class Clg:
    College ="ABC Colleges"

    def __init__(self , name,age,gpa ):
        self.name=name
        self.age=age
        self.gpa=gpa

st1 = Clg("Dipanshu ",20,9.2)
st2 = Clg("Rahul",21,8.5)
print(f"Student {st1.name} get {st1.gpa} gpa at {st1.age} age, college name is {st1.College}")
print(f"Student {st2.name} get {st2.gpa} gpa at {st2.age} age, college name is {st2.College}")
