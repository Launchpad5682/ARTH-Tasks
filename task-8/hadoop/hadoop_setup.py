import os
from hadoop.interface import hadoop_interface
from hadoop.setup import hadoop_setup

def hadoop():

    while True:
        print('1. Hadoop Installation')
        print('2. Hadoop Interface')

        # user input entered
        var = int(input("Enter the option: "))
        if var == 1:
            hadoop_setup.hadoop_install()

        elif var == 2:
            hadoop_interface.hadoop_interface()

        else:
            return

