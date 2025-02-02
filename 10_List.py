#List - список - масив
category = ["Drama","Comedy","Fantasy"]
print(category)


courses = list(("Python","HTML","SQL","C#","C++"))
print(courses)

a = 0
print(a)
a = 15

studentsScores = []
students = list()
print(studentsScores)
print(students)

myList = ["Math",2589, 4.25,True, False,[1,2,3,4,5,1.2, "Text"]]
print(myList)
print(myList[0])
print(myList[2])
print(myList[5])
print(myList[len(myList)-1])
print(myList[-1])
print(myList[-1][-1])

customers = ["Bob", "Jack","Tom","Anna","Bob", "Jack","Tom"]
print(customers)

letters = list("qwertyuiook")
print(letters)

#створення списку з використанням генераторів
#newList = [expession for item in sequence]
#expession - вираз або формула для одного елементу
#for item in sequence - цикл, який дає нам послідовність елементів(або кількість ітерацій)
for i in range(6):
    print(i)#0 1 2 3 4 5


list_1 = [i  for i in range(6)]
print(list_1)

list_2 = [i*i  for i in range(6)]
print(list_2)

list_3 = [i+10  for i in range(6)]
print(list_3)

import random
list_4 = [random.randint(20,50)  for i in range(10)]
print(list_4)

for l in "example":
    print(l)#e x a m p l e

list_5 = [l for l in "example"]
print(list_5)

list_6 = [l*3 for l in "example"]
print(list_6)

list_7 = [s for s in "language"]
print(list_7)

print("_".join(list_7))

colors = "red white grey black green blue yellow pink lime orange"
new_colors = colors.split(" ")
print(new_colors)


#при генерації елементів списку можна вказати умову, які саме елементи брати з послідовності
#if condition  - умова
#newList = [expession for item in sequence if condition ]

list_8 = [i   for i in range(1,11)]
print(list_8)

list_8 = [i   for i in range(1,11) if i%2==0]
print(list_8)

list_8 = [i   for i in range(1,11) if i%2 != 0]
print(list_8)

customers = ["Bob", "Jack","Tom","Anna","Bob", "Jack","Tom"]
print(customers)

list_9 = [c for c in customers if c !="Bob" and c !="Jack"]
print(list_9)

# for x in range(1,5) :
#     for y in range(1,5):
#         print(x*y, end=" ")
#     print()

list_10 = [x*y   for x in range(1,5)  for y in range(1,5)]
print(list_10)

myList = ["Math",2365,5.13,"Yellow",True, False,[1,45,23,14]]
print(myList)
print(myList[0])
print(myList[2])
print(myList[len(myList)-1])
print(myList[-1])
#зріз = [start : stop : step]
print(myList[1:3])
print(myList[-4:-2])
print(myList[1:-1])
# # #reverse 
print(myList[::-1])
print(myList[4::-1])
print(myList[-4::-1])

category =["Drama", "Comedy", "Fantasy"] 
print(category)
print(category[0])
category[0] = "Action"
print(category[0])
print(category)

userLogs = ["admin","student","teacher","hr","user"]
prices = [100,200,30,400,50]
print(len(userLogs))
print(len(prices))

print(sorted(userLogs))
print(sorted(prices))

print(min(userLogs))
print(min(prices))

print(max(userLogs))
print(max(prices))

#print(sum(userLogs)) #error
print(sum(prices))

#operator + 
category1 = ["Drama", "Comedy", "Fantasy","History"]
category2 = ["Cartoon","Horor","History","Science"]
print( category1 + category2 )
print(category1*2)

category = ["Drama", "Comedy", "Fantasy","History"]

for film in category:
    #film = "Error"
    print(film)

print(category)
# len(category) ---> 4
# for i in range(4) ---> 0 1 2 3
for i in range(len(category)):
    #category[i] ="Error"
    print(category[i])

print(category)

print("Methods list : ")
category = ["Drama", "Comedy", "Fantasy","History"]
category2 = ["Cartoon","Horor","History","Science"]
print(category)
#add to the end one element
category.append("Cartoon")
print(category)
#add to the end list of elements
category.extend(["Cartoon","Horor","History","Science"])
#category.extend(category2)
print(category)
# add element in the index
category.insert(1,"History")
print(category)

#delete element by value
category.remove("Drama")
print(category)
#delete element by index
category.pop(0)
print(category)
#delete last element
category.pop()
print(category)
# #delete all elements
# category.clear()
# print(category)

#find element by value 
print("Find element History in index - " ,category.index("History"))
#print("Find element History in index - " ,category.index("Historyyyyyyy")) #not found

count_h = category.count("History")
print(f"Count History element = {count_h}")

print(sorted(category))#return copy of sorted list
print(category)

category.sort()
print(category)

category.sort(reverse=False)
print(category)

category.sort(reverse=True)
print(category)

customers = ['Bob',"Jack","Tom",'Anna','Bob',"Jack","Tom"]
for c in customers:
    if c =="Anna":
        print("Anna is in colection")
    

if "Anna" in customers:
    print("Anna is in the collection")
else:
    print("Error")

numbers = [1,2,3,4,5,6]

# copy_list = numbers
# print(numbers)
# print(copy_list)


# copy_list[0] = 444
# copy_list[3]=111

# print(numbers)
# print(copy_list)

#copy_numbers = numbers --? error
#copy 
#1 use method copy
#copy_numbers = numbers.copy()
#2 - use constructor list()
#copy_numbers = list(numbers)
#3- use [:]
copy_numbers = numbers[:]
print(f"Numbers = {numbers}")
print(f"Copy Numbers = {copy_numbers}")

copy_numbers[0]= 1000
print(f"Numbers = {numbers}")
print(f"Copy Numbers = {copy_numbers}")