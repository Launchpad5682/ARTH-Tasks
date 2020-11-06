# from partition import partition
import os
from hadoop import hadoop_setup
from docker_task import script
from AWS import awsmain

def main():
    os.system("clear")
    print('Select the options to perform')
    print('1. AWS CLI')
    print('2. Hadoop')
    print('3. Modifying Storages')
    print('4. Docker and Web Server')
    print('5. Quit')

    main_var = int(input('Enter the option: '))

    while True:

        if main_var == 1:
            awsmain.hello_from_aws()
            continue

        elif main_var == 2:
            hadoop_setup.hadoop()
            continue

        # elif main_var == 3:
        #     partition.partition()

        elif main_var == 4:
            script.hello()
            continue
            
        elif main_var==5:
            exit()

        else:
            input("Invalid Value, Press Enter to Continue")
            continue

        continue


main()
