
# print("Hello world")
# print('Hello world')
# a = 10
# login = "admin"
# password = 'qwerty123'
# print(login)
# print(id(login))
# login += "!!!"
# print(login)
# print(id(login))
# login = "Helen"
# print(login)
# print(id(login))


# message = "I\n\tLove\n\t\tPython"
# print(message)
# #line = "\\n - перехід на новий рядок"
# #r"C:\Users\helen\Desktop\Work\01_PythonCore\08_String_3_lessons\1"
# raw_line = r"\n - перехід на новий рядок"
# print(raw_line)

# print('''
# I 
#     Love 
#             Pyton''')
# img = '''
#                                      :^~~~~~^:.                                 
#                                 .^!?J??77???JJYYYJ7~:                           
#                              .!JJ7~:            .^!?Y5J~                        
#                            :?5?:        :^^^^:.      .~J5?:                     
#                          .J5!       .!JYJ7!!77YY:       .7P?                    
#                         !G7        ^P7^!~:.~~~ J#^         ?P^                  
#                        7B^         B7.~7~!77^:! &Y          ~G~                 
#                       ^B^          ?577! :^.!:7JG~           ~#.                
#                       P7      .:^~!!55Y77!!~7JJ5!^^:.         #!                
#                       G~   ^!?7!~^:.            .:^~!77~.     #!                
#                       7B^!J7:          .....          .~?7.  !B.                
#                        !P&J!!!7????YY777?????77JJ??7~!!^~?Y !G^                 
#           .^~7!!^.    ?7^JG57~7?!^7P@5       :P@@BPGP!!757JBG!:                 
# ^77777?YJ!JJ!J!?555575Y.^?57~    J?7?P7      PB7!?Y:.  .Y Y?~^??                
# B?:.  .^!^:7! :~^J?^ ?Y  7P^5^  Y5^J5?P^    :#77!.~Y   J^.BY:!!#                
# ^?JJJ?~      ^? Y7    57 7?J?   Y5^Y@@#7    ^@&&!~:J  :Y^ Y5: GJ                
#      .JY     ?? B.     Y?Y5? .^  J77JPG?~^^^:5BJ7!?.   .7~??~PJ                 
#        ?5.   :P.?J.     :YG  P@P!.:J5?~^:::^~75Y!^.^?GY :BJJY~                  
#        .G7    ^J~!??J?!7^!B  Y@@@&#P.         :5PP#@@@? .B:                     
#       7J~  .:^~?BJ!7!:.:^7BP. !5&@@5           7@@@#5!  55                      
#      ^P  ~5J7!!~:          ?B?  !#@&5~       :?#@@&!  ^5GY?~.                   
#       !7J5~                7#YGJ^::.:?J?77??JJ!YY~^!?PBPY5G&#J.                 
#        ..                 .&JJ^^7??!  .~77~. .7?    :J~.?!^?###!                
#                           !&J!   .5PJJ!~^^^!??PP!!?PJ~^:    ^.J&Y               
#                          :GB5^^: 7B!:~7????JJY?:.~P~    ~^^^  .:G7              
#                          JBJ5~:!Y!P:YP??JJ!~:    P^   :?^ ..^^  JG              
#                   ^!7????PGB? .7GJ7:B.          .G:  .P^   !5.  G7              
#                .75Y!:.    :75P557^  JY7!!77!?PY~ ^?7??G. .75  .5Y               
#               ?P7..:^^^^^:.  ^P5~:   :~!!~^. :!JYJ?JJ77JYJG?:~JJ.               
#             .PP^~??JJJJ????J!. BY??.             :^:^777??BJ~~:                 
#             PG!77!^:........?Y!!P !P                    . ?GYY7:                
#            !&J:             ~YG7G^ J?                .::.  777P#57.             
#            J&^               !5P5!  5^ .......:::.          .^.!BY5!            
#            J&.                5BP! .:^^~^^^^:::..               ^G^G7           
#            ~&.                J&5J:~^. ~. ..                    .#~7B           
#             G?                ?&:P5.JY~?!!!!!?Y7^.             :GG 7B           
#             ^B^               ?& ~G P7::^^^::.:!J5Y?~:.     .^JG? .B!           
#              !G~^^^^~~~~~~~~!!?#~ G?5             :!?YYYYYJ5BP?~~?G7            
#               7B??7777777!!77!J5P PP.                  ..::.:~!77~.             
#                5!             .J5JP.                                            
#                .Y!             ?&G:                                             
#                  !J!.        .?P!.                                              
#                   .~??!~~~~!?J7.                                                
#                      .:^^^^:.                                                   
# ......................      ....................................................
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# '''

# #print(img)

msg = "admin admin admin admin admin"
print(msg)
print(msg[0])
print(msg[1])
print(msg[2])
print(msg[3])
print(msg[4])
print(msg[-1])
print(msg[-2])
print(f"Lenght = {len(msg)}")
print(msg[len(msg)-1])


#конкатенація (додавання)
line1 = "Hello, "
line2 = "world"
line3 = "red"
print(line1 + line2)
line4 = line1 + line2 + line3
print(line4)

#дублювання рядків - оператор *
str = "Hello"
print(str*5)
myBigStr = str *10
print(myBigStr)


#визначення довжини рядка
str = "Hello world"
print(f"Length of string : {len(str)}")

name = "Nazar"
age = 22

#formatLine = name + "some text..." + name + " some text " + age + name + " some text ...."
#formatLine = name , "some text..." , name , " some text " , age , name ," some text ...."
#formatLine = "{} some text... {}  some text  {}  {}  some text ....".format(name,name,age,name)
#formatLine = "{} some text... {}  some text  {}  {}  some text ....".format(age,name,name,name)#danger
#formatLine = "{0} some text... {0}  some text  {1}  {0}  some text ....".format(name,age)
formatLine = f"{name} some text... {name}  some text  {age}  {name}  some text ...."
print(formatLine)

salary = 105.364654687987
message = f"You have salary {salary:10.2f} grn/h"
print(message)

start = -10
end = +10

myStr = f"The number is in range [{start:-}] - [{end:+}] "
print(myStr)

points = 10054654
myStr1 = f"You have points {points} points"
print(myStr1)

myStr1 = f"You have points {line1} {points:<20} points"
print(myStr1)

myStr1 = f"You have points {points:>20} points"
print(myStr1)

myStr1 = f"You have points {points:^20} points"
print(myStr1)

print("A")
print('A')
print(chr(65))
print(ord('A'))

for i in range(100):
    print(f"{i} ---> {chr(i)}", end="\t")
    if i%7==0:
        print()
print()
corn_left = 9556
line = 9552
t_element = 9574 
print(f"{chr(corn_left)}{chr(line)*4}{chr(t_element)}")





