import pyfiglet
from halo import Halo
import hashlib
import time,os,sys
import time
import requests
from colorama import init
from colorama import Fore, Back, Style
init()
import itertools as t
from termcolor import colored, cprint

os.system("clear")

print(pyfiglet.figlet_format('Hash PUP',justify="center",font="doom"))
cprint("""
CODED BY:berry-dev
GitHub: https://github.com/berry-dev/
""","blue",attrs=["bold"])

input("Press enter to continue: ")

os.system("clear")

print(Fore.LIGHTYELLOW_EX+""" 
[-] What do you want to do? [-]

1. Decrypt hashes into plain text
2. Generate a wordlist
3. Identify hashes
4. Help
""")

selection=int(input("Enter: " ))

if selection == 1:
 def menu():
     print("""
 
      (+)Select one hashing algorithm(+)

 1. md5          6. SHA224             11. sha3_224        
 2. SHA1         7. blake2b            12. sha3_256        
 3. SHA256       8. blake2s            13. sha3_384        
 4. SHA384       9. shake_128          14. sha3_512        
 5. SHA512      10. shake_256          15. scrypt                 
 """)
 menu()
 print("\n")

 selection=int(input("Enter: " ))
 flag = 0

 print ("\n")
 
 if selection == 1:
     cprint("md5 is now selected",'white')
      
     print ("\n")

     pass_hash = input(Fore.CYAN+"ENTER MD5 HASH: ")
     wordlist = input("ENTER NAME OF THE FILE: ")

     try:
        pass_file = open (wordlist, "r")
     
     except:
         cprint("CANNOT FIND THE FILE!! YOUR FILE SHOULD BE IN THE SAME DIRECTORY THAT YOU ARE RUNNING THIS PYTHON SCRIPT",'red')
         quit()
    
     for word in pass_file:

         enc_wrd = word.encode('utf-8')
         digest = hashlib.md5(enc_wrd.strip()).hexdigest()

         if digest == pass_hash:
             print("Your Password is",)
             cprint(word)
             flag = 1
             break

     if  flag ==0:
         cprint("password not found );")
 
 if selection == 2:
     cprint("sha1 is now selected",'white')
     
     print("\n")
     
     pass_hash = input(Fore.CYAN+"ENTER sha1 HASH: ")
     wordlist = input("ENTER NAME OF THE FILE: ")

     try:
        pass_file = open (wordlist, "r")
     
     except:
         cprint("CANNOT FIND THE FILE!! YOUR FILE SHOULD BE IN THE SAME DIRECTORY THAT YOU ARE RUNNING THIS PYTHON SCRIPT",'red')
         quit()
    
     for word in pass_file:

         enc_wrd = word.encode('utf-8')
         digest = hashlib.sha1(enc_wrd.strip()).hexdigest()

         if digest == pass_hash:
             print("Your Password is",)
             cprint(word)
             flag = 1
             break

     if  flag ==0:
         cprint("password not found );")

 if selection == 3:
     cprint("sha256 is now selected")

     print("\n")

     pass_hash = input(Fore.CYAN+"ENTER sha256 HASH: ")
     wordlist = input("ENTER NAME OF THE FILE: ")

     try:
        pass_file = open (wordlist, "r")
     
     except:
         cprint("CANNOT FIND THE FILE!! YOUR FILE SHOULD BE IN THE SAME DIRECTORY THAT YOU ARE RUNNING THIS PYTHON SCRIPT",'red')
         quit()
    
     for word in pass_file:

         enc_wrd = word.encode('utf-8')
         digest = hashlib.sha256(enc_wrd.strip()).hexdigest()

         if digest == pass_hash:
             print("Your Password is",)
             cprint(word)
             flag = 1
             break

     if  flag ==0:
         cprint("password not found );")

 if selection == 4:
     cprint("sha384 is now selected")

     print("\n")

     pass_hash = input(Fore.CYAN+"ENTER sha384 HASH: ")
     wordlist = input("ENTER NAME OF THE FILE: ")

     try:
        pass_file = open (wordlist, "r")
     
     except:
         cprint("CANNOT FIND THE FILE!! YOUR FILE SHOULD BE IN THE SAME DIRECTORY THAT YOU ARE RUNNING THIS PYTHON SCRIPT",'red')
         quit()
    
     for word in pass_file:

         enc_wrd = word.encode('utf-8')
         digest = hashlib.sha384(enc_wrd.strip()).hexdigest()

         if digest == pass_hash:
             print("Your Password is",)
             cprint(word)
             flag = 1
             break

     if  flag ==0:
         cprint("password not found );")
 
 if selection == 5:
     cprint("sha512 is now selected")
      
     print("\n")

     pass_hash = input(Fore.CYAN+"ENTER sha512 HASH: ")
     wordlist = input("ENTER NAME OF THE FILE: ")

     try:
        pass_file = open (wordlist, "r")
     
     except:
         cprint("CANNOT FIND THE FILE!! YOUR FILE SHOULD BE IN THE SAME DIRECTORY THAT YOU ARE RUNNING THIS PYTHON SCRIPT",'red')
         quit()
    
     for word in pass_file:

         enc_wrd = word.encode('utf-8')
         digest = hashlib.sha512(enc_wrd.strip()).hexdigest()

         if digest == pass_hash:
             print("Your Password is",)
             cprint(word)
             flag = 1
             break

     if  flag ==0:
         cprint("password not found );")

 if selection == 6:
     cprint("sha224 is now selected")

     print("\n")

     pass_hash = input(Fore.CYAN+"ENTER sha224 HASH: ")
     wordlist = input("ENTER NAME OF THE FILE: ")

     try:
        pass_file = open (wordlist, "r")
     
     except:
         cprint("CANNOT FIND THE FILE!! YOUR FILE SHOULD BE IN THE SAME DIRECTORY THAT YOU ARE RUNNING THIS PYTHON SCRIPT",'red')
         quit()
    
     for word in pass_file:

         enc_wrd = word.encode('utf-8')
         digest = hashlib.sha224(enc_wrd.strip()).hexdigest()

         if digest == pass_hash:
             print("Your Password is",)
             cprint(word)
             flag = 1
             break

     if  flag ==0:
         cprint("password not found );")

 if selection == 7:
     cprint("blake2b is now selected")

     print("\n")

     pass_hash = input(Fore.CYAN+"ENTER blake2b HASH: ")
     wordlist = input("ENTER NAME OF THE FILE: ")

     try:
        pass_file = open (wordlist, "r")
     
     except:
         cprint("CANNOT FIND THE FILE!! YOUR FILE SHOULD BE IN THE SAME DIRECTORY THAT YOU ARE RUNNING THIS PYTHON SCRIPT",'red')
         quit()
    
     for word in pass_file:

         enc_wrd = word.encode('utf-8')
         digest = hashlib.blake2b(enc_wrd.strip()).hexdigest()

         if digest == pass_hash:
             print("Your Password is",)
             cprint(word)
             flag = 1
             break

     if  flag ==0:
         cprint("password not found );")

 if selection == 8:
     cprint("blake2s is now selected")

     print("\n")

     pass_hash = input(Fore.CYAN+"ENTER blake2s HASH: ")
     wordlist = input("ENTER NAME OF THE FILE: ")

     try:
        pass_file = open (wordlist, "r")
     
     except:
         cprint("CANNOT FIND THE FILE!! YOUR FILE SHOULD BE IN THE SAME DIRECTORY THAT YOU ARE RUNNING THIS PYTHON SCRIPT",'red')
         quit()
    
     for word in pass_file:

         enc_wrd = word.encode('utf-8')
         digest = hashlib.blake2s(enc_wrd.strip()).hexdigest()

         if digest == pass_hash:
             print("Your Password is",)
             cprint(word)
             flag = 1
             break

     if  flag ==0:
         cprint("password not found );")

 if selection == 9:
     cprint("shake_128 is now selected")

     print("\n")

     pass_hash = input(Fore.CYAN+"ENTER shake_128 HASH: ")
     wordlist = input("ENTER NAME OF THE FILE: ")

     try:
        pass_file = open (wordlist, "r")
     
     except:
         cprint("CANNOT FIND THE FILE!! YOUR FILE SHOULD BE IN THE SAME DIRECTORY THAT YOU ARE RUNNING THIS PYTHON SCRIPT",'red')
         quit()
    
     for word in pass_file:

         enc_wrd = word.encode('utf-8')
         digest = hashlib.shake_128(enc_wrd.strip()).hexdigest()

         if digest == pass_hash:
             print("Your Password is",)
             cprint(word)
             flag = 1
             break

     if  flag ==0:
         cprint("password not found );")
        
 if selection == 10:
     cprint("shake_256 is now selected")

     print("\n")

     pass_hash = input(Fore.CYAN+"ENTER shake_256 HASH: ")
     wordlist = input("ENTER NAME OF THE FILE: ")

     try:
        pass_file = open (wordlist, "r")
     
     except:
         cprint("CANNOT FIND THE FILE!! YOUR FILE SHOULD BE IN THE SAME DIRECTORY THAT YOU ARE RUNNING THIS PYTHON SCRIPT",'red')
         quit()
    
     for word in pass_file:

         enc_wrd = word.encode('utf-8')
         digest = hashlib.shake_256(enc_wrd.strip()).hexdigest()

         if digest == pass_hash:
             print("Your Password is",)
             cprint(word)
             flag = 1
             break

     if  flag ==0:
         cprint("password not found );")

 if selection == 11:
     cprint("sha3_224 is now selected")
     print("\n")

     pass_hash = input(Fore.CYAN+"ENTER sha3_224 HASH: ")
     wordlist = input("ENTER NAME OF THE FILE: ")

     try:
        pass_file = open (wordlist, "r")
     
     except:
         cprint("CANNOT FIND THE FILE!! YOUR FILE SHOULD BE IN THE SAME DIRECTORY THAT YOU ARE RUNNING THIS PYTHON SCRIPT",'red')
         quit()
    
     for word in pass_file:

         enc_wrd = word.encode('utf-8')
         digest = hashlib.sha3_224(enc_wrd.strip()).hexdigest()

         if digest == pass_hash:
             print("Your Password is",)
             cprint(word)
             flag = 1
             break

     if  flag ==0:
         cprint("password not found );")

 if selection == 12:
     cprint("sha3_256 is now selected")

     print("\n")

     pass_hash = input(Fore.CYAN+"ENTER sha3_256 HASH: ")
     wordlist = input("ENTER NAME OF THE FILE: ")

     try:
        pass_file = open (wordlist, "r")
     
     except:
         cprint("CANNOT FIND THE FILE!! YOUR FILE SHOULD BE IN THE SAME DIRECTORY THAT YOU ARE RUNNING THIS PYTHON SCRIPT",'red')
         quit()
    
     for word in pass_file:

         enc_wrd = word.encode('utf-8')
         digest = hashlib.sha3_256(enc_wrd.strip()).hexdigest()

         if digest == pass_hash:
             print("Your Password is",)
             cprint(word)
             flag = 1
             break

     if  flag ==0:
         cprint("password not found );")
        
 if selection == 13:
     cprint("sha3_384 is now selected")
     
     print("\n")
     
     pass_hash = input(Fore.CYAN+"ENTER sha3_384 HASH: ")
     wordlist = input("ENTER NAME OF THE FILE: ")

     try:
        pass_file = open (wordlist, "r")
     
     except:
         cprint("CANNOT FIND THE FILE!! YOUR FILE SHOULD BE IN THE SAME DIRECTORY THAT YOU ARE RUNNING THIS PYTHON SCRIPT",'red')
         quit()
    
     for word in pass_file:

         enc_wrd = word.encode('utf-8')
         digest = hashlib.sha3_384(enc_wrd.strip()).hexdigest()

         if digest == pass_hash:
             print("Your Password is",)
             cprint(word)
             flag = 1
             break

     if  flag ==0:
         cprint("password not found );")

 if selection == 14:
     cprint("sha3_512 is now selected")

     print("\n")

     pass_hash = input(Fore.CYAN+"ENTER sha3_512 HASH: ")
     wordlist = input("ENTER NAME OF THE FILE: ")

     try:
        pass_file = open (wordlist, "r")
     
     except:
         cprint("CANNOT FIND THE FILE!! YOUR FILE SHOULD BE IN THE SAME DIRECTORY THAT YOU ARE RUNNING THIS PYTHON SCRIPT",'red')
         quit()
    
     for word in pass_file:

         enc_wrd = word.encode('utf-8')
         digest = hashlib.sha3_512(enc_wrd.strip()).hexdigest()

         if digest == pass_hash:
             print("Your Password is",)
             cprint(word)
             flag = 1
             break

     if  flag ==0:
         cprint("password not found );")

 if selection == 15:
     cprint("scrypt is now selected")

     print("\n")

     pass_hash = input(Fore.CYAN+"ENTER scrypt HASH: ")
     wordlist = input("ENTER NAME OF THE FILE: ")

     try:
        pass_file = open (wordlist, "r")
     
     except:
         cprint("CANNOT FIND THE FILE!! YOUR FILE SHOULD BE IN THE SAME DIRECTORY THAT YOU ARE RUNNING THIS PYTHON SCRIPT",'red')
         quit()
    
     for word in pass_file:

         enc_wrd = word.encode('utf-8')
         digest = hashlib.scrypt(enc_wrd.strip()).hexdigest()

         if digest == pass_hash:
             print("Your Password is",)
             cprint(word)
             flag = 1
             break

     if  flag ==0:
         cprint("password not found );")
            
elif selection == 2:
   
    min = int(input(Fore.CYAN+"\n""Enter minimum length: "))
    max = int(input("Enter maximum length: "))
    
    chars = input(Fore.YELLOW+"\n""Enter the magical word: ")
    output = input("Enter the new file name: ")
 
    if output == "" or output is None:
        file = open(chars+".txt", "w")
    
    else:
        file = open(output, "w")
  
    if min == max:
        for a in t.product(chars, repeat= min):
            s = "".join(a)
            file.write(s+"\n")
        
        file.close()
    
    elif min < max:
        for i in range(min, max + 1):
            for a in t.product(chars, repeat= i):
                s ="".join(a)
                file.write(s+"\n")
        file.close()
        print("\n""wordlist created without any error")
    else:
        quit()

elif selection == 3:
    print("under maintenance")

elif selection == 4:
    print("\n" """
    ($) Hashpup uses hashlib to crack hashes to plain text, currently there are 15 algorithms (popular ones)
    ($) To get the plain text u need to enter the hash and wordlist. if the wordlist contains the hash password 
    ($) then it will say the password but if it doesn't then it will show "Password not found"

    ($) If you are facing problems entering the wordlist then your wordlist must be in the same directory as you
    ($) are running this script only enter the name of .txt file (dont specify the path).

    ($) For generating a wordlist dont enter too much of words it can kill your pc press CTRL+C to stop it the
        output file will be in the same directory you are running this script.

                            
                            
                            --THANK YOU FOR READING FOLLOW MY GITHUB TO KNOW MORE --
    """)



