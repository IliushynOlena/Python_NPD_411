'''
line = "Hello, world!"

print(line)
print(line[0])
print(line[1])
print(line[2])
print(line[6])
print(line[7])

for letter in line:
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
i = 5
while i <= 20:
    i+=1
    # if i%3!= 0:
    #     print(i, end=" ")
    if i%3== 0:
        continue
    print(i, end=" ")
print()