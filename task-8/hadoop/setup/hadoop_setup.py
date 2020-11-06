import os


def hadoop_install():
    while True:
        print('Do you want to install the hadoop:')
        print('1. Locally?')
        print('2. Remotely?')

        exec_type = int(input('Enter the option: '))


def hadoop_install_local():

    while True:
        print("1. Installing the packages(JDK+Hadoop")
        print("2. Configuring the Hadoop")
        print("3. ")