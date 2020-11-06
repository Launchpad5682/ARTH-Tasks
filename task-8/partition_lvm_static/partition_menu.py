import os

from partition_lvm_static.lvm_aka_elastic import lvm_local, lvm_remote
from partition_lvm_static.static_partition import static_partition


def partition():

    while True:
        print('1. Static Partition')
        print('2. LVM Partition')
        op = int(input('Enter the option: '))

        if op == 1:
            static()

        elif op == 2:
            LVM()

        else:
            return


def static():

    while True:
        print('Do you want to perform Static partition ')
        print('1. Locally ?')
        print('2. Remotely ?')

        op = int(input('Enter the option: '))

        if op == 1:
            pass

        elif op == 2:
            pass

        else:
            return


def LVM():

    while True:
        print('Do you want to perform LVM partition ')
        print('1. Locally ?')
        print('2. Remotely ?')

        op = int(input('Enter the option: '))

        if op == 1:
            lvm_local.LVM_local()

        elif op == 2:
            lvm_remote.LVM_remote()

        else:
            return
