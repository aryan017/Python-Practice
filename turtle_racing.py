import turtle
import time
import random

WIDTH,HEIGHT=500,500

COLORS=['black','white','red','green','blue','yellow','cyan','magenta','gray','brown','orange','purple','pink']

def get_Number_of_Racing_Turtles():
    
    racers=0
    while True:
        racers=input("How many turtle you want to be in Racing ? ")
        
        if racers.isdigit():
            racers=int(racers)
            if 2<=racers<=10:
                return racers
            else:
                print('Number of Racers should be between 2 and 10')
        else:
            print('Enter a valid number not String')
            
def create_Racing_Turtles(colors):
    turtles=[]
    for i, color in enumerate(colors):
        Racing_Turtle=turtle.Turtle()
        Racing_Turtle.color(color)
        Racing_Turtle.shape('turtle')
        Racing_Turtle.left(90)
        Racing_Turtle.penup()
        Racing_Turtle.pendown()
        turtles.append(Racing_Turtle)
    
racers=get_Number_of_Racing_Turtles()

def init_Turtle_Racing_Window():
    screen=turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title('Turtle Racing')
   
init_Turtle_Racing_Window()

random.shuffle(COLORS)
colors=COLORS[:racers]

create_Racing_Turtles(colors)