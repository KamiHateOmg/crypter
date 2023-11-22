#//////////////////////////////////////////////////////////////////////////////
# Code by Kami (arnaqueurs on discord)
# 21/11/23 (21:30)
# Coded with my heart <3
#//////////////////////////////////////////////////////////////////////////////



from pystyle import *
import os
import subprocess
from colorama import *
import time
from cryptography.fernet import Fernet

def mt(titre):
    if os.name == 'nt':
        os.system(f"title {titre}")
    else:
        print("La modification du titre de la console n'est pas supportée sur ce système d'exploitation.")


titre = "KamiCrypt"
mt(titre)

os.system('clear' if os.name == 'posix' else 'cls')

def clearing():
    os.system('cls' if os.name == 'nt' else 'clear')

def gen_key():
    key = Fernet.generate_key()
    key_edit = key + b'_KAMI_'
    return key_edit

def save_key(key, name_f):
    with open(name_f, 'wb') as f:
        f.write(key)

def take_key(name_f):
    with open(name_f, 'rb') as f:
        key = f.read()
        # Supprimer "_KAMI_" de la clé chargée si présent
        key = key.replace(b'_KAMI_', b'')
        return key
    
def crypt_f(nf, key):
    fer = Fernet(key)
    with open(nf, 'rb') as fo:
        c = fo.read()
    cf = fer.encrypt(c)
    with open(nf + '.kami', 'wb') as fc:
        fc.write(cf)

def decrypt_f(nfc, key):
    fer = Fernet(key)
    with open(nfc, 'rb') as fc:
        cc = fc.read()

    nfd = nfc[:-len('.kami')]

    cd = fer.decrypt(cc)
    with open(nfd, 'wb') as fd:
        fd.write(cd)

    os.remove(nfc)

intro = """
                                                                    
 ▄▀▄▄▄▄   ▄▀▀▄▀▀▀▄  ▄▀▀▄ ▀▀▄  ▄▀▀▄▀▀▀▄  ▄▀▀▀█▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄ 
█ █    ▌ █   █   █ █   ▀▄ ▄▀ █   █   █ █    █  ▐ ▐  ▄▀   ▐ █   █   █ 
▐ █      ▐  █▀▀█▀  ▐     █   ▐  █▀▀▀▀  ▐   █       █▄▄▄▄▄  ▐  █▀▀█▀  
  █       ▄▀    █        █      █         █        █    ▌   ▄▀    █     by kami
 ▄▀▄▄▄▄▀ █     █       ▄▀     ▄▀        ▄▀        ▄▀▄▄▄▄   █     █   
█     ▐  ▐     ▐       █     █         █          █    ▐   ▐     ▐   
▐                      ▐     ▐         ▐          ▐                  
                        
                         > Press Enter 

"""

Anime.Fade(Center.Center(intro), Colors.black_to_red, Colorate.Vertical, interval=0.035, enter=True)

def intro2():
    print(f"""{Fore.LIGHTRED_EX}

 ▄▀▄▄▄▄   ▄▀▀▄▀▀▀▄  ▄▀▀▄ ▀▀▄  ▄▀▀▄▀▀▀▄  ▄▀▀▀█▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄ 
█ █    ▌ █   █   █ █   ▀▄ ▄▀ █   █   █ █    █  ▐ ▐  ▄▀   ▐ █   █   █ 
▐ █      ▐  █▀▀█▀  ▐     █   ▐  █▀▀▀▀  ▐   █       █▄▄▄▄▄  ▐  █▀▀█▀  
  █       ▄▀    █        █      █         █        █    ▌   ▄▀    █     by kami
 ▄▀▄▄▄▄▀ █     █       ▄▀     ▄▀        ▄▀        ▄▀▄▄▄▄   █     █   
█     ▐  ▐     ▐       █     █         █          █    ▐   ▐     ▐   
▐                      ▐     ▐         ▐          ▐                  
                                     
                    Welcome to crypter

""")

intro2()
time.sleep(1)


while True:
    Write.Print("\nQuel option voulez vous choisir: ", Colors.red_to_yellow)
    Write.Print("\n 1. Créer une clé", Colors.red_to_yellow)
    Write.Print("\n 2. Crypter un fichier (Clé requise)", Colors.red_to_yellow)
    Write.Print("\n 3. Décrypter un fichier (Clé requise)", Colors.red_to_yellow)
    Write.Print("\n 4. Close", Colors.red_to_yellow)
    Write.Print("\nFaite vôtre choix: ", Colors.red_to_yellow, end="")
    choice = input()

    if choice == "1":
        key = gen_key()
        nfk = input(Fore.CYAN + "\nEntrez le nom de la clé:" + Style.RESET_ALL)
        save_key(key, nfk)
        Write.Print("\nClé créée avec succès!", Colors.red_to_green)
        time.sleep(2)
        clearing()
        intro2()
    
    elif choice == "2":
        nf = input(Fore.CYAN + "\nEntrez le nom du fichier à crypter: " + Style.RESET_ALL)
        nfk = input(Fore.CYAN + "\nEntrez le nom de la clé pour crypter le fichier: " + Style.RESET_ALL)
        cl = take_key(nfk)
        crypt_f(nf, cl)
        Write.Print(f"\nLe fichier {nf} a été crypté avec succès!", Colors.red_to_green)
        time.sleep(2)
        clearing()
        intro2()

    elif choice == "3":
        nf = input(Fore.CYAN + "\nEntrez le nom du fichier à décrypter: " + Style.RESET_ALL)
        nfk = input(Fore.CYAN + "\nEntrez le nom de la clé: " + Style.RESET_ALL)
        cl = take_key(nfk)
        decrypt_f(nf, cl)
        Write.Print(f"\nLe fichier {nf} a été décrypté avec succès!", Colors.red_to_green)
        time.sleep(2)
        clearing()
        intro2()

    elif choice == "4":
        Write.Print("\nSortie du programme...", Colors.red_to_yellow)
        break
    else:
        Write.Print("\nVôtre choix est invalide. Veuillez recommencer.", Colors.red_to_purple)
        time.sleep(2)
        clearing()
        intro2()