from cryptography.fernet import Fernet

password = input ("Enter the master password: ")
if password != '@sme' :
    print('Invalid password!!! Run again.')
    quit()

# def write_key() :
#     key = Fernet.generate_key()
#     with open('key.key','wb') as key_file:    # wb = write bytes mode (special one)
#         key_file.write(key)

def load_key() :
    with open('key.key','rb') as f:
        key = f.read()
    
    # f = open('key.key','rb')
    # key = f.read()
    # f.close()
    return key

# write_key()
# master = input('Enter a master password: ')
key = load_key() #+ master.encode()
fer = Fernet(key)         # encode the key

def add() :
    name = input("Enter username: ")
    pas = input("Enter password: ")

    with open ("password.txt", "a")  as f :      # f = open ('password','a')     ....   f.close()
        f.write(name + "|" + fer.encrypt(pas.encode()).decode() + "\n")         #  samsun|123


def view() :
    with open ('password.txt', 'r') as f :
        
        # for line in f.readlines():            # ......................   .......................
        #     # print(line.rstrip())
        #     asme,tultul = line.split("|")                          # samsun  123    asme=samsun, tultul=123    print(user = asme, pass = tultul)
        #     print(f"Username = {asme} , Password = {tultul}")

        for line in f.readlines() :
            data = line.rstrip()
            u,p = data.split("|")
            print(f'Username = {u} , Password = {fer.decrypt(p.encode()).decode()}')


while True :
    n = input("Do u want to add a password or view or quit the program (a/v/q): ").lower()

    if n == 'q':
        break

    elif n == 'a':
        add()

    elif n == 'v':
        view()

    else :
        print("Invalid input!!!")
        # continue 

