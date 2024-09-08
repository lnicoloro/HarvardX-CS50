import random

class Fighter:
    def __init__(self):
        self.hp = 120

    @property
    def damage_value(self):
        damage = random.randint(0, 25)
        return damage

    @property
    def block_value(self):
        stopped = random.randint(0, 15)
        return stopped


def main():

    dave = Fighter()
    bob = Fighter()

    while bob.hp > 0 and dave.hp > 0:
        x = attack(dave, bob)
        print(x)
        print(bob.hp)
    else:
        exit()







def attack(killer, victim):
    dmg = killer.damage_value
    victim.hp = victim.hp - dmg
    return dmg






if __name__ == "__main__":
    main()