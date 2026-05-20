import time
#الاساس 
print(" hello and welcome to SIMPLE OS with py by karam ... v.0.1...")
print("    powered by OS SYS ")
time.sleep(2)
print("start OS")
time.sleep(5)
print("\x1b[92mwelcome\x1b[0m")

# larp os 🤑 
def neofetch():
    print("""
\033[96m
ooOOOOoo       ssSSSSss
oo.   oo       ss
oo.   oo         ssssss
ooOOOOoo       ssssssss
\033[0m
╔════════════════════════════════╗
║ \033[93mOS:\033[0m        S.OS v0.1                 ║
║ \033[93mKernel:\033[0m    S.OS Kernel               ║
║ \033[93mShell:\033[0m        SIMPLE OS Shell        ║
║ \033[93mTerminal:\033[0m     Custom                 ║
║ \033[93mColors:\033[0m       Hacker Green           ║
╚════════════════════════════════╝
""")

#info 
text = '''
this OS like Dos and early linux the kernel is simple and easy \n you don't need to learn it and enjoy the os
 v.0.1 created with python and with T STUDIO ;]
'''
# عقل النظام kernel 
while True:
    user_input = input("S_os$~/ ")
    if user_input == "help":
        print("info \n exit \n neofetch_larp\n you can use IT in this OS ") 
    elif user_input == "info":
        print(text)  
    elif user_input == "neofetch_larp":
        neofetch()  
    elif user_input == "exit":
        break  
    else:
        print("ERROR$404")  
