import os
from hadoop.interface.local import hadoop_interface_local
from hadoop.interface.remote import hadoop_interface_remote


def hadoop_interface():

    while True:
        print('Do you want to start/stop the hadoop ')
        print('1. Locally')
        print('2. Remotely')
        
        exec_type = int(input('Enter the option: '))

        if exec_type == 1:
            hadoop_interface_local.hadoop_interface_local()

        elif exec_type == 2:
            hadoop_interface_remote.hadoop_interface_remote()

        else:
            return
