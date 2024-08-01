# Tower Defense Game

## Overview

This is a tower defense game implemented in Python using the Pygame library. The goal of the game is to prevent enemies from reaching a designated endpoint by strategically placing towers that shoot at the enemies.

## Project Structure

- **tower_defense_game**
  - **assets**
    - **images**: Contains image assets for the game.
    - **sounds**: Contains sound files used in the game.
    - **levels**: Contains level design files and data.
  - **src**
    - **main.py**: Entry point for the game, initializes Pygame and starts the game loop.
    - **game_loop.py**: Contains the `GameLoop` class responsible for managing the main game loop, including event handling, updating game state, and rendering.
    - **game_states**
      - **game_state.py**: Base class for all game states.
      - **main_menu_state.py**: Manages the main menu state of the game.
      - **playing_state.py**: Handles the gameplay state where the player interacts with the game.
      - **paused_state.py**: Manages the state when the game is paused.
      - **game_over_state.py**: Handles the game over state, where the player is shown the results and options to restart or quit.
    - **entities**
      - **tower.py**: Defines the tower entities that can be placed on the game map.
      - **enemy.py**: Defines the enemy entities that move through the map.
      - **projectile.py**: Defines the projectiles fired by towers.
      - **player.py**: Defines player-specific attributes and methods.
    - **levels**
      - **level_manager.py**: Manages the loading and progression of game levels.
      - **level_1.py**: Contains data and logic for the first level.
      - **level_2.py**: Contains data and logic for the second level.
    - **ui**
      - **button.py**: Defines button UI elements.
      - **menu.py**: Manages the game menus.
      - **hud.py**: Defines the heads-up display (HUD) elements.
    - **utils**
      - **constants.py**: Contains constants used throughout the game.
      - **pathfinding.py**: Implements pathfinding algorithms for enemy movement.
      - **helpers.py**: Contains various helper functions used in the game.

## Features Yet to Be Implemented

- **Assets**
  - **images**: Game assets such as textures and sprites.
  - **sounds**: Background music and sound effects.
  - **levels**: More level designs and data files.

- **Game States**
  - **game_state.py**: Implementation details for transitioning between different game states.

- **Entities**
  - **tower.py**: Implementation of various tower types with different abilities.
  - **enemy.py**: Different enemy types with varying attributes and behaviors.
  - **projectile.py**: Various projectile types and effects.
  - **player.py**: Features for player upgrades and scoring.

- **Levels**
  - **level_manager.py**: Advanced level progression and difficulty scaling.
  - **level_1.py**: Additional levels and their unique challenges.
  - **level_2.py**: More complex level designs.

- **UI**
  - **button.py**: Interactive UI elements like buttons for in-game actions.
  - **menu.py**: Additional menus for game settings and options.
  - **hud.py**: Enhanced HUD features and visual indicators.

- **Utils**
  - **pathfinding.py**: Improved pathfinding algorithms and optimizations.
  - **helpers.py**: Additional utility functions for game features.
