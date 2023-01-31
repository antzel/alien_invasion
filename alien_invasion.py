import sys

import pygame

class AlienInvasion:
    """Класс управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()

        self.screen  = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Отображение последнего прорисованного экрана.
            pygame.display.flip()


#if __name__ == '__alien_invasion__':
    # Создание экземпляра и запуск игры.
ai = AlienInvasion()
ai.run_game()
