
# number1 = None
# number2 = None
# while number1==None or number2 == None:
#     try:
#         number1 = int(input("Enter number : "))
#         number2 = int(input("Enter number : "))
#         print(number1/number2)
    
#     except ValueError:
#         print("Value Error . You must enter number ...")
#     except ZeroDivisionError:
#         print("division by zero")
#     except Exception:
#         print("Some error")

# print("Continue......")
# print("Continue......")
# print("Continue......")

try:
    age = int(input("Enter age : "))
    
    if age < 0 :
        #raise == throw exception       
        raise Exception("Age error < 0....")
    
    if age > 125:        
        raise Exception("Age error > 125....")

    print(f"Age = {age}")
except ValueError:
    print("Value Error . You must enter number ...")
    

except Exception as ex:
    print(ex)
    
else:
    print("When all is fine...")
    
finally:
    print("Work always")
    #file.close()


try:
    colors = ['red','white','blue','yellow','green']#0....4
    index = int(input("Enter index of element : "))
    print(colors[index])
except ValueError:
    print("Value Error. Incorrect number ")
except IndexError:
    print("list index out of range")
