import os


def hadoop_interface_local():

    while True:
        os.system('clear')
        
        print("You are in Local execution console-->")
        print('Select whether node is ')
        print('1. Namenode')
        print('2. Datanode')
        print('3. Return to Main Menu')
        print('4. Exit')

        op = int(input('Enter the option: '))

        if op == 1:
            hadoop_local_namenode()

        elif op == 2:
            hadoop_local_datanode()

        elif op == 3:
            break

        elif op == 4:
            exit()

        else:
            input("Invalid Value, Press Enter to Continue")
            continue


def hadoop_local_namenode():

    while True:
        os.system('clear')
        print('1. Start the namenode')
        print('2. Stop the namenode')
        print('3. Return to Main Menu')
        print('4. Exit')
        op = int(input('Select the option: '))

        if op == 1:
            os.system('systemctl stop firewall')
            os.system('hadoop-daemon.sh start namenode')
            os.system('hadoop dfsadmin -safemode leave')

        elif op == 2:
            os.system('systemctl stop firewall')
            os.system('hadoop-daemon.sh stop namenode')

        elif op == 3:
            break

        elif op == 4:
            exit()

        else:
            input("Invalid Value, Press Enter to Continue")
            continue


def hadoop_local_datanode():

    while True:
        os.system('clear')
        print('1. Start the datanode')
        print('2. Stop the datanode')
        print('3. Return to Main Menu')
        print('4. Exit')
        op = int(input('Select the option: '))

        if op == 1:
            os.system('systemctl stop firewall')
            os.system('hadoop-daemon.sh start datanode')

        elif op == 2:
            os.system('systemctl stop firewall')
            os.system('hadoop-daemon.sh stop datanode')

        elif op == 3:
            break

        elif op == 4:
            exit()

        else:
            input("Invalid Value, Press Enter to Continue")
            continue
