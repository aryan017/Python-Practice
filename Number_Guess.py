import random

top_of_range=input("Give the range of Number ")

if top_of_range.isdigit() : 
    top_of_range=int(top_of_range)
else:
    print('It is not a Number')
    quit()

range=random.randint(0,top_of_range)

count=0
while True : 
    guess=input('Make a Guess ')

    if guess.isdigit() : 
        guess=int(guess)
    else :
        print('Guess is not a number')
        quit()

    if guess==range : 
        print('You Got it Right')
        break
    elif guess>range :
        print('You got a Guess Above')
        count+=1
    else : 
        print('You got a Guess Below')
        count+=1

print('Number of times You got Guess Wrong',count,'Guess')