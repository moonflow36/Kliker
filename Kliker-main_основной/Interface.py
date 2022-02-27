from Interface_buttons.seed import Seed
from Interface_buttons.name import Name
from Interface_buttons.level import Level
from Interface_buttons.shop_button import Shopbutton



class Interface:
    def __init__(self):
        self.seed = Seed()
        self.name = Name()
        self.level = Level()
        self.shop_button = Shopbutton()

    def draw(self, screen):
        """
        Эта функция рисует картинки из разных файлов
        """
        self.shop_button.draw(screen)
        self.seed.draw(screen)
        self.name.draw(screen)
        self.level.draw(screen)

