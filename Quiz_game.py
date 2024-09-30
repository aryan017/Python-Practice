print("Welcome to the Infinity Stone Quiz Game : ")

play=input('Do you want to Play? ')

if play != 'yes' : 
    print('ok')
else :
    print('Time to play')

score=0
stone=input('What does Time stone do? ').lower()
if stone == 'control time' :
    print('Correct')
    score+=1
else : 
    print('Incorrect')

stone=input('What does Soul Stone do? ').lower()
if stone == 'control soul' :
    print('Correct')
    score+=1
else : 
    print('Incorrect')

stone=input('What does Space stone do ? ').lower()
if stone == 'control space' :
    print('Correct')
    score+=1
else : 
    print('Incorrect')


print(score)