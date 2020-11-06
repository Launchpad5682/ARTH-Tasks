from partition_lvm_static import partition_menu
from hadoop import hadoop


def main():

    print('Select the options to perform')
    print('1. AWS CLI')
    print('2. Hadoop')
    print('3. Modifying Storages')
    print('4. Docker')
    print('5. Web Server')

    main_var = int(input('Enter the option: '))

    while True:

        if main_var == 1:
            pass

        elif main_var == 2:
            hadoop.hadoop()

        elif main_var == 3:
            partition_menu.partition()

        elif main_var == 4:
            pass

        else:
            break


main()
