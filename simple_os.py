import time
import os
import sys

# مسح الشاشة
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# شعار النظام
def show_banner():
    print("")
    print("  ███████╗██╗███╗   ███╗██████╗ ██╗     ███████╗")
    print("  ██╔════╝██║████╗ ████║██╔══██╗██║     ██╔════╝")
    print("  ███████╗██║██╔████╔██║██████╔╝██║     █████╗  ")
    print("  ╚════██║██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  ")
    print("  ███████║██║██║ ╚═╝ ██║██║     ███████╗███████╗")
    print("  ╚══════╝╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝")
    print("                    v0.2.1")
    print("")

# neofetch
def neofetch():
    print("")
    print("\033[96m")
    print("  ╔═══════════════════════════════════════╗")
    print("  ║            SIMPLE OS v0.2.1           ║")
    print("  ╠═══════════════════════════════════════╣")
    print("  ║ \033[93mOS:\033[0m        SIMPLE OS v0.2.1          ║")
    print("  ║ \033[93mKernel:\033[0m    S.OS Kernel                ║")
    print("  ║ \033[93mShell:\033[0m     SIMPLE OS Shell            ║")
    print("  ║ \033[93mTerminal:\033[0m  Custom                     ║")
    print("  ║ \033[93mColors:\033[0m    Hacker Green               ║")
    print("  ║ \033[93mCreated:\033[0m   Karam Al-Bari & T STUDIO   ║")
    print("  ╚═══════════════════════════════════════╝")
    print("\033[0m")

# الآلة الحاسبة
def calc():
    try:
        num1 = float(input("  enter the number> : "))
        op = input("  enter the operation> : ")
        num2 = float(input("  enter the number2> : "))

        if op == "+":
            print(f"  {num1} + {num2} = {num1 + num2}")
        elif op == "-":
            print(f"  {num1} - {num2} = {num1 - num2}")
        elif op == "*" or op == "×":
            print(f"  {num1} × {num2} = {num1 * num2}")
        elif op == "/" or op == "÷":
            if num2 == 0:
                print("  ERROR: Division by zero is not allowed.")
            else:
                print(f"  {num1} ÷ {num2} = {num1 / num2}")
        else:
            print("  ERROR: Unknown operation.")
    except ValueError:
        print("  ERROR: Invalid number input.")

# لعبة الثعبان (نسخة مبسطة)
def snake_game():
    print("  🐍 Snake Game is under development...")
    print("  Coming soon in v0.3!")
    print("  Press Enter to return.")
    input()

# معلومات النظام
def show_info():
    print("""
  ╔═══════════════════════════════════════╗
  ║           ABOUT SIMPLE OS             ║
  ╠═══════════════════════════════════════╣
  ║  SIMPLE OS is a lightweight terminal  ║
  ║  operating system inspired by DOS and ║
  ║  early Linux. It was created to be    ║
  ║  simple, educational, and fun to use. ║
  ║                                       ║
  ║  Version: 0.2.1                       ║
  ║  Creator: Karam Al-Bari               ║
  ║  Studio: T STUDIO                     ║
  ║  Powered by: OS.SYS Concept           ║
  ╚═══════════════════════════════════════╝
  """)

# دالة المساعدة
def show_help():
    print("""
  ╔═══════════════════════════════════════╗
  ║           AVAILABLE COMMANDS          ║
  ╠═══════════════════════════════════════╣
  ║  help        - Show this help menu   ║
  ║  info        - System information    ║
  ║  neofetch    - Display system info   ║
  ║  calc        - Open calculator       ║
  ║  snake       - Snake game (soon)     ║
  ║  clear       - Clear screen          ║
  ║  exit        - Exit SIMPLE OS        ║
  ╚═══════════════════════════════════════╝
  """)

# ========== الرئيسي ==========
clear_screen()
show_banner()
print("  [ powered by OS.SYS concept ]")
time.sleep(2)
print("  Starting SIMPLE OS...")
time.sleep(1)
print("\033[92m  Welcome to SIMPLE OS!\033[0m")
time.sleep(1)
clear_screen()

while True:
    try:
        user_input = input("  S_os$~/ ").strip().lower()
        
        if user_input == "help":
            show_help()
        elif user_input == "info":
            show_info()
        elif user_input == "neofetch":
            neofetch()
        elif user_input == "calc":
            calc()
        elif user_input == "snake":
            snake_game()
        elif user_input == "clear":
            clear_screen()
        elif user_input == "exit":
            print("  Shutting down SIMPLE OS... Goodbye!")
            time.sleep(1)
            clear_screen()
            break
        elif user_input == "":
            continue
        else:
            print(f"  ERROR 404: '{user_input}' not recognized. Type 'help'.")
    except KeyboardInterrupt:
        print("\n  Use 'exit' to quit.")
    except Exception as e:
        print(f"  ERROR: {e}")

sys.exit(0)
