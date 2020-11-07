import os
from AWS import awsauto
# from awsauto import key_pair,ec2,ebs,sg,s3,cloudfront,configure_aws

def hello_from_aws():
    flag=False
    while True:
        os.system("clear")
        print("""
            Press 0: To configure AWS
            Press 1: To create a Key Pair
            Press 2: To configure EC2 instance
            Press 3: To configure EBS
            Press 4: To configure Security Group
            Press 5: To configure S3 bucket
            Press 6: To configure CloudFront
            Press 7: To Return to Main Menu
            Press 8: To Exit
            """)

        i = int(input("Enter ur choice : "))
        print(i)
        if i==0:
            awsauto.configure_aws()
        if i == 1:
            awsauto.key_pair()
        if i == 2:
            awsauto.ec2()
        if i == 3:
            awsauto.ebs()
        if i == 4:
            awsauto.sg()
        if i == 5:
            awsauto.s3()
        if i == 6:
            awsauto.cloudfront()
        if i == 7:
            break
        if i == 8:
            exit()
        
        

        else:
            input("Incorrect Option, please Press Enter")
            continue
    if flag:
        return

