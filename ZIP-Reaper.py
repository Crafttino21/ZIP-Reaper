import os
import time
from colorama import Fore
import zipfile
from datetime import datetime






time_now = datetime.now().strftime("%H:%M:%S")


banner = '''


███████╗██╗██████╗       ██████╗ ███████╗ █████╗ ██████╗ ███████╗██████╗ 
╚══███╔╝██║██╔══██╗      ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗
  ███╔╝ ██║██████╔╝█████╗██████╔╝█████╗  ███████║██████╔╝█████╗  ██████╔╝
 ███╔╝  ██║██╔═══╝ ╚════╝██╔══██╗██╔══╝  ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
███████╗██║██║           ██║  ██║███████╗██║  ██║██║     ███████╗██║  ██║
╚══════╝╚═╝╚═╝           ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                         
                      * ZIP-Reaper By WeepingAngel *
                    a simple tool to crack .zip file password :)
            Hack The Planet >:) | GitHub: https://www.github.com/Crafttino21 

'''


print(Fore.LIGHTMAGENTA_EX + banner)
print("Eating some cookies...")
time.sleep(5)
zit = input("enter the name of the zip file > ")
ps = input("enter name of your passlist > ")
print("Start Cracking..")






def extrractFile(zfile, password):
    try:
        zfile.extractall(pwd=bytes(password, 'utf-8'))
        return password
    except:
        print("Wrong Password Hash: " + time_now)
        return

def main():
    zfile = zipfile.ZipFile(zit)
    passFile = open(ps)
    for line in passFile.readlines():
        password = line.strip('\n')
        guess = extrractFile(zfile, password)
        if guess:
            print("Password cracked at " + time_now + " The Password is: " + password)
            break




if __name__ == '__main__':
    main()