import os
# import getpass
# print("\t\t\tWelcome to AWS Automation")
# print("\t\t\t--------------------")

# password = getpass.getpass('Enter password : ')

# if password != "priya":
#     print('wrong password')
#     exit()

def configure_aws():
	print("Configure AWS")
	os.system('aws configure')

def key_pair():
	key = input('Enter key name you want to create : ')
	os.system('aws ec2 create-key-pair --key-name {}'.format(key))

def ec2():
	while True:
		os.system("clear")
		print("\n \n")
		print("""
		Press 1: To Describe EC2 Instance
		Press 2: To launch EC2 Instance
		Press 3: To stop EC2 Instance
		Press 4: To start EC2 Instance
		Press 5: To terminate EC2 Instance
		Press 6: Return to menu
		""")

        
		i = int(input("Enter ur choice : "))
		print(i)
		if i==1:
			Describe_ec2()
		elif i==2:
			launching_ec2()
		elif i==3:
			stopping_ec2()
		elif i==4:
			starting_ec2()
		elif i==5:
			terminate_ec2()
		elif i==6:
			return
		else:
			input("\n Invalid option, please press enter to continue")  
def s3():
	while True:
		os.system("clear")		
		print("\n \n")
		print("""
		Press 1: To create S3 bucket
		Press 2: To update the content in S3 bucket
		Press 3: To delete S3 bucket
		Press 4: To delete object from the bucket
		Press 5: Return to menu
		""")

        
		i = int(input("Enter ur choice : "))
		print(i)
		if i==1:
			s3bucket()
		elif i==2:
			s3content()
		elif i==3:
			s3delete()
		elif i==4:
			s3deleteobj()
		elif i==5:
			return
		else:
			input("\n Invalid option, please press enter to continue") 
 
def ebs():
	while True:
		os.system("clear")
		print("\n \n")
		print("""
		Press 1: To Create EBS storage
		Press 2: To describe EBS
		Press 3: To attach EBS
		Press 4: To detach EBS
		Press 5: To Delete the EBS
		Press 6: Create a SnapShot of EBS
		Press 7: Return to menu
		""")

        
		i = int(input("Enter ur choice : "))
		print(i)
		if i==1:
			Creating_ebs()
		elif i==2:
			Describe_ebs()
		elif i==3:
			Attaching_ebs()
		elif i==4:
			Detaching_ebs()
		elif i==5:
			Deleting_ebs()
		elif i==6:
			create_snapshot()
		elif i==7:
			return

		else:
			input("\n Invalid option, please press enter to continue") 

def sg():
	while True:
		os.system("clear")
		print("\n \n")
		print("""
		Press 1: To create Security group
		Press 2: To describe Security group
		Press 3: To add ingress to security group
		Press 4: To update egress to security group
		Press 5: To delete security group
		Press 6: Return to menu
		Press 7: To exit
		""")

        
		i = int(input("Enter ur choice : "))
		print(i)
		if i==1:
			Security_group()
		elif i==2:
			Describe_sg()
		elif i==3:
			Ingress()
		elif i==4:
			Egress()
		elif i==5:
			Deleting_sg()
		elif i==6:
			return
		elif i==7:
			exit()
		else:
			input("\n Invalid option, please press enter to continue") 

def create_snapshot():
	a=input("Enter Volume_ID: ")
	b=input("Enter The Description of This Snapshot: \n")
	os.system(f"aws ec2 create-snapshot --volume-id {a} --description {b}")
	input("\n \nTask Completed, Press Enter To continue")


def launching_ec2():
	a = input('Enter AMI_ID: ')
	i = input('Enter instance-type: ')
	c = int(input('Enter number of instance you want to launch: '))
	s = input('Enter subnet-ID: ')
	sg = input('Enter security-group: ')
	k = input('Enter key name: ')
	os.system('aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --security-group-ids {} --key-name {}'.format(a,i,c,s,sg,k))
	input("\n \nTask Completed, Press Enter To continue")
def Describe_ec2():
	os.system('aws ec2 describe-instances')
	input("\n \nTask Completed, Press Enter To continue")

def starting_ec2():
	a = input('Enter ami-id: ')
	os.system('aws ec2 start-instances --instance-ids {}'.format(a))
	input("\n \nTask Completed, Press Enter To continue")
	
def stopping_ec2():
	a = input('Enter ami-id: ')
	os.system('aws ec2 stop-instances --instance-ids {}'.format(a))
	input("\n \nTask Completed, Press Enter To continue")

def terminate_ec2():
	a = input('Enter ami-id: ')
	os.system('aws ec2 terminate-instances --instance-ids {}'.format(a))
	input("\n \nTask Completed, Press Enter To continue")

def Describe_ebs():
	os.system('aws ec2 describe-volumes')
	input("\n \nTask Completed, Press Enter To continue")

def Attaching_ebs():

	a = input('Enter instance-id: ')
	v = input('Enter volume-id: ')
	d = input('Enter device-name: ')
	os.system('aws ec2 attach-volume --instance-id {} --volume-id {} --device {}'.format(a,v,d))
	input("\n \nTask Completed, Press Enter To continue")


def Creating_ebs():
	t = input('Enter volume type eg. gp2: ')
	s = input('Enter volume-size: ')
	a = input('Enter availability-zone eg.ap-south-1a: ')
	os.system('aws ec2 create-volume --volume-type {} --size {} --availability-zone {}'.format(t,s,a))
	input("\n \nTask Completed, Press Enter To continue")

def Detaching_ebs():
	v = input('Enter volume-id: ')
	os.system('aws ec2 detach-volume --volume-id {}'.format(v))
	input("\n \nTask Completed, Press Enter To continue")


def Deleting_ebs():
	v = input('Enter volume-id: ')
	os.system('aws ec2 delete-volume --volume-id {}'.format(v))
	input("\n \nTask Completed, Press Enter To continue")

def Security_group():
	n = input('Enter security_group_name: ')
	d = input('Add description: ')
	v = input('Enter vcp_id: ')
	os.system('aws ec2 create-security-group --group-name {} --description "{}" --vpc-id {}'.format(n,d,v))
	input("\n \nTask Completed, Press Enter To continue")

def Describe_sg():
	i = input('Enter security_group_id: ')
	os.system('aws ec2 describe-security-groups --group-ids {}'.format(i))
	input("\n \nTask Completed, Press Enter To continue")

def Ingress():
	i = input('Enter security-group id: ')
	n = input('Enter security-group name: ')
	e = input('Enter protocol: ')
	p = int(input('Enter port number: '))
	c = input('Enter cidr-block: ')
	os.system('aws ec2 authorize-security-group-ingress --group-id {} --group-name {} --protocol {} --port {} --cidr {}'.format(i,n,e,p,c))
	input("\n \nTask Completed, Press Enter To continue")

def Egress():
	i = input('Enter security-group id: ')
	e = input('Enter protocol: ')
	p = int(input('Enter port number: '))
	c = input('Enter cidr-block: ')
	os.system('aws ec2 authorize-security-group-egress --group-id {}  --protocol {} --port {} --cidr {}'.format(i,e,p,c))
	input("\n \nTask Completed, Press Enter To continue")

def s3bucket():
	n = input('Enter a unique bucket name: ')
	r = input('Enter region: ')
	os.system('aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}'.format(n,r,r))
	input("\n \nTask Completed, Press Enter To continue")

def s3delete():
	n = input('Enter bucket name: ')
	r = input('Enter region: ')
	os.system('aws s3api delete-bucket --bucket {} --region {}'.format(n,r))
	input("\n \nTask Completed, Press Enter To continue")

def s3content():
	l = input('Enter local location: ')
	n = input('Enter bucket name: ')
	os.system('aws s3 sync "{}" s3://{}'.format(l,n))
	input("\n \nTask Completed, Press Enter To continue")

def s3deleteobj():
	n = input('Enter bucket-name: ')
	k = input('Enter key or pic: ')
	os.system('aws s3api delete-object --bucket {} --key {}'.format(n,k))
	input("\n \nTask Completed, Press Enter To continue")

def cloudfront():
	n = input('Enter bucket name: ')
	os.system('aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com'.format(n))
	input("\n \nTask Completed, Press Enter To continue")

def Deleting_sg():
	n = input('Enter security_group_id: ')
	os.system('aws ec2 delete-security-group --group-id {}'.format(n))
	input("\n \nTask Completed, Press Enter To continue")


