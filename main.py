import base64
from colorama import Fore, Style, Back, init
credit = f"""{Fore.RED} {Style.DIM}
 ___  ____    _____  ____      _     ____  _  __ _____  ____  
|_ _||  _ \  |_   _||  _ \    / \   / ___|| |/ /| ____||  _ \ 
 | | | | | |   | |  | |_) |  / _ \ | |    | ' / |  _|  | |_) |
 | | | |_| |   | |  |  _ <  / ___ \| |___ | . \ | |___ |  _ < 
|___||____/    |_|  |_| \_\/_/   \_\\____||_|\_\|_____||_| \_\

                                                {Fore.GREEN}{Style.BRIGHT}by Div_YT
             
"""
init(convert=True)
def token(ID):
    token = base64.b64encode(ID.encode("Utf-8"))
    return token.decode("Utf-8")

def starter():
    print(credit)
    print(f"{Fore.GREEN}[INIT]{Fore.BLUE}Cet Outil est pour Discord")
    print(f"{Fore.GREEN}[INIT]Appuyez sur entrée pour quitter. {Fore.RED}{Style.BRIGHT}")
    ID = input(f"[-]ID de la personne Cible : ")
    if ID :
        a_token = token(ID)
        print(f"{Fore.GREEN}[END]Le début de son Token est : {Style.BRIGHT}{a_token} {Style.RESET_ALL}{Fore.RESET}")
        exit()
    else:
        exit()

def exit():
    print(f"{Fore.RED}[END]{Fore.RESET}Exiting")
    input("(Process 32) Appuyez sur n'importe quelle touche pour sortir ...")

if __name__ == "__main__":
    starter()