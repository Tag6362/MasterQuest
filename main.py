from MasterQuest import login_functions as log_func
import combat_functions as comb_func
import inv_functions as inv_func


"""
Initialisation des classes
"""


class Character:
    def __init__(self, name, health, atk, defense, xp=0.0):
        self.name = name
        self.health = health
        self.atk = atk
        self.defense = defense
        self.xp = xp


"""
Initialisation des variables
"""
hasAccount = False
"""
FIN
"""
"""
Définition des fonctions
"""


combatVar = comb_func.combat("Tom", "Orc")
playerName = combatVar[-1]
if combatVar[0]:
    reward = comb_func.reward(combatVar[2])
    rewardPrinting = reward[0]
    rewardMaterials = reward[1][0]
    rewardGold = reward[1][1]
    rewardXp = reward[1][2]
    print(str(rewardPrinting) + "\n" + str(rewardXp) + "\n" + str(rewardGold))
    print("Reward Materials", rewardMaterials)
    storeLoot = inv_func.store_loot(playerName, rewardMaterials,rewardXp, rewardGold)

else:
    print("Didn't took the fight")


# playsound("RPG Sound Pack/inventory/smithing.wav")

"""
FIN
"""
"""
login = log_func.login()
print(login[0:3])

while True:
    hasAccount = log_func.has_account()  # on regade si le compte existe
    if hasAccount:
        try:
            print(log_func.login())  # si le compte existe, on se connecte via login()
            break
        except FileNotFoundError:
            print("Can't find your account")
    elif not hasAccount:
        log_func.register()  # si le compte n'existe pas, on crée un compte via register()
        break
"""