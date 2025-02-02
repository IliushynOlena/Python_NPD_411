matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

print(matrix)
#show all rows in matrix
for row in matrix:
    print(row)

for row in matrix:
    for elem in row:
        print(elem, end=" ")
    print()

print("---------- Get elements by index -------------")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j] , end=" ")
    print()


import random
matrix = []
row = 3
col = 4

# for i in range(row):
#     numbers = []
#     for j in range(col):
#         numbers.append(random.randint(20,50))
#     matrix.append(numbers)
for i in range(row):
    matrix.append([ random.randint(20,50) for j in range(col)])


for row in matrix:
    for elem in row:
        print(elem, end=" ")
    print()
#summa elements in row 
summa = 0
for row in matrix:
    summa += sum(row)
    print(f"Summa elements in one row : {sum(row)}")

print(f"Summa element in matrix : {summa}")

#summa elements in cols
summa = 0
row = 3
summa_total = 0
for i in range(col):
    summa = 0
    for j in range(row):
        summa += matrix[j][i]
        summa_total += matrix[j][i]
    print(f"Summa elements in one col : {summa}")

print(f"Summa element in matrix colume : {summa_total}")