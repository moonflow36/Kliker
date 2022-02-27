import pygame
from pygame.color import THECOLORS

import time
from Boss import Boss
from Interface import Interface
from Shop import Shop


class Main:
    def __init__(self):
        pygame.init()
        self.wid = 800
        self.hei = 600
        self.screen = pygame.display.set_mode((self.wid, self.hei))
        self.interface = Interface()
        self.boss = Boss(1)
        self.draw_work = True
        self.player_damage = 5
        self.damage_per_second = 1
        self.level = 1
        self.active_window = "game"
        self.shop = Shop()
        self.time = time.time()
        self.img1 = pygame.image.load(r"img/new_level1.png")
        self.img2 = pygame.image.load(r"img/new_level2.png")
        self.last_visible_health = self.boss.hp
        self.need_to_draw = True

    def draw(self):
        if self.active_window == "game":
            if self.need_to_draw:
                self.screen.fill((0, 0, 0))
            self.interface.draw(self.screen)
            self.boss.draw(self.screen)
            self.health_bar()

        elif self.active_window == "shop":
            self.screen.fill(THECOLORS['purple'])
            self.shop.draw(self.screen, self.interface.seed.count)

    def start(self):
        """
        Эта функция обрабатывет нажатие мыши и запускает, функция draw()
        """
        print(pygame.font.get_fonts())
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.try_to_click(event.pos)
            self.draw()
            self.check_time()
            pygame.display.flip()

    def bite_boss(self, damage):
        """
        Эта функция проверяет был ли убит босс, если убит то левел + 1 если нет то pass
        """
        self.need_to_draw = True
        new_seed_count = self.boss.bite(damage)
        self.interface.seed.count += new_seed_count
        if new_seed_count != 0:
            self.interface.level.value += 1

    def check_time(self):
        new_time = time.time()
        if new_time >= self.time + 1:
            self.need_to_draw = True
            self.bite_boss(self.damage_per_second)
            self.time = new_time

    def try_to_click(self, pos):
        """
        Эта функция проверяет координаты мыши. Если координаты по x от 100 до 700 и по y от 200 до 600 наносим урон боссу.
        Если координаты по x от 0 до 50 и по y от 0 до 50 открывается магазин, где можно покупать разные приколюхи.
        Дальше 2 условия проверяет, нажата ли была клавиша на буст(приколюху)
        """
        if self.active_window == "game":
            self.try_to_click_game(pos)
        elif self.active_window == "shop":
            self.try_to_click_shop(pos)

    def try_to_click_game(self, pos):
        if self.active_window == "game":
            if 100 < pos[0] < 700 and 200 < pos[1] < 600:
                self.bite_boss(self.player_damage)
            elif 0 < pos[0] < 50 and 0 < pos[1] < 50:
                self.active_window = "shop"
                self.need_to_draw = True

    def try_to_click_shop(self, pos):
        if self.check_that_hit((0, pos[0], 50), (0, pos[1], 50)):
            self.active_window = "game"
        elif self.check_that_hit((40, pos[0], 150), (100, pos[1], 200)):
            first_damage = self.interface.seed.count
            self.interface.seed.count = self.shop.try_to_buy("click", self.interface.seed.count)
            if first_damage != self.interface.seed.count:
                self.player_damage += 10
        elif self.check_that_hit((40, pos[0], 150), (300, pos[1], 400)):
            first_damage = self.interface.seed.count
            self.interface.seed.count = self.shop.try_to_buy("DPS", self.interface.seed.count)
            if first_damage != self.interface.seed.count:
                self.damage_per_second += 2

    def check_that_hit(self, x_position, y_position):
        """
        :param x_position: кортеж из трех чисел(наименьшее, проверяемое, наибольшее)
        :param y_position: кортеж из трех чисел(наименьшее, проверяемое, наибольшее)
        :return: попали ли на кнопку
        rtype: bool
        """
        return x_position[0] < x_position[1] < x_position[2] and y_position[0] < y_position[1] < y_position[2]

    def health_bar(self):
        """
        Эта функция выводит здоровье нашего босса, и отображает
        его ввиде прямоугольника у которого с право max хп, а слева min
        """
        k = self.boss.hp / (50 * self.boss.level)
        r = pygame.Rect(100, 60, k * 600, 50)
        pygame.draw.rect(self.screen, (255, 0, 0), r, 0)
        pygame.display.update()
        l = self.boss.hp
        font = pygame.font.SysFont('couriernew', 40)
        text = font.render(str('0'), True, THECOLORS['green'])
        text1 = font.render(str(f"{l}"), True, THECOLORS['green'])
        if self.need_to_draw:
            self.screen.blit(text, (65, 50))
            self.screen.blit(text1, (710, 50))
        self.need_to_draw = False


main = Main()
main.start()
# Код помогал писать https://github.com/nongi3
