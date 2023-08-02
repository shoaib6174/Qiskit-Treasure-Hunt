# Qiskit Treasure Hunt

The game is designed to help students understand how the states change when single qubit gates and measurement is done. The player will navigate a quantum map to reach treasure ( target state) as many time as possible using 100 play of cards. The target state will change randomly once the player reaches the target state.

<img width="502" alt="image" src="https://github.com/shoaib6174/Qiskit-Treasure-Hunt/assets/40586752/11b26b38-48ed-4df5-ac79-84008d7a5eeb">


## Gameplay:
* The game will start on |0> state and the objective is to reach the target state mentioned in the green box
* The player will navigate the map  using cards representing gates and measurement to reach the target state
* The player will have access to 4 cards at a time and after playing one card it will be replaced with another card randomly
* The goal is to reach the treasure ( target state) as many time as possible.

## Cards:
Here is the name and description of all the cards availabe in the game:
* H (Hadamard Gate): Roates about the (x+z)-axis by 180 degree
* S (Phase Gate): Rotates about the z-axis by 90 degree
* X (Pauli X Gate): Rotates about the x-axis by 180 degree
* Y (Pauli Y Gate): Rotates about the y-axis by 180 degree
* Z (Pauli Z Gate): Rotates about the z-axis by 180 degree
* I (Identity Gate): Does nothing
* Measurement: If the player is at 0 or 1, does nothing. Otherwise, it randomly selects 0 or 1
* Square Root of X Gate : Rotates about the x-axis by 90 degree



## Installation Guide:
* clone the repo
* install pygame on your device (pip install pygame)
* run the `main.py` file (python main.py)

## Credit:
This game has been inspired by Thomas Wong's Qubit Touchdown game.

  
  
