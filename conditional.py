color =input("Enter the color of traffic light: ")

if color =="Red":
    print("Stop")
elif color =="Yellow":
    print("get ready to go ")
elif color =="Green":
    print("Now Go")   

# Match Case 
color = input("Enter the color of traffic light: ")
match color:
    case "Green":
        print("Now Go")
    case "Yellow":
        print("get ready to go ")
    case "Red":
        print("Stop")    
    case _ :
        print("Invalid color") 
# Range()
n=int(input("Enter a number: "))

sum=0
for i in range(1,n+1):
    sum+=i
print("Sum of first",n,"numbers is",sum)
