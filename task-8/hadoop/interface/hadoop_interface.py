import os
from hadoop.interface.local import hadoop_interface_local
from hadoop.interface.remote import hadoop_interface_remote


def hadoop_interface():

    while True:
        print('Do you want to start/stop the hadoop ')
        print('1. Locally')
        print('2. Remotely')
        print('3. Return to Main Menu')
        print('4. Exit')

        exec_type = int(input('Enter the option: '))

        if exec_type == 1:
            hadoop_interface_local.hadoop_interface_local()

        elif exec_type == 2:
            hadoop_interface_remote.hadoop_interface_remote()

        elif exec_type == 3:
            break

        elif exec_type == 4:
            exit()

        else:
            input("Invalid Value, Press Enter to Continue")
            continue
