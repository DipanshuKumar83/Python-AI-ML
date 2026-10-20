class Employee:
    Start_time ="9am"
    End_time="6pm"

class Teacher(Employee):
    def __init__(self,subject):
        self.subject=subject
        t1=Teacher("Math")
        print(t1.Start_time,t1.End_time,t1.subject)
