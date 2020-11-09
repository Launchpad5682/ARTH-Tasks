import os


def hadoop_client_remote():
    os.system('clear')

    print('I assume the Hadoop Client is already configured')
    print("You are in the remote mode -->")
    login = input('Enter the username@ip_address: ')

    while True:
        os.system('clear')

        print('1. List files in the hadoop cluster')
        print('2. List files in the directory')
        print('3. Upload file')
        print('4. Read the file')
        print('5. Download file')
        print('6. Delete the file')
        print('7. Use different user')
        print('8. Return to Main Menu')
        print('9. Exit')

        var = int(input('Enter the option: '))

        if var == 1:
            os.system("ssh {} hadoop fs -ls /".format(login))
            input('Press enter to continue')

        elif var == 2:
            dir = input('Enter the valid directory to list the contents: ')
            os.system('ssh {} ls {}'.format(login, dir))
            input('Press enter to continue')

        elif var == 3:
            print('Do you want to select the block size ?, Then press 1')
            ex = int(input("Enter the option, any other to use default: "))

            if ex == 1:
                block_size = int(('Enter the block size like 512M,1024K: '))
                file = input("Enter the filename with the complete path: ")
                os.system(
                    'ssh {} hadoop fs -Ddfs.block.size={} -put {} /' .format(login, block_size, file))
                os.system('sleep 5')

            else:
                file = input("Enter the filename with the complete path: ")
                os.system('ssh {} hadoop fs -put {} /'.format(login, file))
                os.system('sleep 5')

        elif var == 4:
            file = input("Enter the filename with the complete path: ")
            os.system('ssh {} hadoop fs -cat {}'.format(login, file))
            input('Press enter to continue')

        elif var == 5:
            file = input("Enter the filename with the complete path: ")
            os.system('ssh {} hadoop fs -get {}'.format(login, file))
            input('Press enter to continue')

        elif var == 6:
            file = input("Enter the filename with the complete path: ")
            os.system('ssh {} hadoop fs -rm {}'.format(login, file))
            input('Press enter to continue')

        elif var == 7:
            os.system('clear')
            hadoop_client_remote()

        elif var == 8:
            break

        elif var == 9:
            exit()

        else:
            input("Invalid Value, Press Enter to Continue")
            continue
