master_pwd=input('Give the master Password : ').lower()

def view():
    with open('account_info.txt','r') as f:
        for line in f.readlines():
            data=line.rstrip()
            accountName,accountPassword=data.split(',')
            print('accountName : '+accountName+', accountPassword : '+accountPassword)

def add():
    accountName=input('Type your account Name !!')
    accountPassword=input('Type your account Password !!')

    with open('account_info.txt','a') as f :
         f.write('accountName : '+accountName+ ', accountPassword : '+accountPassword+"\n")

while True : 
    option=input('Give your option either view/add/q : ').lower()

    if option=='q' :
        break
    
    if option=='view':
        view()
    elif option=='add':
        add()
    else:
        print('Give your option Again ^ _ ^')
        continue