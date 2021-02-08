from halo import Halo
import pyfiglet, PIL.Image
import hashlib
import time,os,sys
from multiprocessing import Pool
import time
from colorama import init
from colorama import Fore, Back, Style
init()
from termcolor import colored, cprint


print(pyfiglet.figlet_format('Hash Pup',justify="center",font="small"))

def f(x):
    time.sleep()
    return x

spinner=Halo (text="Loading please wait", spinner = "dots")
spinner.start()
time.sleep(3)
spinner.stop()
    
print(Style.BRIGHT+Fore.GREEN+"[*]Select any one hashing algorithm[*]")

import hashlib

flag = 0

print("\n")
def menu():
 
 cprint("1. md5",'green',attrs=['bold', 'blink'])
 cprint("2. SHA1",'green',attrs=['bold', 'blink'])
 cprint("3. SHA256",'green',attrs=['bold', 'blink'])
 cprint("4. SHA384",'green',attrs=['bold', 'blink'])
 cprint("5. SHA512",'green',attrs=['bold', 'blink'])
 cprint("6. SHA224",'green',attrs=['bold', 'blink'])
menu()

print("\n")

selection=int(input("Enter: " ))
print("\n")

if selection==1:
 cprint("[#]md5 is now selected[#]",'white')
 print('\n')
 pass_hash = input(Fore.LIGHTYELLOW_EX+"ENTER MD5 HASH: ")
 wordlist = input("ENTER NAME OF THE FILE: ")

 try:
    pass_file = open (wordlist, "r")

 except:
    cprint("CANNOT FIND THE FILE YOU ARE LOOKING FOR ",'red')
    quit()
    
 for word in pass_file:
    
    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()
    
    if digest == pass_hash:
         print("Password found",'green')
         cprint("password is " + word,'green')
         flag = 1
         break
#md5()          

 if  flag ==0:
    cprint("Password not found") 
     
elif selection==3:
 cprint("[#]SHA256 is now selected[#]",'white')
 print('\n')
 pass_hash = input(Fore.LIGHTYELLOW_EX+"ENTER SHA256 HASH: ")
 wordlist = input("ENTER NAME OF THE FILE: ")

 try:
    pass_file = open (wordlist, "r")

 except:
    cprint("CANNOT FIND THE FILE YOU ARE LOOKING FOR ",'red')
    quit()
    
 for word in pass_file:
    
    enc_wrd = word.encode('utf-8')
    digest = hashlib.sha256(enc_wrd.strip()).hexdigest()
    
    if digest == pass_hash:
         print("Password found",'green')
         cprint("password is " + word,'green')
         flag = 1
         break
#md5()              

 if  flag ==0:
    cprint("Password not found")
    
elif selection==2:
 print("[-]SHA1 is now selected[-]" )   
 print('\n')
 pass_hash = input(Fore.LIGHTYELLOW_EX+"ENTER SHA1 HASH: ")
 print('\n')
 wordlist = input(Fore.LIGHTYELLOW_EX+"Enter name of the file: ")


 try: 
    pass_file = open (wordlist, "r")

 except:
     print("\n")
     cprint(Fore.RED+"CANNOT FIND THE FILE YOU ARE LOKING FOR")
     quit()

 for word in pass_file:
        
    enc_wrd = word.encode('utf-8')
    digest = hashlib.sha1(enc_wrd.strip()).hexdigest()
        
    if digest== pass_hash:
         print("\n")
         cprint("YOUR PASSWORD IS ",'green')
         cprint(word,'green' ,attrs=['bold'])
         flag = 1    
         break
 
 if flag ==0:
        cprint("PASSWORD NOT FOUND", 'red')

elif selection==4:
 print("[-]SHA384 is now selected[-]" )  
 print('\n')
 pass_hash = input(Fore.LIGHTYELLOW_EX+"ENTER SHA384 HASH: ")
 print('\n')
 wordlist = input(Fore.LIGHTYELLOW_EX+"Enter name of the file: ")


 try: 
    pass_file = open (wordlist, "r")

 except:
     print("\n")
     cprint(Fore.RED+"CANNOT FIND THE FILE YOU ARE LOKING FOR")
     quit()

 for word in pass_file:
        
    enc_wrd = word.encode('utf-8')
    digest = hashlib.sha384(enc_wrd.strip()).hexdigest()
        
    if digest== pass_hash:
         print("\n")
         cprint("YOUR PASSWORD IS ",'green')
         cprint(word,'green' ,attrs=['bold'])
         flag = 1    
         break
 
 if flag ==0:
        cprint("PASSWORD NOT FOUND", 'red')
elif selection==5:
 print("[-]SHA512 is now selected[-]" )  
 print('\n')
 pass_hash = input(Fore.LIGHTYELLOW_EX+"ENTER SHA512 HASH: ")
 print('\n')
 wordlist = input(Fore.LIGHTYELLOW_EX+"Enter name of the file: ")


 try: 
    pass_file = open (wordlist, "r")

 except:
     print("\n")
     cprint(Fore.RED+"CANNOT FIND THE FILE YOU ARE LOKING FOR")
     quit()

 for word in pass_file:
        
    enc_wrd = word.encode('utf-8')
    digest = hashlib.sha512(enc_wrd.strip()).hexdigest()
        
    if digest== pass_hash:
         print("\n")
         cprint("YOUR PASSWORD IS ",'green')
         cprint(word,'green' ,attrs=['bold'])
         flag = 1    
         break
 
 if flag ==0:
        cprint("PASSWORD NOT FOUND", 'red')

elif selection==6:
 print("[-]SHA224 is now selected[-]" )  
 print('\n')
 pass_hash = input(Fore.LIGHTYELLOW_EX+"ENTER SHA224 HASH: ")
 print('\n')
 wordlist = input(Fore.LIGHTYELLOW_EX+"Enter name of the file: ")


 try: 
    pass_file = open (wordlist, "r")

 except:
     print("\n")
     cprint(Fore.RED+"CANNOT FIND THE FILE YOU ARE LOKING FOR")
     quit()

 for word in pass_file:
        
    enc_wrd = word.encode('utf-8')
    digest = hashlib.sha224(enc_wrd.strip()).hexdigest()
        
    if digest== pass_hash:
         print("\n")
         cprint("YOUR PASSWORD IS ",'green')
         cprint(word,'green' ,attrs=['bold'])
         flag = 1    
         break
 
 if flag ==0:
        cprint("PASSWORD NOT FOUND", 'red')



    