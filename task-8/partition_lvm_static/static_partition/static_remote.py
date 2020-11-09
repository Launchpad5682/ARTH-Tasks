import os


def static_remote():
    print("You are in Remote execution console-->")

    login = input('Enter the username@ip_address: ')

    os.system('sleep 5')

    while True:
        os.system('clear')
        print("1: Create Partition")
        print('2: Format and Mount the Volume')
        print('3: Display the physical volumes')
        print('4. Change the user')
        print('5. Return to Main Menu')
        print('6. Exit')

        code = int(input('Enter the code:'))

        if code == 1:
            drive_name = input('Enter the disk name: ')
            os.system('ssh {} fdisk {}'.format(login, drive_name))
            os.system('ssh {} udevadm settle'.format(login))
            input('enter to continue ')

        elif code == 2:
            mount = input('Enter the directory to mount: ')
            partition = input('Enter the partition name to mount: ')
            os.system('ssh {} mkfs.ext4 {}'.format(login, partition))
            os.system('ssh {} mount {} {}'.format(login, partition, mount))
            input('enter to continue ')

        elif code == 3:
            os.system('ssh {} fdisk -l'.format(login))
            input('enter to continue ')

        elif code == 4:
            os.system('clear')
            static_remote()

        elif code == 5:
            break

        elif code == 6:
            exit()

        else:
            input("Invalid Value, Press Enter to Continue")
            continue
