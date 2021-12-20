from random import randint

"""
Modèle: Enemy
["STR: name", [FLOAT: health, FLOAT: maxHealth, FLOAT: attack, FLOAT: def], 
[(("STR: lootName", FLOAT: percentLoot), INT: minLootNb, INT: maxLootNb, INT : minGold, INT : maxGold,
INT: minXp, INT: maxXp]
"""


def combat(player, enemy):
    """
    player = ["playerName", [FLOAT: health, FLOAT: maxHealth, FLOAT: atk, FLOAT: def],
    [INT: helmet, INT: chestplate, INT: leggings, INT: boots, INT: weapon]]
    enemy = ["enemyName", [FLOAT: health, FLOAT: maxHealth, FLOAT: atk, FLOAT: def]]

    RETURN:
        win = BOOL: True si combat gagné, False si perdu.
        enemyName = STR: nom de l'ennemi
    """
    with open("Accounts/" + player + ".txt", 'r', encoding="utf-8") as fil:
        playerData = eval(fil.read())
    with open("Tables/EnemyTables/" + enemy + ".txt", 'r', encoding="utf-8") as fil:
        enemyData = eval(fil.read())
    playerName = playerData[0]
    playerStats = playerData[1]
    playerInventory = playerData[2]
    enemyName = enemyData[0]
    enemyStats = enemyData[1]
    win = False  # Mettre à False pour lancer le programme correctement
    """
    print(enemyName, "is coming to attack you!")
    ans = input("You have: " + str(playerStats[0]) + " hp, do you want to take this fight? Y/N")
    ans = ans.upper()
    if ans[0] == "Y":
        print("You attack first, ", playerName, "!")
        while playerStats[0] >= 0 and enemyStats[0] >= 0:
            nb = [randint(1, 20), randint(1, 20)]
            nbAns = int(input("How much is " + str(nb[0]) + "x" + str(nb[1]) + "?"))
            nb = nb[0] * nb[1]
            if nb == nbAns:
                enemyStats[0] -= playerStats[2] + playerInventory[4]
                print("Good answer! You deal", playerStats[2] + playerInventory[4], "damages!")
            else:
                enemyStats[0] -= (playerStats[2] + playerInventory[4]) / 2
                print("The answer was ", nb, "! You deal ", (playerStats[2] + playerInventory[4]) / 2, " damages!")
            print("The", enemyName, "deals you", enemyStats[3], "damages.")
            playerStats[0] -= enemyStats[2]
            print("You have", playerStats[0], "hp, and your enemy has", enemyStats[0], "hp left")
        if playerStats[0] <= 0:
            print("You died.")
            return win
        else:
            print("You won this fight! You have", playerStats[0], "hp left.")
            win = True

            return win, playerStats, enemyName, playerName
    else:
        return [False]
    """
    return True, playerStats, enemyName, playerName #Ligne de test


def reward(enemyName):
    with open("Tables/EnemyTables/" + enemyName + ".txt", 'r', encoding="utf-8") as fil:
        enemyGlobal = eval(fil.read())
    enemyLootTable = enemyGlobal[2][0]  # Récupère la LootTable

    enemyMinLootNb = enemyGlobal[2][1]  # Récupère la valeur minimale du nombre de loot
    enemyMaxLootNb = enemyGlobal[2][2]  # Récupère la valeur maximale du nombre de loot

    enemyMinGold = enemyGlobal[2][3]  # Idem pour Gold
    enemyMaxGold = enemyGlobal[2][4]  # Idem pour Gold

    enemyMinXp = enemyGlobal[2][5]  # Idem pour xp
    enemyMaxXp = enemyGlobal[2][6]  # Idem pour xp

    lootPool = []  # Création de la LootPool
    lootReward = []  # Création du LootReward (ce qui va être donné au joueur)
    for item, weight in enemyLootTable:
        lootPool.extend([item] * weight)
    nbLoot = randint(enemyMinLootNb, enemyMaxLootNb)  # Création de la loot table
    if nbLoot != 0:
        for i in range(nbLoot):
            lootReward.append(lootPool[randint(0, 99)])
    else:
        lootReward.append(None)
    lootReward.append(randint(enemyMinGold, enemyMaxGold))
    lootReward.append(randint(enemyMinXp, enemyMaxXp))
    lootPrint = "You looted:"
    lootDict = {}
    for loot in lootReward[0:-2]:  # Sélectionne tous les loots sauf l'xp et l'or
        if loot in lootDict.keys():  # Si le loot est dans le dict, on ajoute 1 à son nombre
            lootDict[loot] += 1
        else:  # Si le loot n'est pas dans le dict, on l'ajoute au dict : key = loot et value = 1
            lootDict[loot] = 1

    """
    Diplay part of the fonction
    """

    for loot in lootDict.keys():  # Boucle parmis les clés
        if loot is not None:  # Si le loot est différent de None
            lootPrint += "\n-" + str(loot) + ": " + str(lootDict[loot])  # Ajoute le nombre et son nombre à LootPrint

    if lootReward[-2] != 0:
        if lootReward[-2] == 1:
            lootPrint += "\n-" + str(lootReward[-2]) + " coin"  # Permet d'afficher qu'on a gagné 1 coin
        else:
            lootPrint += "\n-" + str(lootReward[-2]) + " coins"  # Permet d'afficher qu'on a gagné plusieurs coins

    if lootReward[-1] != 0:
        lootPrint += "\n-" + str(lootReward[-1]) + " xp"  # Ajoute la valeur de l'xp gagnée

    return lootPrint, [lootDict, lootReward[-2], lootReward[-1]]  # Retourne lootPrint et son tableau de valeur,
    # [dict, xp]
