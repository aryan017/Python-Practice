import random

options=["rock","paper","scissor"]

user_wins=0
computer_wins=0

while True : 
    userInput=input("State Rock/Paper/Scissor or Q to quit :").lower()

    if userInput=='q' :
        break

    if userInput not in options :
        continue

    Random_index=random.randint(0,2)

    computer_Input=options[Random_index]

    if userInput=='rock' and computer_Input=='scissor' :
        user_wins+=1
        print("win")
        continue
    elif userInput=='paper' and computer_Input=='rock' :
        user_wins+=1
        print("win")
        continue
    elif userInput=='scissor' and computer_Input=='paper' :
        user_wins+=1
        print("win")
        continue
    else :
        computer_wins+=1
        print("lose")
        continue

print('User Wins',user_wins)
print('Computer Wins',computer_wins)


