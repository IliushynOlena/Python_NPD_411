'''

def summa(*args):
    #args[0] = 1000 - error
    new_list = list(args)
    print(new_list)
    print(args)
    for el in args:
        print(el, end=" ")
    print()
    print(f"Element in index [0] - {args[0]} ")
    print(f"Find Element 5 - in index [{args.index(5)}]")
    print(f"Count Element 5  - {args.count(5)} ")
    print(f"Lenght  - {len(args)} ")
    return sum(args)
#(1, 5, 5, 7, 9, 7)  - cortege 
#45 + 78 + 6 + 3 8 5 + 4 2
# print(summa(1))
# print(summa(1,5))
# print(summa(1,5,5))
# print(summa(1,5,5,7))
print(summa(1,5,5,7,9,7,45,78,96,2))

def fullInfo(name, age, *marks):
    print(f"Name : {name}")
    print(f"Age : {age}")
    print(f"Marks : {marks}")


fullInfo("Mukola",18,12,10,9,7,11,10,12,8)

#lambda function - anonim function
'''
def sum(a,b):
    return a+b

def show(color):
    print(color)

print(sum(5,5))
show("white")

lambda_summa =  lambda a,b: a+b
lambda_show = lambda color:print(color)
print(lambda_summa(7,9))
lambda_show("red")
#-------------------1.1-----------------------
numbers = [1,5,89,6,3,2,4,7,85,3,6,9]

def modifyList(numbers):
    new_list=[]
    for elem in numbers:
        new_list.append(elem*2) 
    return new_list

print(numbers)
numbers = modifyList(numbers)
print(numbers)

#-------------------1.2 using lambda-----------------------
print("------------------1.2 using lambda-----------------------")
numbers = [1,5,89,6,3,2,4,7,85,3,6,9]

# def doubleNumber(x):
#     return x*2

print(numbers)
#numbers = list(map(doubleNumber,numbers))
#numbers = list(map(lambda x:x*2,numbers))
#numbers = list(map(lambda x:x*x,numbers))
numbers = list(map(lambda x:x+10,numbers))
print(numbers)




#-------------------2-----------------------
# line = list(map(int,input("Enter numbers : [5 8 9 6 3] ").split(' ')))
# #line = [ int(item) for item in line]
# print(line)

#filter()
numbers = [1,5,89,6,3,2,4,7,85,3,6,9]

# def parne(x):
#     if x%2== 0:
#         return True
#     else:
#         return False
# def parne(x):
#     return x%2== 0
    

#list_even = list(filter(parne,numbers))
list_even = list(filter(lambda x:x%2==0,numbers))
print(numbers)
print(list_even)

list_odd = list(filter(lambda x:x%2!=0,numbers))
print(numbers)
print(list_odd)

new_numbers= list(filter(lambda x:x>0 and x < 10,numbers))
print(numbers)
print(new_numbers)