# asking attacker and defender

attacker_pkmn = input("please enter the attacking pokemon's name: ")
defender_pkmn = input("please enter the defending pokemon's name: ")

# asking for move's power

move_power = float(input("please enter the move's power (ex. 30, 40, 50): "))

# asking for effectiveness multiplier
effectivness = float(input("please enter the effectiveness multiplier (2 for super effective, 0.5 for not very effective)"))

# setting damage 
damage = move_power * effectivness
print(f"{attacker_pkmn} used a move!!")
print(f"{attacker_pkmn} dealt {damage} damage to {defender_pkmn}!!")
