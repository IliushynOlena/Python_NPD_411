'''
line = "Hello, world!"

print(line)
print(line[0])
print(line[1])
print(line[2])
print(line[6])
print(line[7])

for letter in line:# i = 0; i < 13; i +=1
    print(letter, end=" ")


print("Continue.......")
#[start = 0 : end = 13 : step = 1]
for letter in line[0:13:1]:
    print(letter, end=" ")
print()

#[start = 5 : end = 13 : step = 1]
for letter in line[5:]:
    print(letter, end=" ")
print()

#[start = 5 : end = 10 : step = 1]
for letter in line[5:10]:
    print(letter, end=" ")
print()

#[start = 0 : end = 13 : step = 1]
for letter in line[:]:
    print(letter, end=" ")
print()

#[start = 0 : end = 13 : step = 2]
for letter in line[::2]:
    print(letter, end=" ")
print()

#---------------2----------
for number in range(10): #start = 0, end = 10, step = 1
    print(number, end=" ")

print()

for number in range(10,20): #start = 10, end = 20, step = 1
    print(number, end=" ")

print()

for number in range(1,10,2): #start = 1, end = 10, step = 2
    print(number, end=" ")

print()

start = int(input("Enter start : "))
end = int(input("Enter end : "))

for number in range(start,end+1): #start = 10, end = 20, step = 1
    if(number %2 ==0 ):
        print(number, end=" ")

print()
# break 
while True:
    res = int(input(" 2 + 2 = ? -->  "))
    if res == 4:
        print("Congratulation.....")
        break
    else:
        print("Wrong answer...... Enter again")

print("Continue.....")
#continue

'''
# i = 5
# while i <= 20:
#     i+=1
#     # if i%3!= 0:
#     #     print(i, end=" ")
#     if i%3== 0:
#         continue
#     print(i, end=" ")
# print()
#----------------------------1--------------------------- simple number
# counter = 0
# number = int(input("Enter number : "))#8
# #100 = 100/1 100/2  100/4 100/5 100/10 .... 100/50 100/51 100/52 100/53
# #8 = 8/1 8/2 8/3 8/4 8/5 8/6 8/7 8/8
# #4 = 4/1 4/2 4/3 4/4
# for div in range(1, number + 1):
#     if number%div == 0:      
#         counter +=1

# print(f"Count div = {counter}")

# if counter > 2 :
#     print("Number is compound")
# else:
#     print("Number is prime")
#-----------------------2-------simple numbers
# flag = True
# number = int(input("Enter number : "))#8
# for div in range(2, number//2 + 1):#100//2 = 50
#     if number%div == 0:#100/2 100/3 100/4 100/5 100/6      
#         flag = False
#         break
# #and or ...not True---> False    False ---> True
# if not flag:
#     print("Number is compound")
# else:
#     print("Number is prime")

# if flag == True:
#     print("Number is prime")
# else:
#     print("Number is compound")
#---------3------------------------

number = int(input("Enter number : "))#8
for div in range(2, number//2 + 1):
    if number%div == 0:  
        print("Number is compound")
        break
else:
    print("Number is prime")

