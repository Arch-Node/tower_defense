#%%
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('td_test.log'),  # Log messages to a file named 'app.log'
        logging.StreamHandler()])
import sys
sys.path.append('C:/software/tower_defense/scr/')
import pygame
from game_loop import GameLoop
from game_states.main_menu_state import MainMenuState
from game_states.playing_state import PlayingState
from game_states.paused_state import PausedState
from game_states.game_over_state import GameOverState
#%%

class TowerDefenseGame(GameLoop):
    def __init__(self):
        super().__init__()
        self.main_menu_state = MainMenuState(self)
        self.playing_state = PlayingState(self)
        self.paused_state = PausedState(self)
        self.game_over_state = GameOverState(self)
        self.current_state = self.main_menu_state

    def set_state(self, state):
        logging.debug(f"Changing state to {state.__class__.__name__}")
        self.current_state = state

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            else:
                self.current_state.handle_event(event)

    def update(self):
        delta_time = self.clock.tick(60) / 1000.0  # Delta time in seconds
        self.current_state.update(delta_time)

    def render(self):
        self.current_state.render(self.screen)
        pygame.display.flip()


#%%
if __name__ == "__main__":
    pygame.init()
    game = TowerDefenseGame()
    game.run()
    pygame.quit()

# %%
