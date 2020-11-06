import os
from partition_lvm_or_static.lvm_aka_elastic import *
from partition_lvm_or_static.static import static_partition

def partition():

    while True:
        print('Do you want to perform LVM partition ')
        print('1. Locally ?')
        print('2. Remotely ?')

        op = int(input('Enter the option: '))

        if op == 1:
            partition_local()

        elif op == 2:
            partition_remote()


def partition_local():
    pass




def static_partition_local():
    pass


def partition_remote():
    pass
