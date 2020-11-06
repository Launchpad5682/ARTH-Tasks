import os
# import getpass

# os.system("tput setaf 3")
# print("\t\t\t Welcome to our Menu")
# os.system("tput setad 7")
# print("\t\t\t -------------")

# password = getpass.getpass("Enter your password to continue")

# if password!="arth":
#     print("Password is incorrect")
#     exit()


def hello():
    while True:
        os.system("clear")
        print("""
        1. Starting the Python Interpreter 
        2. Start the Apache Web Server
        3. Return to Main Menu
        4. Exit
        """)
        option = int(input("Enter your Choice\n"))
        if option == 1:
            envi = input("Where do you want to run this python interpreter? container/local \n")
            if(envi == "container"):
                os.system("clear")
                cd=os.getcwd()
                os_name = input("Enter the name of the container ")
                os.chdir("docker_task/docker_python_task")
                os.system("docker build -t python_repl:v1 .")
                print("Now you can proceed ahead with the docker container set up")
                print(" \n \n Your Container Is setup , you can start it with Python3")
                os.system(f"docker container run -it --name {os_name} python_repl:v1")
                os.system(f"docker container stop {os_name}")
                os.system(f"docker system prune --force")
                os.chdir(cd)
                input("Task Completed, press Enter To Continue")
                continue
            elif(envi == "local"):
                os.system(f"yum -y install python3")
                os.system(f"python3")
        if(option == 2):
            envi = input("Where do you want to run this web Server? container/local\n")
            if(envi == "container"):
                os.system("clear")
                cd=os.getcwd()
                os_name = input("Enter the name of the container ")
                os.chdir("docker_task/web_server_task")
                print("Now you can proceed ahead with the docker container set up")
                os.system("docker build -t myrepl:v1 .")
                print(" \n \n Your Container Is setup , you can start the web Server with /usr/sbin/httpd")
                os.system(f"docker container run -it --name {os_name} myrepl:v1")
                os.system(f"docker container stop {os_name}")
                os.system(f"docker system prune --force")
                os.chdir(cd)
                input("Task Completed, press Enter To Continue")
                continue
            if(envi == "local"):
                os.system("yum -y install httpd")
                os.system(f"systemctl start httpd")
        if(option == 3):
            break
        if(option == 4):
            exit()
        else:
            input("Invalid Value, Press Enter to Continue")
            continue

