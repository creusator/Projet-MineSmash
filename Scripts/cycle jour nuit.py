# Créé par Elève, le 20/01/2025 en Python 3.7
import time

class Game:
    def __init__(self, day_duration, night_duration):
        self.day_duration = day_duration  # durée du jour en second
        self.night_duration = night_duration  # durée de la nuit en second
        self.is_day = True  # lance le jeu le jour
    def toggle_day_night(self):
        self.is_day = not self.is_day
        if self.is_day:
            show_light()
        else:
            show_dark

    def run_day_night_cycle(self):
        while True:
            self.toggle_day_night()
            if self.is_day:
                time.sleep(self.day_duration)
            else:
                time.sleep(self.night_duration)
    def show_light(self):
        screen.fill((85,0,170))
    def show_dark(self):
        screen.fill((135,206,235))

# Exemple :
day_duration = 60
night_duration = 60

game = Game(day_duration, night_duration)
game.run_day_night_cycle()
