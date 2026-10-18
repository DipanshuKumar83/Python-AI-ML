a=5
b=10
sum=a+b
print("Sum of {} and {} is {}".format(a,b,sum))
print("sum of {1} and {0} is {2}".format(a,b,sum))


print("value of var {A} and {B}".format(A=2,B=3))

#F-String
def Sum(a,b):
    s=a+b
    return s
#calling functions 
Result=Sum(5,11)
print(f"Sum of a and b is {Result}")
