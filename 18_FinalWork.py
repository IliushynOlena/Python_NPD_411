import json
def AddNewUser():
    id = int(input("Enter id : "))
    name = input("Enter name : ")
    return {'id':id,'name':name}

def createList(count):
    users = []
    for i in range(count):
        users.append(AddNewUser())
    return users

def printAllUsers(users):
    for i in range(len(users)):
        print(users[i])

def writeToFile(users):
    with open('students.json', 'w') as file:
        file.write(json.dumps(users))

def readFromFile():
    with open('students.json', 'r') as file:
        return json.loads(file.read())

while True:
    choice = int(input('''
        1 - Fill database 
        2 - Add new user
        3 - Delete user
        4 - Print all users
        5 - Sort by name
        0 - Exit
    '''))
    if choice == 1:
        number = int(input("Enter count users : "))#4
        users = createList(number)
        writeToFile(users)
    if choice == 0:
        print("Goodbye")
        break
    if choice == 4:
        users = readFromFile()
        printAllUsers(users)

    if choice == 5:
        users = readFromFile()
        printAllUsers(users)
        users.sort(key = lambda u:u['id'])
        printAllUsers(users)

              

