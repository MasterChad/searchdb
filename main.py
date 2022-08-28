# Les packages
import os
import random
import string

os.system("cls") # Clear cmd
print("""  ____                                 _       ____    ____  
 / ___|    ___    __ _   _ __    ___  | |__   |  _ \  | __ ) 
 \___ \   / _ \  / _` | | '__|  / __| | '_ \  | | | | |  _ \ 
  ___) | |  __/ | (_| | | |    | (__  | | | | | |_| | | |_) |
 |____/   \___|  \__,_| |_|     \___| |_| |_| |____/  |____/ 
                                                             
                    By Kzx aka Sale Gosse
\n\n\n\n\n\n\n\n\n\n\n\n""") # print de gros hackeur fou


chose = input("[*] Chose à chercher: ") # input pour savoir quoi chercher
print("\n\n\n\n") # sauts de lignes pour un peu de beauté




letters = string.ascii_lowercase
result_str = ''.join(random.choice(letters) for i in range(8))
## ces deux lignes génère une string random


print("Fichier de logs:\n"+result_str+".txt") ## indique le fichier de log


os.system("powershell.exe findstr /I "+chose+" D:\db1\*.* > "+result_str+".txt") ## N'oubliez pas de changer   D:\db1\   par le chemin de vos bases de données ! Attention à bien coller *.* après le \