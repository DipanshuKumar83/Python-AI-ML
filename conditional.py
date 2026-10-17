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
