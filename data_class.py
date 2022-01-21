class Player():
    def __init__(self, hp=100, shield=100):
        self.hp = hp
        self.shield = shield
        self.dead = False

    def take_damage(self, weapon):
        dmg = weapon.get_damage()

        # Remove shield
        while self.shield != 0:
            if dmg != 0:
                self.shield -= 1
                dmg -= 1
            else:
                break

        # Remove Hp
        while self.hp != 0:
            if dmg != 0:
                self.hp -=1
                dmg -= 1
            else:
                break

        if self.hp == 0:
            self.dead = True

    def get_hp(self):
        return self.hp
    def get_shield(self):
        return self.shield
    def get_dead(self):
        return self.dead

class Weapon():
    def __init__(self, dmg=0):
        self.damage = dmg

    def get_damage(self):
        return self.damage

if __name__ == "__main__":
    player1 = Player(hp=100,shield=100)
    ak47 = Weapon(dmg=120)

    print(f"HP: {player1.get_hp()}, SHIELD: {player1.get_shield()}")
    player1.take_damage(ak47)
    print(f"HP: {player1.get_hp()}, SHIELD: {player1.get_shield()}")
