import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLUMNS=3

SYMBOLS_COUNT={
    'A' : 2,
    'B' : 3,
    'C' : 6,
    'D' : 8
}

SYMBOLS_VALUE={
    'A' : 5,
    'B' : 4,
    'C' : 3,
    'D' : 2
}

def get_Slot_Machine_Input(ROWS,COLUMNS,SYMBOLS_COUNT):
    All_Symbols=[]
    
    for symbol,count in SYMBOLS_COUNT.items():
        current_symbol=symbol
        for _ in range(count):
            All_Symbols.append(current_symbol)
    
    symbols=[]
    
    for _ in range(COLUMNS):
        symbol=[]
        Current_Symbols=All_Symbols[:]
        for _ in range(ROWS):
            value=random.choice(Current_Symbols)
            Current_Symbols.remove(value)
            symbol.append(value)
        
        symbols.append(symbol)
        
    return symbols

def get_Slot_Machine(symbols):
    
    for row in range(len(symbols)):
        for i,col in enumerate(symbols):
            if i!=len(symbols)-1:
                print(col[row],end='|')
            else:
                print(col[row],end='')
        print()
       
    
def deposit():
    while True:
        amount=input("How much amount you want to deposit for betting? ")
        if amount.isdigit() :
            amount=int(amount)
            if amount>0 :
                break
            else :
                print("Your amount should be Greater than zero")
        else:
            print("Please enter a Number")

    return amount

def Number_Of_Lines():
    while True:
        lines=input("Please enter the number of Lines you want to bet on between (1-"+str(MAX_LINES)+")?")
        
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=3:
                break
            else:
                print("Please enter between the range")
        else:
            print("Please enter a Number")
    return lines

def bet():
    while True:
        bet=input(f"How much bet you want to bet on Each line between ${MIN_BET}-${MAX_BET}?")
        
        if bet.isdigit():
            bet=int(bet)
            if MIN_BET<=bet<=MAX_BET:
                break
            else:
                print(f"Bet should be between ${MIN_BET}-${MAX_BET}")
        else:
            print("Please enter a Number")
            
    return bet
                
    
def main():
    Deposit=deposit()
    lines=Number_Of_Lines()
    while True:
        Bet=bet()
        total_bet=Bet*lines
        
        if total_bet>Deposit:
            print(f"You have insufficient Balance for betting, Current Balance is ${Deposit}")
        else:
            break
    
    print("You can bet")
    
main()

get_Slot_Machine(get_Slot_Machine_Input(ROWS,COLUMNS,SYMBOLS_COUNT))