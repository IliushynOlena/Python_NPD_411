import random
print("\t\tWelcome to the game")
print("\t\tRock Scissors Paper")

user = 0# r p s
bot = 0 #r p  s

while True:    
    user_score = 0
    bot_score = 0
    for round in range(3):
        print(f"---------------------------Round {round + 1}-----------------------------------")
        while True:
            user = input("\t [r] - Rock; \n\t [s] - Scissors; \n\t [p] - Paper;\n\t Enter your choice : ")
            user = user.lower()
            if user == 'r' or user == 's' or user == 'p':
                break
            else:
                print("Error input......")
        
        bot = random.choice('rps')
        print("\t Bot \t User")
        print(f"\t [{bot}] \t [{user}]")
        if (user =='r' and bot== 's') or (user =='p' and bot== 'r') or(user =='s' and bot== 'p') :
            user_score+=1
        elif (bot =='r' and user== 's') or (bot =='p' and user== 'r') or(bot =='s' and user== 'p') :
            bot_score+=1


    if user_score > bot_score:
        print("\t=================== Congratulation!!! User is winner  ========")
    elif bot_score > user_score:
        print("\t=================== Sorry ! You lose !!!======================")
    else:
        print("\t============================= Draw============================")

    while True:
        user = input("Play again ? [y] - Yes; [n] - No. Enter choive : ")
        user = user.lower()
        if user =='y' or user =='n':
            break
        else:
            print("Error input......")

    if user == 'n':
        print("Have a nice day! Goodbye!!!!")
        break