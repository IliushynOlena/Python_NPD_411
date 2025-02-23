
# відкрити файл
# читати файл
# записати файл
# закрити файл

#абсолютний шлях до файлу
url = r'C:\Users\helen\Desktop\NewGroups\Python_NPD_411\16_Files\test.txt'
#відносний шлях до файлу(відносно кореневої папки в якій відкритий Visual Studio)
#file = open("./16_Files/test.txt")
#file = open("test.txt")

#file = open(url)

#читає всю інформацію з файлу і повертає рядок
#print(file.read())

#читає рядок до \n
# print(file.readline().strip())
# print(file.readline().strip())
# print(file.readline().strip())
# print(file.readline().strip())

#print(file.readlines())
# print(file.read(5))

# file.close()

# with open(url, 'r') as file: #file = open(url)
#     print(file.read())
#     #file.close()

#режим перезапису файлу
# url_write=  './16_Files/write_file.txt'
# with open(url_write,'w') as file:
#     file.write("Hello friend")

#режим дозапису файлу
# url_write=  './16_Files/write_file.txt'
# with open(url_write,'a') as file:
#     file.write("Hello friend\n")

lines = [
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
'Donec ac nunc convallis, sollicitudin tellus accumsan, dignissim augue.',
'In eleifend nisi eget ligula viverra, non posuere erat pharetra.',
'Nulla vitae justo finibus, pretium nisl et, laoreet dui.'
]

url_write=  './16_Files/write_file.txt'
#1 - wrile lines to file
# with open(url_write,'w') as file:
#     #file.write(lines)#error
#     counter = 1
#     for line in lines:
#         file.write(f"{counter}. {line}\n")
#         counter+=1

# with open(url_write,'w') as file:
#     file.writelines(lines)#error

def readFile(filename):
    with open(filename,'r') as file:
        return file.read()
        
def writeFile(filename,info):
    with open(filename,'a') as file:
        file.write(info)      



url_read = "./16_Files/test.txt"
url_write = './16_Files/write_file.txt'

#text = readFile(url_read)
# writeFile(url_write,text)
# lines = []
# with open(url_read) as file:
#     lines = file.readlines()

# with open(url_write,'a') as file:
#     for line in lines[::-1] :
#         #print(line.strip())
#         file.write(line.strip()+'\n')

with open(url_write,'r+') as file:
    print(file.readable())
    print(file.writable()) 