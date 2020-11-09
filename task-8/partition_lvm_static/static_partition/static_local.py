import os


def static_local():
    print("You are in Local execution console-->")

    os.system('sleep 5')

    while True:
        os.system('clear')
        print("1: Create Partition")
        print('2: Format and Mount the Volume')
        print('3: Display the physical volumes')
        print('4. Return to Main Menu')
        print('5. Exit')

        code = int(input('Enter the code:'))

        if code == 1:
            drive_name = input('Enter the disk name: ')
            os.system('fdisk {}'.format(drive_name))
            os.system('udevadm settle')
            input('enter to continue ')

        elif code == 2:
            mount = input('Enter the directory to mount: ')
            partition = input('Enter the partition name to mount: ')
            os.system('mkfs.ext4 {}'.format(partition))
            os.system('mount {} {}'.format(partition, mount))
            input('enter to continue ')

        elif code == 3:
            os.system('fdisk -l')
            input('enter to continue ')

        elif code == 4:
            break

        elif code == 5:
            exit()

        else:
            input("Invalid Value, Press Enter to Continue")
            continue
