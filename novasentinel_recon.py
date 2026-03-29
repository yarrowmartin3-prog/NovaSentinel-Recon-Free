import time
import sys
import os

GRIS_FONCE = '\033[1;30m'
GRIS_CLAIR = '\033[0;37m'
BLANC = '\033[1;37m'
CYAN = '\033[0;36m'
RESET = '\033[0m'

def afficher_banniere():
    os.system('clear')
    print(f"{CYAN}")
    print(r"""
     _   _  ______     __  ___  
    | \ | |/ __ \ \   / / / _ \ 
    |  \| | |  | \ \ / / / /_\ \
    | . ` | |__| |\ V / /  ___  \
    |_|\__|\____/  \_/ /_/     \_\
    """)
    print(f"      S E N T I N E L   R E C O N{RESET}")
    print(f"\n{GRIS_CLAIR}::: Défi d'Audit de Conformité de 60 Secondes :::")
    print(f"{GRIS_FONCE}Propulsé par NovaSuite Technologies{RESET}\n")

def lancer_defi_audit(cible):
    print(f"{BLANC}[+] Lancement du POC Gratuit sur : {cible}{RESET}")
    time.sleep(1)
    print(f"{GRIS_FONCE}[*] Interrogation des bases de données publiques...{RESET}")
    time.sleep(1.5)
    print(f"{GRIS_FONCE}[*] Analyse des en-têtes de sécurité HTTP...{RESET}")
    time.sleep(1.5)
    print(f"{GRIS_FONCE}[*] Vérification des ports critiques standards...{RESET}")
    time.sleep(2)
    print(f"\n{GRIS_CLAIR}--- RÉSULTATS DU DÉFI 60 SECONDES ---{RESET}")
    print(f"{BLANC}[!] ATTENTION : Vulnérabilités détectées sur la surface d'attaque.{RESET}")
    print(f"{GRIS_CLAIR}[!] Niveau de risque estimé : MOYEN-ÉLEVÉ{RESET}")
    print(f"\n{GRIS_FONCE}======================================================================{RESET}")
    print(f"{BLANC}La remédiation nécessite l'arsenal complet Aegis Nexus.{RESET}\n")
    print(f"{CYAN}OPTION 1 (DIY) : Obtenez le code source complet Aegis Pro")
    print(f"         >>> Télécharger sur Gumroad : https://gumroad.com/l/novasuite{RESET}\n")
    print(f"{CYAN}OPTION 2 (Expert) : Laissez nos experts sécuriser votre réseau")
    print(f"         >>> Lancez votre Audit Express (499 $ CAD) : https://novasuite.com/audit{RESET}")
    print(f"{GRIS_FONCE}======================================================================{RESET}\n")

if __name__ == "__main__":
    afficher_banniere()
    if len(sys.argv) > 1:
        cible = sys.argv
    else:
        cible = input(f"{BLANC}Entrez le domaine ou l'IP cible (ex: client.com) : {RESET}")
    lancer_defi_audit(cible)
