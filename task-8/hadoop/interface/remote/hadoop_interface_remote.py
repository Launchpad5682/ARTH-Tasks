import os


def hadoop_interface_remote():

    print("You are in Remote execution console-->")

    while True:
        login = input('Enter the username@ip_address')

        print('Select whether node is ')
        print('1. Namenode')
        print('2. Datanode')

        op = int(input('Enter the option: '))

        if op == 1:
            hadoop_remote_namenode(login)

        elif op == 2:
            hadoop_remote_datanode(login)

        else:
            return


def hadoop_remote_namenode(login):

    while True:
        print('1. Start the namenode')
        print('2. Stop the namenode')
        op = int(input('Select the option: '))

        if op == 1:
            os.system('ssh {} systemctl stop firewall', login)
            os.system('ssh {} hadoop-daemon.sh start namenode', login)
            os.system('ssh {} hadoop dfsadmin -safemode leave', login)

        elif op == 2:
            os.system('ssh {} systemctl stop firewall', login)
            os.system('ssh {} hadoop-daemon.sh stop namenode', login)

        else:
            return


def hadoop_remote_datanode(login):

    while True:
        print('1. Start the datanode')
        print('2. Stop the datanode')
        op = int(input('Select the option: '))

        if op == 1:
            os.system('ssh {} systemctl stop firewall', login)
            os.system('ssh {} hadoop-daemon.sh start datanode', login)

        elif op == 2:
            os.system('ssh {} systemctl stop firewall', login)
            os.system('ssh {} hadoop-daemon.sh stop datanode', login)

        else:
            return
