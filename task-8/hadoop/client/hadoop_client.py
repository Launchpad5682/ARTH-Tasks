import os
from hadoop.client.local import hadoop_client_local
from hadoop.client.remote import hadoop_client_remote

def hadoop_client():

    while True:
        print('Do you want use the Hadoop Client')
        print('1. Locally')
        print('2. Remotely')

        exec_type = int(input('Enter the option: '))

        if exec_type == 1:
            hadoop_client_local.hadoop_client_local()
        
        elif exec_type == 2:
            hadoop_client_remote.hadoop_client_remote()

        else:
            os.system('clear')
            return