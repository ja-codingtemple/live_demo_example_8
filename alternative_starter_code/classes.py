'''
REMINDER:
In addition to completing the Warrior and Mage classes, you need to create two more classes that inherit from Character, such as:
- Archer
- Paladin
You don't have to create these EXACT classes, you have creative freedom about which additional classes to create. It doesn't have to be Archer & Paladin.

Each custom class must have two unique abilities, such as:
- Archer: "Quick Shot" (double arrow attack) and "Evade" (avoid next attack).
- Paladin: "Holy Strike" (bonus damage) and "Divine Shield" (blocks the next attack).

If you'd like, you can consider Rogue one of your two custom classes, leaving you with only one more to implement.
Note: Instructor Jeremy Alkire provided permission for Rogue to count as the first custom class.

Additional requirements:
- You need to implement a heal() method in the base Character class.
- You need to randomize the damage done in the Character class' attack() method.
- You need to implement the special_ability() method for the Mage class.
'''
# ====================== BASE CHARACTER CLASS ============================
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.gold = 1000

    def attack(self, opponent):
        # MAKE SURE YOU RANDOMIZE YOUR ATTACK DAMAGE
        # HINT: Use the Python random library
        damage = self.attack_power
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
    
    # PLEASE MAKE SURE YOU IMPLEMENT THIS METHOD.
    def heal(self):
        print("THIS METHOD IS NOT YET IMPLEMENTED.")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
        
# ========================= SUBCLASSES ===================================

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        
    def special_ability(self, opponent):
        print("\nAbilities:")
        print("1. Deadly Strike")
        print("2. Vampiric Strike")
        action = input("\nWhich ability do you want to use? ")
        
        if action == "1":
            '''
            Ability: Deady Strike
            Description: The warrior performs a deadly strike which does significant damage to the opponent.
            '''
            damage = self.attack_power * 2.5
            opponent.health -= damage
            print(f"\n{self.name} strikes {opponent.name} and does {damage} damage!")
        elif action == "2":
            '''
            Ability: Vampiric Strike
            Description: The fighter strikes the opponent & heals for the damage done.
            '''
            damage = self.attack_power
            opponent.health -= damage # Do damage to the opponent equal for an amount equal to 'damage'
            self.health += damage # Heal self equal for an amount equal to 'damage'
            # Check if our current health exceeds our maximum health
            if self.health > self.max_health:
                self.health = self.max_health # If it does, forcibly set our current health back down to our max health.

            print(f"\n{self.name} attacks {opponent.name} and does {damage} damage & and heals for the same amount!")
            print(f"{self.name} now has {self.health} health.")
            

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")
        
# Custom Class #1
class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)
        
    def special_ability(self, opponent):
        print("\nAbilities")
        print("1. Backstab")
        print("2. Steal")
        action = input("\nWhich ability do you want to use? ")
        
        if action == "1":
            '''
            Ability: Backstab
            Description: The rogue sneaks behind the target & stabs them in the back for significant damage.
            '''
            damage = self.attack_power * 2
            opponent.health -= damage
            print(f"\n{self.name} sneaks behind {opponent.name} and stabs him in the back for {damage} damage.")
        elif action == "2":
            '''
            Ability: Steal
            Description: The rogue sneaks up on his target & steals some gold from them.
            '''
            amount_to_steal = 100
            opponent.gold -= amount_to_steal
            self.gold += amount_to_steal
            print(f"\n{self.name} sneaks up on {opponent.name} and steals {amount_to_steal} gold!")

# Custom Class #2