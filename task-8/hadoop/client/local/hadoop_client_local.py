import os


def hadoop_client_local():
    print('I assume the Hadoop Client is already configured')
    print("You are in the local mode -->")

    os.system('sleep 10')

    while True:
        os.system('clear')
        print('1. List files in the hadoop cluster')
        print('2. List files in the directory')
        print('3. Upload file')
        print('4. Read the file')
        print('5. Download file')
        print('6. Delete the file')
        print('7. Return to Main Menu')
        print('8. Exit')

        var = int(input('Enter the option: '))

        if var == 1:
            os.system('hadoop fs -ls /')

        elif var == 2:
            dir = input('Enter the valid directory to list the contents: ')
            os.system('ls {}'.format(dir))

        elif var == 3:
            print('Do you want to select the block size ?, Then press 1')
            ex = int(input("Enter the option, any other to use default: "))

            if ex == 1:
                block_size = int(('Enter the block size like 512M,1024K: '))
                file = input("Enter the filename with the complete path: ")
                os.system(
                    'hadoop fs -Ddfs.block.size={} -put {}' .format(block_size, file))

            else:
                file = input("Enter the filename with the complete path: ")
                os.system('hadoop fs -put {}'.format(file))

        elif var == 4:
            file = input("Enter the filename with the complete path: ")
            os.system('hadoop fs -cat {}'.format(file))

        elif var == 5:
            file = input("Enter the filename with the complete path: ")
            os.system('hadoop fs -get {}'.format(file))

        elif var == 6:
            file = input("Enter the filename with the complete path: ")
            os.system('hadoop fs -rm {}'.format(file))

        elif var == 7:
            break

        elif var == 8:
            exit()

        else:
            input("Invalid Value, Press Enter to Continue")
            continue
