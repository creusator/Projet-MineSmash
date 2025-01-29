class GameClock:
    def __init__(self, day_duration, night_duration):
        self.day_duration = day_duration
        self.night_duration = night_duration
        self.total_duration = day_duration + night_duration
        self.elapsed_time = 0  # Temps écoulé en "unités de temps" du jeu

    def update(self):
        self.elapsed_time += 1  # Incrémente le temps écoulé à chaque mise à jour

    def get_time_of_day(self):
        current_time = self.elapsed_time % self.total_duration
        if current_time < self.day_duration:
            return "day"
        else:
            return "night"

class Game:
    def __init__(self):
        self.clock = GameClock(day_duration=120, night_duration=60)  
        # 120 unités de temps pour le jour, 60 pour la nuit

    def update(self):
        self.clock.update()
        time_of_day = self.clock.get_time_of_day()
        if time_of_day == "day":
            self.set_day()
        else:
            self.set_night()

    def set_day(self):
        # Code pour définir l'environnement du jeu pendant le jour
        screen.fill((85,0,170))

    def set_night(self):
        # Code pour définir l'environnement du jeu pendant la nuit
        screen.fill((135,206,235))

    def run(self):
        while True:
            self.delay_counter += 1
            if self.delay_counter >= 60:  # Simule un délai de 60 cycles de boucle
                self.update()
                self.delay_counter = 0
if __name__ == "__main__":
    game = Game()
    game.run()