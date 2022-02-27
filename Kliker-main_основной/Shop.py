import pygame.image
from pygame.color import THECOLORS


class Shop:
    def __init__(self):
        self.return_button = pygame.image.load(r"img/Krestik.png")
        self.return_pos = (0, 0)
        self.klik = pygame.image.load(r"img/Klik.png")
        self.pos_klik = (40, 300)
        self.mech = pygame.image.load(r"img/Mech.png")
        self.pos_mech = (40, 100)
        self.click_cost = 10
        self.DPS_cost = 10

    def buying(self, cost, balance):
        if balance >= cost:
            cost += 10
            return int(balance - cost / 2), cost
        return balance, cost

    def try_to_buy(self, type, balance):
        """
        Функция проверяет что было куплено в магазине
        """
        if type == "click":
            new_balance, new_cost = self.buying(self.click_cost, balance)
            self.click_cost = new_cost
            return new_balance
        elif type == "DPS":
            new_balance, new_cost = self.buying(self.DPS_cost, balance)
            self.DPS_cost = new_cost
            return new_balance
        return balance

    def draw(self, screen, balance):
        """
        Все запускает и переносит в мейн файл
        """
        screen.blit(self.return_button, self.return_pos)
        screen.blit(self.klik, self.pos_klik)
        screen.blit(self.mech, self.pos_mech)
        self.write(screen, balance)
        self.first_bonus(screen)

    def write(self, screen, balance):
        """
        Эта функция создает описания товаров в магазине и твой балланс
        """
        font = pygame.font.SysFont('arial', 20)
        font1 = pygame.font.SysFont('arial', 40)
        text2 = font1.render(str(f'Ваш балланс:{balance}'), True, THECOLORS['green'])
        text1 = font.render(str('Этот палец сможет работать как негр, пока вы спите!'), True, THECOLORS['green'])
        text = font.render(str('Этот меч сможет прокачать вашу силу до бесконечности!'), True, THECOLORS['green'])
        screen.blit(text, (165, 100))
        screen.blit(text1, (165, 300))
        screen.blit(text2, (60, 0))

    def first_bonus(self, screen):
        """
        Эта функция выводит на экран сколько стоит этот товар
        """
        font = pygame.font.SysFont('arial', 30)
        text2 = font.render(str(f"Это стоит:{self.click_cost}"), True, THECOLORS['orange'])
        screen.blit(text2, (30, 210))
        text1 = font.render(str(f"Это стоит:{self.DPS_cost}"), True, THECOLORS['orange'])
        screen.blit(text1, (30, 410))


