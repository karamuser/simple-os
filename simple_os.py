
import time
#الاساس 
print(" hello and welcome to SIMPLE OS with py by karam ... v.0.2...")
print("                  {powered by OS SYS} ")
time.sleep(2)
print("start OS")
time.sleep(5)
print("\x1b[92mwelcome\x1b[0m")

# larp os 🤑 
def neofetch():
    print("""
\033[96m
ooOOOOoo       ssSSSSss
oo    oo       ss
oo    oo         ssssss:
ooOOOOoo       ssssssss:
\033[0m
╔════════════════════════════════╗
║ \033[93mOS:\033[0m        S.OS v0.1                 ║
║ \033[93mKernel:\033[0m    S.OS Kernel               ║
║ \033[93mShell:\033[0m        SIMPLE OS Shell        ║
║ \033[93mTerminal:\033[0m     Custom                 ║
║ \033[93mColors:\033[0m       Hacker Green           ║
╚════════════════════════════════╝
""")
# calc in OS 👀
def calc():
    # calc brain 
    num1 = float(input(" enter the number>:  "))
    oP = input(" enter the operation>: ")
    num2 = float(input(" enter the number2>: "))
    #calc oP
    if oP == "+":
        print(num1+num2)
    elif oP == "-":
        print(num1-num2)
    elif oP == "×":
        print(num1*num2) 
    # stupid error      
    elif oP == "÷":
        if num2 and num1 != "0":
            print(num1/num2)
        else:
            print("error! stupid question bro....SON 🥀")
    else:
        print("error.in.input!")
#end

# ترا عندي حياة 😭 ✌️ 

#info 
text = '''
this OS like Dos and early linux the kernel is simple and easy \n you don't need to learn it and enjoy the os
 v.0.1 created with python and with T STUDIO ;]
'''
# عقل النظام kernel 
while True:
    user_input = input("S_os$~/ ")
    if user_input == "help":
        print("info \n exit \n neofetch_larp\n calc\n you can use IT in this OS ") 
    elif user_input == "info":
        print(text)  
    elif user_input == "neofetch_larp":
        neofetch()
    elif user_input == "calc":
        calc()
    elif user_input == "snake_game":
        snake_game()    
    elif user_input == "exit":
        break  
    else:
        print("ERROR$404")  
    
