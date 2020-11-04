import os

print('Program to add/modify the Volume Group/ Logical Volume')
print('------------------------------------------------------')
print("1: Create Volume Group")
print('2: Create Logical Volume')
print('3: Mount the Volume')
print('4: Extend the Logical Volume')
print('5: Reduce the Logical volume')
print('6: Display the physical volumes')
print('7: Display the volume group')
print('8: Create the physical volume')
print('Enter any other code to quit')
code = int(input('Enter the code:'))

while(code >= 1 and code <= 8):
    
    os.system('clear')
    print('Program to add/modify the Volume Group/ Logical Volume')
    print('------------------------------------------------------')
    print("1: Create Volume Group")
    print('2: Create Logical Volume')
    print('3: Mount the Volume')
    print('4: Extend the Logical Volume')
    print('5: Reduce the Logical volume')
    print('6: Display the physical volumes')
    print('7: Display the volume group')
    print('8: Create the physical volume')
    print('Enter any other code to quit')

    
    if(code == 1):
        pv = input('Enter the physical volume names using space: ')
        vg_name = input('Enter the volume group name: ')
        os.system('vgcreate {} {}'.format(vg_name, pv))

    elif(code == 2):
        size = input('Enter the size of the partition with G,M,K: ')
        name = input('Enter the name of the partition: ')
        vg_name = input('Enter the name of the volumee group: ')
        os.system('lvcreate --size {} --name {} {}'.format(size,name,vg_name))
        os.system('udevadm settle')
    
    elif(code == 3):
        mount = input('Enter the directory to mount: ')
        partition = input('Enter the partition name to mount: ')
        os.system('mkfs.ext4 {}'.format(partition))
        os.system('mount {} {}'.format(partition,mount))

    elif(code == 4):
        size = input('Enter the size to extend: ')
        name = input('Enter the name of lv (eg: /dev/vg_name/lv_name): ')
        os.system('lvextend --size {} {}'.format(size,name))
        
    elif(code == 5):
        name = input('Enter the name of lv (eg: /dev/vg_name/lv_name): ')
        size = input('Enter the size to reduce: ')
        os.system('lvreduce --size {} {}'.format(size,name))

    elif(code == 6):
        os.system('fdisk -l')

    elif(code == 7):
        os.system('lvdisplay')

    elif(code == 8):
        pv = input('Enter the drive name to create physical volumes: ')
        os.system('pvcreate {}'.format(pv))
    else:
        os.system('clear')
        exit()
 
    code = int(input('Enter the code:'))
