from halo import Halo
import pyfiglet
import hashlib
import time,os,sys
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



flag = 0

def menu():
 print("""
 
 1. md5          6. SHA224             11. sha3_224        
 2. SHA1         7. blake2b            12. sha3_256        
 3. SHA256       8. blake2s            13. sha3_384        
 4. SHA384       9. shake_128          14. sha3_512        
 5. SHA512      10. shake_256          15. scrypt                 
 """)
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

elif selection==7:
 print("[-]blake2b is now selected[-]" )  
 print('\n')
 pass_hash = input(Fore.LIGHTYELLOW_EX+"ENTER blake2b HASH: ")
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
    digest = hashlib.blake2b(enc_wrd.strip()).hexdigest()
        
    if digest== pass_hash:
         print("\n")
         cprint("YOUR PASSWORD IS ",'green')
         cprint(word,'green' ,attrs=['bold'])
         flag = 1    
         break
 
 if flag ==0:
        cprint("PASSWORD NOT FOUND", 'red')

elif selection==8:
 print("[-]blake2s is now selected[-]" )  
 print('\n')
 pass_hash = input(Fore.LIGHTYELLOW_EX+"ENTER blake2s HASH: ")
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
    digest = hashlib.blake2s(enc_wrd.strip()).hexdigest()
        
    if digest== pass_hash:
         print("\n")
         cprint("YOUR PASSWORD IS ",'green')
         cprint(word,'green' ,attrs=['bold'])
         flag = 1    
         break
elif selection==12:
 cprint("[#]sha3_256 is now selected[#]",'white')
 print('\n')
 pass_hash = input(Fore.LIGHTYELLOW_EX+"ENTER sha3_356 HASH: ")
 wordlist = input("ENTER NAME OF THE FILE: ")

 try:
    pass_file = open (wordlist, "r")

 except:
    cprint("CANNOT FIND THE FILE YOU ARE LOOKING FOR ",'red')
    quit()
    
 for word in pass_file:
    
    enc_wrd = word.encode('utf-8')
    digest = hashlib.sha3_256(enc_wrd.strip()).hexdigest()
    
    if digest == pass_hash:
         print("Password found",'green')
         cprint("password is " + word,'green')
         flag = 1
         break
#md5()              

 if  flag ==0:
    cprint("Password not found")
    
elif selection==9:
 print("[-]shake_128 is now selected[-]" )   
 print('\n')
 pass_hash = input(Fore.LIGHTYELLOW_EX+"ENTER shake_128 HASH: ")
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
    digest = hashlib.shake_128(enc_wrd.strip()).hexdigest()
        
    if digest== pass_hash:
         print("\n")
         cprint("YOUR PASSWORD IS ",'green')
         cprint(word,'green' ,attrs=['bold'])
         flag = 1    
         break
 
 if flag ==0:
        cprint("PASSWORD NOT FOUND", 'red')
elif selection==11:
 cprint("[#]sha3_224 is now selected[#]",'white')
 print('\n')
 pass_hash = input(Fore.LIGHTYELLOW_EX+"ENTER sha3_224 HASH: ")
 wordlist = input("ENTER NAME OF THE FILE: ")

 try:
    pass_file = open (wordlist, "r")

 except:
    cprint("CANNOT FIND THE FILE YOU ARE LOOKING FOR ",'red')
    quit()
    
 for word in pass_file:
    
    enc_wrd = word.encode('utf-8')
    digest = hashlib.sha3_224(enc_wrd.strip()).hexdigest()
    
    if digest == pass_hash:
         print("Password found",'green')
         cprint("password is " + word,'green')
         flag = 1
         break
#md5()              

 if  flag ==0:
    cprint("Password not found")
    
elif selection==10:
 print("[-]shake_256 is now selected[-]" )   
 print('\n')
 pass_hash = input(Fore.LIGHTYELLOW_EX+"ENTER shake_256 HASH: ")
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
    digest = hashlib.shake_256(enc_wrd.strip()).hexdigest()
        
    if digest== pass_hash:
         print("\n")
         cprint("YOUR PASSWORD IS ",'green')
         cprint(word,'green' ,attrs=['bold'])
         flag = 1    
         break
 
 if flag ==0:
        cprint("PASSWORD NOT FOUND", 'red')

elif selection==13:
 print("[-]sha3_384 is now selected[-]" )   
 print('\n')
 pass_hash = input(Fore.LIGHTYELLOW_EX+"ENTER sha3_384 HASH: ")
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
    digest = hashlib.sha3_384(enc_wrd.strip()).hexdigest()
        
    if digest== pass_hash:
         print("\n")
         cprint("YOUR PASSWORD IS ",'green')
         cprint(word,'green' ,attrs=['bold'])
         flag = 1    
         break
 
 if flag ==0:
        cprint("PASSWORD NOT FOUND", 'red')

elif selection==14:
 print("[-]sha3_512 is now selected[-]" )   
 print('\n')
 pass_hash = input(Fore.LIGHTYELLOW_EX+"ENTER sha3_512 HASH: ")
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
    digest = hashlib.sha3_512(enc_wrd.strip()).hexdigest()
        
    if digest== pass_hash:
         print("\n")
         cprint("YOUR PASSWORD IS ",'green')
         cprint(word,'green' ,attrs=['bold'])
         flag = 1    
         break
 
 if flag ==0:
        cprint("PASSWORD NOT FOUND", 'red')

elif selection==15:
 print("[-]scrypt is now selected[-]" )   
 print('\n')
 pass_hash = input(Fore.LIGHTYELLOW_EX+"ENTER scrypt HASH: ")
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
    digest = hashlib.scrypt(enc_wrd.strip()).hexdigest()
        
    if digest== pass_hash:
         print("\n")
         cprint("YOUR PASSWORD IS ",'green')
         cprint(word,'green' ,attrs=['bold'])
         flag = 1    
         break
 
 if flag ==0:
        cprint("PASSWORD NOT FOUND", 'red')
