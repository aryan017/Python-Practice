import random
import string

def generate_password(min_length_of_Characters,numbers=True,special_characters=True):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation
    
    characters=letters
    
    if numbers:
        characters+=digits
    
    if special_characters:
        characters+=special
        
    pwd=""
    
    meets_criteria=False
    has_number=False
    has_special=False
    
    while not meets_criteria or len(pwd)<min_length_of_Characters:
        new_char=random.choice(characters)
        pwd+=new_char
        
        if new_char in digits :
            has_number=True
        elif new_char in special :
            has_special=True
            
        meets_criteria=True
        
        if numbers :
            meets_criteria=has_number
        if special_characters :
            meets_criteria=meets_criteria  and has_special
            
    return pwd

ans=""
while True :
    number_of_characters=int(input('Type the length of your Password please !!!'))
    things_you_want_in_password=input('For Numbers only type 0,\n'+"For Special_Characters only type 1, \n" + "For both type 2, \n" + 'For None of them type 3\n')
    if things_you_want_in_password=='0':
        ans=generate_password(number_of_characters,True,False)
        break
    elif things_you_want_in_password=='1':
        ans=generate_password(number_of_characters,False,True)
        break
    elif things_you_want_in_password=='2' :
        ans=generate_password(number_of_characters)
        break
    elif things_you_want_in_password=='3':
        ans=generate_password(number_of_characters,False,False)
        break
    else :
        print('Please type out of 0,1,2,3 only ')
        continue
    

print(ans)