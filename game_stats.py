class GameStats():
    """Отслеживание статистики для игры Alien Invasion."""

    def __init__(self, ai_game):
        """Инициализирует статистику."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Игра Alien Invasion запускается в активном состоянии.
        self.game_active = False

        self.high_score = 0
        self.read_high_score()

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def read_high_score(self):
        try:
            with open('score.bin', 'r') as f:
                self.high_score = int(f.readline())
        except FileNotFoundError:
            with open('score.bin', 'w') as f:
                f.write('0')

    def write_high_score(self):
        try:
            with open('score.bin', 'w') as f:
                f.write(str(self.high_score))
        except FileNotFoundError:
            print('Невозможно записать файл результатов')
