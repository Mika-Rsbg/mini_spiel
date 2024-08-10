# Terminal Text-Based Game: Mini-Game

Welcome to the **Mini-Game**! This is a simple Python game that you can play directly in your terminal. The game allows you to walk, eat, and encounter various in-game events like finding items, animals, or monsters.

## How to Play

1. **Start the Game:**
   - Clone this repository to your local machine.
   - Navigate to the directory where the repository is stored.
   - Run the game with the command:
     ```bash
     python main.py
     ```

2. **Game Options:**
   - When the game starts, you will be prompted to either start a new game or load a previous one:
     - Type `new` to start a new game.
     - Type `load` to load the last saved game state.

3. **In-Game Actions:**
   - **Walk:** Type `W` or `w` to walk. Walking consumes energy and may lead to finding items, encountering animals, or fighting monsters.
   - **Eat:** Type `E` or `e` to eat. Eating will restore some of your energy using the food you have collected.

## Features

- **Walking:** Move through the game world, with chances to find items, encounter animals, or face monsters.
- **Eating:** Restore energy by consuming food, essential for surviving in the game.
- **Random Events:** Encounters with items, animals, and monsters are determined randomly, making each playthrough unique.
- **Saving and Loading:** The game automatically saves your progress, allowing you to load your last game session.

## Requirements

- The game is programmed in **Python 3.12**.
- Compatibility with other Python versions has not been tested.

## Code Structure

- **main.py:** Contains the main game logic and all the classes:
  - `Game`: Manages the game's start, stop, and kill functions.
  - `Interaction`: Handles user input and game interactions.
  - `Player`: Represents the player's status and actions like walking and eating.
  - `Fight`: Manages combat-related actions.
  - `Monster`: Handles monster behavior.
  - `Item`: Deals with items found during the game.

## Contributing

Contributions are welcome! If you find bugs or have suggestions for new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the GPL v.3.0 License. See the `LICENSE` file for more information.

## Contact

For any questions or feedback, please reach out via GitHub issues.

Enjoy the game!
