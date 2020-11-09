import os


def LVM_remote():

    print("You are in Remote execution console-->")

    login = input('Enter the username@ip_address: ')

    os.system('sleep 5')

    while True:
        os.system('clear')
        print("1: Create Volume Group")
        print('2: Create Logical Volume')
        print('3: Mount the Volume')
        print('4: Extend the Logical Volume')
        print('5: Reduce the Logical volume')
        print('6: Display the physical volumes')
        print('7: Display the volume group')
        print('8: Create the physical volume')
        print('9. Change the user')
        print('10. Return to Main Menu')
        print('11. Exit')

        code = int(input('Enter the code:'))

        if(code == 1):
            pv = input('Enter the physical volume names using space: ')
            vg_name = input('Enter the volume group name: ')
            os.system('ssh {} vgcreate {} {}'.format(login, vg_name, pv))
            input('enter to continue ')

        elif(code == 2):
            size = input('Enter the size of the partition with G,M,K: ')
            name = input('Enter the name of the partition: ')
            vg_name = input('Enter the name of the volumee group: ')
            os.system(
                'ssh {} lvcreate --size {} --name {} {}'.format(login, size, name, vg_name))
            os.system('ssh {} udevadm settle'.format(login))
            input('enter to continue ')

        elif(code == 3):
            mount = input('Enter the directory to mount: ')
            partition = input('Enter the partition name to mount: ')
            os.system('ssh {} mkfs.ext4 {}'.format(login, partition))
            os.system('ssh {} mount {} {}'.format(login, partition, mount))
            input('enter to continue ')

        elif(code == 4):
            size = input('Enter the size to extend: ')
            name = input('Enter the name of lv (eg: /dev/vg_name/lv_name): ')
            os.system('ssh {} lvextend --size {} {}'.format(login, size, name))
            input('enter to continue ')

        elif(code == 5):
            name = input('Enter the name of lv (eg: /dev/vg_name/lv_name): ')
            size = input('Enter the size to reduce: ')
            os.system('ssh {} lvreduce --size {} {}'.format(login, size, name))
            input('enter to continue ')

        elif(code == 6):
            os.system('ssh {} fdisk -l'.format(login))
            input('enter to continue ')

        elif(code == 7):
            os.system('ssh {} lvdisplay'.format(login))
            input('enter to continue ')

        elif(code == 8):
            pv = input('Enter the drive name to create physical volumes: ')
            os.system('ssh {} pvcreate {}'.format(login, pv))
            input('enter to continue ')

        elif code == 9:
            os.system('clear')
            LVM_remote()

        elif code == 10:
            break

        elif code == 11:
            exit()

        else:
            input("Invalid Value, Press Enter to Continue")
            continue
