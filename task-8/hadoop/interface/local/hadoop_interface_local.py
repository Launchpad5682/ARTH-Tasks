import os


def hadoop_interface_local():
    print("You are in Local execution console-->")
    while True:

        print('Select whether node is ')
        print('1. Namenode')
        print('2. Datanode')

        op = int(input('Enter the option: '))

        if op == 1:
            hadoop_local_namenode()

        elif op == 2:
            hadoop_local_datanode()

        else:
            return


def hadoop_local_namenode():

    while True:
        print('1. Start the namenode')
        print('2. Stop the namenode')
        op = int(input('Select the option: '))

        if op == 1:
            os.system('systemctl stop firewall')
            os.system('hadoop-daemon.sh start namenode')
            os.system('hadoop dfsadmin -safemode leave')

        elif op == 2:
            os.system('systemctl stop firewall')
            os.system('hadoop-daemon.sh stop namenode')

        else:
            return


def hadoop_local_datanode():

    while True:
        print('1. Start the datanode')
        print('2. Stop the datanode')
        op = int(input('Select the option: '))

        if op == 1:
            os.system('systemctl stop firewall')
            os.system('hadoop-daemon.sh start datanode')

        elif op == 2:
            os.system('systemctl stop firewall')
            os.system('hadoop-daemon.sh stop datanode')

        else:
            return
