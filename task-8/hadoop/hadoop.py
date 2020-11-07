import os
from hadoop.interface import hadoop_interface
from hadoop.setup import hadoop_setup
from hadoop.client import hadoop_client


def hadoop():

    while True:
        print('1. Hadoop Installation')
        print('2. Hadoop Interface(for starting/stopping the namenode/datanodes)')
        print('3. Hadoop Client')
        print('4. Return to Main Menu')
        print('5. Exit')

        # user input entered
        var = int(input("Enter the option: "))
        if var == 1:
            # hadoop_setup.hadoop_install()
            print('Currently under development')

        elif var == 2:
            hadoop_interface.hadoop_interface()

        elif var == 3:
            hadoop_client.hadoop_client()

        elif var == 4:
            break

        elif var == 5:
            exit()

        else:
            input("Invalid Value, Press Enter to Continue")
            continue
