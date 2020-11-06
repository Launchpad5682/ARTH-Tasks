import os
from hadoop.interface import hadoop_interface
from hadoop.setup import hadoop_setup
from hadoop.client import hadoop_client


def hadoop():

    while True:
        print('1. Hadoop Installation')
        print('2. Hadoop Interface(for starting/stopping the namenode/datanodes)')
        print('3. Hadoop Client')

        # user input entered
        var = int(input("Enter the option: "))
        if var == 1:
            hadoop_setup.hadoop_install()

        elif var == 2:
            hadoop_interface.hadoop_interface()

        elif var == 3:
            hadoop_client.hadoop_setup()

        else:
            return
