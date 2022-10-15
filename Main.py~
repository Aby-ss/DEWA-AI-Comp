from rich.panel import Panel
from rich.live import Live
from rich import print
from time import sleep
import fileinput

import psutil
import os

from rich.traceback import install
install(show_locals = True)



    # ------------------------------------- WELCOME TO THE APP -------------------------------------
def app():
    
    welcome_art = "DEWA PROJECT - BACKEND VISULAIZATION"
    print(welcome_art)
    print(" ")
    
    cpu_usage = psutil.cpu_percent(interval=1)
    no_of_cores = psutil.cpu_count()
    used_virtual_memory = psutil.virtual_memory()[2]
    

    cpu_info = f"Number of Cores in Your System : {no_of_cores}\nCPU Usage : {cpu_usage}\nRAM memory used : {used_virtual_memory}"

    cpu_track = Panel(f"{cpu_info}", title=" CPU ", subtitle=" Artificial Intelligence ", border_style="green")
    with Live(cpu_track, auto_refresh=True):
        cpu_usage = cpu_usage
        sleep(1)
    print(" ")
    

    info_channel = Panel("1 - Video Detection\n2 - Chat Bot\n3 - Notification\n0 - EXIT", title="Choose your test action", subtitle=" ... ", border_style="bold blue")
    print(info_channel)
    print(" ")
    
    while True:
        Option = int(input(">> "))
        if Option == 1:
            print("Video Detection Commensing . . . ")
            import OBJ_Detection as live_detect
            live_detect.obj_detection()
        elif Option == 2:
            print("Chat Bot Commensing . . . ")
        elif Option == 3:
            print("Notifications Commensing . . . ")
        elif Option == 0:
            exit()
        else:
            print("WRONG CHOICE OF NUMBER !!")
            exit()



# -------------------------------------------------------------------------------------------                
methods_LOGIN = "1 - LOG IN\n2 - SIGN UP"

print(methods_LOGIN)
user_credentials = int(input("Choose your LOGIN method :"))


if user_credentials == 1:
    # ---- LOG  IN ----
    
    logIn_username_ = input("Username 🕵🏻‍♂️: ")
    logIn_password_ = input("Password 🔒: ")
    
    LOGIN = Panel(f"{logIn_username_}\n{logIn_password_}", title="LOGGING IN . . .", subtitle = "  ...  ", border_style = "bold blue")
    
    with open('Users.txt','r') as file:
        for line in file:
            usernames = line.split()[0]
            passwords = line.split()[1]

    if ((logIn_username_ == usernames ) and (logIn_password_ == passwords)):
        print(f"Welcome back {logIn_password_} , you can choose your options below !")
        print(" ")
        
        print(LOGIN)
        
        
    app()
    # ---- ... ----



            
elif user_credentials == 2:
    # ---- SIGN UP ----
    signUp_username_ = input("Create a Unique username 🎈: ")
    signUp_password_ = input("Create a unique password that you can remember 💼: ")

    # ---- SIGNGIN IN USER ----
    SIGNUP = Panel(f"{signUp_username_}\n{signUp_password_}", title="SIGNING YOU IN . . .", subtitle="  ...  ", border_style= "bold blue")
    # ---- ... ----

    print(SIGNUP)
    
    with open(pass_path, 'a') as file:
        file.write(signUp_username_ + " " + signUp_password_)
        main()
else: 
    print("WORNG CHOICE")



