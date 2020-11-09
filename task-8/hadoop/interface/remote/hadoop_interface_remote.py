import os


def hadoop_interface_remote():

    while True:
        os.system('clear')
        print("You are in Remote execution console-->")

        login = input('Enter the username@ip_address: ')

        print('Select whether node is ')
        print('1. Namenode')
        print('2. Datanode')
        print('3. Return to Main Menu')
        print('4. Exit')

        op = int(input('Enter the option: '))

        if op == 1:
            hadoop_remote_namenode(login)

        elif op == 2:
            hadoop_remote_datanode(login)

        elif op == 3:
            break

        elif op == 4:
            exit()

        else:
            input("Invalid Value, Press Enter to Continue")
            continue


def hadoop_remote_namenode(login):

    while True:
        os.system('clear')
        print('1. Start the namenode')
        print('2. Stop the namenode')
        print('3. Return to Main Menu')
        print('4. Exit')
        op = int(input('Select the option: '))

        if op == 1:
            os.system(
                f"""ssh {login} hadoop-daemon.sh start namenode &&
                    ssh {login} hadoop dfsadmin - safemode leave""")
            print('Namenode Started')
            os.system('sleep 5')

        elif op == 2:
            os.system(
                f"""ssh {login} hadoop-daemon.sh stop namenode""")
            print('Namenode Stopped')
            os.system('sleep 5')

        elif op == 3:
            break

        elif op == 4:
            exit()

        else:
            input("Invalid Value, Press Enter to Continue")
            continue


def hadoop_remote_datanode(login):

    while True:
        os.system('clear')
        print('1. Start the datanode')
        print('2. Stop the datanode')
        print('3. Return to Main Menu')
        print('4. Exit')
        op = int(input('Select the option: '))

        if op == 1:
            os.system(f'ssh {login} hadoop-daemon.sh start datanode')
            print('Datanode Started')
            os.system('sleep 5')

        elif op == 2:
            os.system(f'ssh {login} hadoop-daemon.sh stop datanode')
            print('Datanode Stopped')
            os.system('sleep 5')

        elif op == 3:
            break

        elif op == 4:
            exit()

        else:
            input("Invalid Value, Press Enter to Continue")
            continue
