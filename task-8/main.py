# from partition import partition
from hadoop import hadoop_setup
from script import hello
def main():

    print('Select the options to perform')
    print('1. AWS CLI')
    print('2. Hadoop')
    print('3. Modifying Storages')
    print('4. Docker and Web Server')

    main_var = int(input('Enter the option: '))

    while True:

        if main_var == 1:
            pass

        elif main_var == 2:
            hadoop_setup.hadoop()

        # elif main_var == 3:
        #     partition.partition()

        elif main_var == 4:
            hello()
            

        else:
            break


main()
