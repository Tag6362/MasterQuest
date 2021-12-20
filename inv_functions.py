"""
["Name",[life, maxLife, atk, def],[helmet, chestplate, leggings, boots, weapon],{materials},{bluePrints}, {achievements}
    coins , xp]
"""


def store_loot(playerName, materials, coins, xp):
    """
    player = "playerName"
    rewardLoots = [DICT : {'item' : number}, INT : xp]


    RETURN:
        win = BOOL: True si combat gagné, False si perdu.
        enemyName = STR: nom de l'ennemi
    """
    with open("Accounts/" + playerName + ".txt", 'r', encoding="utf-8") as fil:
        playerData = eval(fil.read())
    print("=================Function Store Loot correctly used")
    print(playerData)

    for item in materials:  # Tous les items lootés
        if item in playerData[3]:  # Déjà dans les matériaux du joueur ? Oui -->
            playerData[3][item] += materials[item]  # On ajoute le nombre d'items lootés à celui déjà présent
        else:  # Si le joueur n'a jamais rencontré ce matériaux
            playerData[3][item] = materials[item]  # On crée la valeur dictionnaire avec le nombre d'items lootés

    playerData[-2] += coins
    playerData[-1] += xp

    with open("Accounts/" + playerName + ".txt", 'w') as fil:
        print(playerData, file=fil)

    print(playerData)
    print("====================Function End")

