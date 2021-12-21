from colorama import Fore
import os
import screen_brightness_control as br

cmd = os.system("sleep 3 && clear")


def intro():
    print("welcome to bright ")
    print("                             ")
    print("                             ")
    print("                             ")
    print(
        Fore.YELLOW + "                                  0000000       00000000      000000000000      0000000000       00       00     000000000000")
    print(
        Fore.YELLOW + "                                  00     00     00     00     0    00    0     00         00     00       00     00   00   00")
    print(
        Fore.YELLOW + "                                  00     00     00      00         00         00           00    00       00          00    ")
    print(
        Fore.YELLOW + "                                  0000000       00     00          00        00                  00000000000          00    ")
    print(
        Fore.YELLOW + "                                  0000000       00000000           00        00       000000     00000000000          00    ")
    print(
        Fore.YELLOW + "                                  00     00     00    00           00        00       00  00     00       00          00    ")
    print(
        Fore.YELLOW + "                                  00     00     00     00     0    00    0    00      00  00     00       00          00    ")
    print(
        Fore.YELLOW + "                                  0000000       00      00    000000000000     000000000  00     00       00          00    ")
    print("                             ")
    print("                             ")
    print("developed by:teckhacker1990           ")
    print("visit may channel:")

    print("[1]scan brightness ")
    print("[2]change brightness")
    print("[3]exit")
    print("                             ")
    print("                             ")

    # importing the module
    # importing the module

    bright = br.get_brightness()
    command = int(input("COMMAND:"))
    if command == 1:
        if bright == 100:
            print("current brightness:-")
            print(bright)
            print("you can not increase brightness , you can only decrease")
            com = input("command>>>")
            if com == 'exit()':
                intro()
            else:
                print("if you want to exit to main menue run command 'exit' ")
                com = input("command>>>")

        else:
            print("current brightness:-")
            print(bright)
            print("you can increase it ")
            intro()

    elif command == 2:
        com1 = int(input("change brightness to:"))
        br.set_brightness(com1)
        intro()
    elif command == 3:
        exit()


intro()
