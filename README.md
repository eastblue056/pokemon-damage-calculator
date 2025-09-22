# Pokémon Damage Calculator 

A Python Script that simulates how much damage an attacking Pokémon does to a defending Pokémon.  
You can input the Pokémon names, the move’s base power, and the effectiveness multiplier (e.g. *super effective* or *not very effective*) — then the program calculates the final damage.

---

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/pokemon-damage-calculator.git
   cd pokemon-damage-calculator
   ```

2. Run the script:
```
python main.py
```

## Usage 

Example Input:

```
please enter the attacking pokemon's name: Pikachu
please enter the defending pokemon's name: Bulbasaur
please enter the move's power (ex. 30, 40, 50): 40
please enter the effectiveness multiplier (2 for super effective, 0.5 for not very effective): 2
```


Example output:

```
Pikachu used a move!!
Pikachu dealt 80.0 damage to Bulbasaur!!
```

## Features
- Calculates damage as `move_power * effectiveness`
- Text based, no external dependencies.

