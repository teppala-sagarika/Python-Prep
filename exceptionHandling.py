#EXCEPTION HANDLING
#try, except , fnally , else

try:
    x=int(input("enter a divisor="))
    ans=10/x

except ZeroDivisionError: #divison by 0 
    print("Division by 0 is not allowed")

#u can also handle multiple exceptions for a try block
except ValueError: #string instead of int
    print("Invalid input")

else:
    print(f"ans = {ans}")

#finally executes irrespective of the error being thrown or not
finally:
    print("End of program")