name  ="Mukola"
surname = "Ivanchuk"
lastname = 'Petrovuch'
age = 18
marks = [12,11,10,8,9,6,3,12]
birthday = '12.05.2008'

student1 = ["Mukola","Ivanchuk",'Petrovuch',18,[12,11,10,8,9,6,3,12],'12.05.2008']
print(student1)
student1[4] = 21
print(student1)

student = {
    # key : value
    # key - string, numbers
    #value - any type
    'name':'Mukola',
    'surname':'Ivanchuk',
    'lastname':'Petrovuch',
    'age':18,
    'marks':[12,11,10,8,9,6,3,12],
    'birthday' :  '12.05.2008'
}

print(student['name'])
print(student['birthday'])
print(student['name'], student['birthday'])


#get all kyes
for key in student.keys():
    print(f"Key : {key} ---- > Value : {student[key]}")

#get all values
for value in student.values():
    print(value)


#get all kyes and  values
for key, value in   student.items():
    print(f"{key} ---> {value}")

print(student.keys())
print(student.values())
print(student.items())

#delete keys
print(student)
del student['surname']
print(student)
#delete by key
student.pop('birthday')
print(student)
#delete last element
student.popitem()
print(student)

#add new key and value 
student['email'] = 'mukola@gmail.com'
print(student)

#change value
student['email'] = 'super_puper@gmail.com'
print(student)

numbers = [5,7,8,9]
print("----------------------------------------------------------------------")
group = [
    
{'name':'Mukola', 'surname':'Ivanchuk','lastname':'Petrovuch','age':18,'marks':[12,11,10,8,9,6,3,12], 'birthday' :  '12.05.2006'},
{'name':'Olga', 'surname':'Ivanchuk','lastname':'Petrovuch','age':18,'marks':[12,11,10,8,9,6,3,12], 'birthday' :  '12.07.2008'},
{'name':'Ivanka', 'surname':'Ivanchuk','lastname':'Petrovuch','age':18,'marks':[12,11,10,8,9,6,3,12], 'birthday' :  '12.12.20098'},
{'name':'Oleg', 'surname':'Ivanchuk','lastname':'Petrovuch','age':18,'marks':[12,11,10,8,9,6,3,12], 'birthday' :  '12.05.2005'},
]

print(group[3])
print(group[3]["marks"])
print(group[3]["marks"][0])
print(group[0])
group[0]['birthday'] = '01.01.2001'
print(group[0]['birthday'])

for mark in group[3]["marks"]:
    print(mark, end=" ")
print()


import json
student = {
    'name':'Mukola',
    'surname':'Ivanchuk',
    'lastname':'Petrovuch',
    'age':18,
    'marks':[12,11,10,8,9,6,3,12],
    'birthday' :  '12.05.2008'
}


print(student)
print(type(student))

byte_obj = json.dumps(student)
print(byte_obj)
print(type(byte_obj))
with open('student.txt', 'w') as file :
    file.write(byte_obj)

new_obj = json.loads(byte_obj)
print(new_obj)
print(type(new_obj))
print("Rad from file")
with open('student.txt') as file:
    info = file.read()
    info = json.loads(info)
    print(info)
    print(type(info))
    print(info['name'])