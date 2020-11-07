import os
from partition_lvm_static import partition_menu
from hadoop import hadoop
from docker_task import script
from AWS import awsmain

import getpass
os.system("clear")
os.system("tput setaf 3")
print("\t\t\t Welcome to our Menu")
os.system("tput setaf 7")
print("\t\t\t -------------")

password = getpass.getpass("Enter your password to continue: ")

if password != "ARTH":
    input("Password is incorrect")
    exit()



def main():

    while True:
        os.system("clear")
        print('Select the options to perform')
        print('1. AWS CLI')
        print('2. Hadoop')
        print('3. Modifying Storages')
        print('4. Docker and Web Server')
        print('5. Quit')

        main_var = int(input('Enter the option: '))

        if main_var == 1:
            awsmain.hello_from_aws()
            continue

        elif main_var == 2:
            hadoop.hadoop()
            continue

        elif main_var == 3:
            partition_menu.partition()
            continue

        elif main_var == 4:
            script.hello()
            continue

        elif main_var == 5:
            exit()

        else:
            input("Invalid Value, Press Enter to Continue")
            continue

        continue


main()
