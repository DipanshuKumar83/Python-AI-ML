try :
    x=int(input("Enter a number:"))
    ans = 10/x

except ZeroDivisionError:
    print("You cannot divide by zero")

except ValueError:
    print("Please enter a valid number")

else :
    print("The answer is:",ans)  
finally :
    print("Thsi is finaly block")    
