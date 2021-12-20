"""
Stats joueur : health, maxHealth, attack,  armor
"""


def has_account():
    """
    Fonction pour savoir si le joueur a un compte

    Demande :
    STR : a un compte ? -> hasAccount
    STR : hasAccount -> upper pour éviter les fautes de compréhension

    Tant que le joueur n'a pas dit s'il avait un compte ou non
    Si hasAccount = Y:
        hasAccount STR -> BOOL : True
    Si hasAccount = N:
        hasAccount STR -> BOOL : False
    Défaut :
        Affiche "I don't understand. Can you repeat?"

    """
    while True:
        hasAccount = input("Hello! \nDo you have an account? Y/N")
        hasAccount = hasAccount.upper()
        if hasAccount[0] == "Y":
            hasAccount = True
            return hasAccount
        elif hasAccount[0] == "N":
            hasAccount = False
            return hasAccount
        print("I don't understand.\nCan you repeat?")


def register():
    """
    Fonction de création de compte
    
    STR : nom de compte -> accountName
    STR : confirmation -> accountNameSure
    Tant que le compte n'est pas créé :
        Si accountNameSure = Y:
            Création du compte dans le dossier "Accounts/accountName.txt"
                Structure du fichier texte (LIST) -> playerData :
                    STR : nom du compte  -> playerName
                    LIST : stats du comtpe -> playerStats
                    LIST : équipement du compte -> playerInventory
                    DICT : matériaux du compte -> playerMaterials
                    DICT : blue prints du compte -> playerBlueprints
                    INT : or du compte -> playerGold
                    DICT : avancements du compte -> playerAdvancements
                    INT : xp depuis le dernier niveau -> playerXp
                retourne :
                    playerName, playerStats, playerInventory, playerMaterials, playerBlueprints, playerGold,
                    playerAdvancements
        Si accountNameSure = N:
            Affiche "Okay", retourne dans la boucle principale
        Si accountNameSure != N et != Y:
            Affiche "I don't understand", retourne dans la boucle principale
    """
    print("Let's create your account!")
    while True:
        accountName = input("What will be your account's name?")
        accountNameSure = input(accountName + " will be your name, are you sure? Y/N")
        if accountNameSure[0] == "Y":
            accountName += ".txt"
            with open("Accounts/" + accountName, 'w') as fil:
                print("[\"" + accountName[0:-4] + "\",[],[],{},{}, 0, {}, 0]", file=fil)
            print("Account created!")
            with open("Accounts/" + accountName, 'r', encoding="utf-8") as fil:
                playerData = eval(fil.read())
            playerName = playerData[0]
            playerStats = playerData[1]
            playerInventory = playerData[2]
            playerMaterials = playerData[3]
            playerBlueprints = playerData[4]
            playerGold = int(playerData[5])
            playerAdvancements = playerData[6]
            playerXp = playerData[7]
            return [playerName, playerStats, playerInventory, playerMaterials, playerBlueprints, playerGold,
                    playerAdvancements, playerXp]
        elif accountNameSure[0] == "N":
            print("Okay")
        else:
            print("I don't understand, can you repeat?")


def login():
    """
    Fonction de création de compte

    Demande STR accountName
    Ajoute ".txt" à accountName
    Ouvre le fichier txt du compte, prend et retourne les données (voir fonction "register" pour les valeurs)
    """
    while True:
        accountName = input("What's your account's name?")
        accountName += ".txt"
        with open("Accounts/" + accountName, 'r', encoding="utf-8") as fil:
            playerData = eval(fil.read())
        playerName = playerData[0]
        playerStats = playerData[1]
        playerInventory = playerData[2]
        playerMaterials = playerData[3]
        playerBlueprints = playerData[4]
        playerGold = int(playerData[5])
        playerAdvancements = playerData[6]
        playerXp = playerData[7]
        return [playerName, playerStats, playerInventory, playerMaterials, playerBlueprints, playerGold,
                playerAdvancements, playerXp]


def save(playerName, playerStats, playerInventory, playerMaterials, playerBlueprints, playerGold,
         playerAdvancements, playerXp):
    playerData = []
    playerData[0] = "\"" + str(playerName) + "\""
    playerData[1] = playerStats
    playerData[2] = playerInventory
    playerData[3] = playerMaterials
    playerData[4] = playerBlueprints
    playerData[5] = int(playerGold)
    playerData[6] = playerAdvancements
    playerData[7] = int(playerXp)
    with open("Accounts/" + playerName + ".txt", 'w') as fil:
        print(playerData, file=fil)
