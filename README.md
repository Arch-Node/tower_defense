# tower_defense

## Structure
tower_defense_game/
├── assets/
│   ├── images/
│   ├── sounds/
│   └── levels/
├── src/
│   ├── main.py
│   ├── game_loop.py
│   ├── game_states/
│   │   ├── game_state.py
│   │   ├── main_menu_state.py
│   │   ├── playing_state.py
│   │   ├── paused_state.py
│   │   └── game_over_state.py
│   ├── entities/
│   │   ├── tower.py
│   │   ├── enemy.py
│   │   ├── projectile.py
│   │   └── player.py
│   ├── levels/
│   │   ├── level_manager.py
│   │   ├── level_1.py
│   │   └── level_2.py
│   ├── ui/
│   │   ├── button.py
│   │   ├── menu.py
│   │   └── hud.py
│   └── utils/
│       ├── constants.py
│       ├── pathfinding.py
│       └── helpers.py
└── README.md

