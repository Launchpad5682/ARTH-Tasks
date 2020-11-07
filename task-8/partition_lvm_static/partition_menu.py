import os

from partition_lvm_static.lvm_aka_elastic import lvm_local, lvm_remote
from partition_lvm_static.static_partition import static_local, static_remote


def partition():

    while True:
        os.system('clear')
        print('1. Static Partition')
        print('2. LVM Partition')
        print('3. Return to Main Menu')
        print('4. Exit')

        op = int(input('Enter the option: '))

        if op == 1:
            static()

        elif op == 2:
            LVM()

        elif op == 3:
            break

        elif op == 4:
            exit()

        else:
            return


def static():

    while True:
        os.system('clear')
        print('Do you want to perform Static partition ')
        print('1. Locally ?')
        print('2. Remotely ?')
        print('3. Return to Main Menu')
        print('4. Exit')

        op = int(input('Enter the option: '))

        if op == 1:
            static_local.static_local()

        elif op == 2:
            static_remote.static_remote()

        elif op == 3:
            break

        elif op == 4:
            exit()

        else:
            input("Invalid Value, Press Enter to Continue")
            continue


def LVM():

    while True:
        os.system('clear')
        print('Do you want to perform LVM partition ')
        print('1. Locally ?')
        print('2. Remotely ?')
        print('3. Return to Main Menu')
        print('4. Exit')

        op = int(input('Enter the option: '))

        if op == 1:
            lvm_local.LVM_local()

        elif op == 2:
            lvm_remote.LVM_remote()

        elif op == 3:
            break

        elif op == 4:
            exit()

        else:
            input("Invalid Value, Press Enter to Continue")
            continue
