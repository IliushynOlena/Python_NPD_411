
# for i in range(10):#i = 0;i <10; i+=1
#     for j in range(10):# j = 0; j < 10; j +=1
#         print(" *",end=" ")
#     print()

# print("Continue......")

# for i in range(1,11):#1....10
#     for j in range(1,11):
#         print(f"{i} * {j} = {i*j}")
#     print()

# floor = 1
# energy = 70
# print(f"I am on the {floor} floor")

# while floor != 5:
#     step = 0

#     if floor == 3:
#         print("I will take an elevator....")
#         break
#     while step != 20:
#         step+=1
#         energy -=1
#         if energy == 0:
#             print("I am tired, I will rest a little")
#             energy+=70    


#     floor+=1
#     print(f"I am on the {floor} floor")

#Task 1
A = int(input("Введіть початок діапазону (A) : "))#1
B = int(input("Введіть кінець діапазону (B) : "))#11
for num in range(A,B+1):
    print(f"Дільники для числа {num} - {', '.join([str(i) for i in range(1, num+1) if num % i == 0])}",sep='\n')
#1 --> 1/1
#2 --> 2/1 2/1 
for num in range(A, B+1):
    print(f"Дільники для числа {num} : ", end=" ")
    for div in range(1, num+1):
        if num%div == 0:
            print(div, end= ", ")
    print()
    







