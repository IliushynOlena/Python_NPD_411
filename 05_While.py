



i = 0 #1.створення лічилька
while i < 10: #2. перевірка умови (ваш лічильник має бути використаний в самій умові)
    i +=1 #3. збільшувати лічильник
    print(i ,"Hello world ")

#вивести всі числа від 5 до 20 - 5 6 7 8 9....20

i = 5
while i <= 20:
    print(i, end=" ")
    i+=1
print()
#вивести всі числа від 10 до 0 -- 10 9 8 7 6 5...0
i = 10
while i >= 0:
    print(i, end=" ")
    i-=1
print()
#користувач вводить число…вивести всі числа від введеного користувачем значення до 20
i = int(input("Enter number : "))#30

if i<= 20:
    while i <= 20:
        print(i, end=" ")
        i+=1
else:
    while i>= 20:
        print(i, end=" ")
        i-=1
print()

#користувач вводить число…вивести таблицю множення на це число
number = int(input("Enter number : "))
if number <0 or number > 10:
    print("Error")
else:
    i = 1
    while i <= 10:
        print(f"{number} * {i} = {number*i}")
        i+=1
    else:
        print("="*30)

# number %2 == 0 - parne
# number %2 !=0 - ne parne
