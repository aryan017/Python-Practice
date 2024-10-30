import random

Max_Score=50

def roll() :
   return random.randint(1,6)

while True:
   Number_of_Players=input('Please type the number of players want to play : ')

   if Number_of_Players.isdigit():
       put_in_players_list=int(Number_of_Players)
       if put_in_players_list>=2 and put_in_players_list<=4 :
            break
       else :
            print('Number of players should be between 2 and 4')
   else:
      print('please write the valid input in the form of Integer')

players=[0 for _ in range(put_in_players_list)]


while max(players) < Max_Score : 
    for index in range(put_in_players_list) :
        score=0
        
        while True :
            Play_Or_NotPlay=input("Do you want to play or Not : ").lower()
            
            if Play_Or_NotPlay!='y':
                break
            
            value=roll()
            print(value)
            if value>=2 and value<=6 :
                score+=value
            else :
                score=0
                
        players[index]+=score
        print("Score of player",index+1,"is",players[index])
        
        
print("Player",players.index(max(players)),"has the maximum score of ",max(players))