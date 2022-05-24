import pygame
from settings import *
import pygame_widgets
from pygame_widgets.button import Button
from Gamemap import *

pygame.init()


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'

    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.draw_start()
            if self.state == 'next_day':
                self.next_day_events()
                self.draw_next_day()
            if self.state == 'garden_info':
                self.garden_info_events()
                self.draw_garden_info()

    ########################     START FUNCTIONS     ########################

    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def draw_start(self):
        self.screen.fill(BLACK)
        # back = pygame.image.load("images/garden_background.png")
        # self.screen.blit(back,(20, 75))
        self.add_button_start_garden(20, 20)
        self.draw_buttons()
        event = pygame.event.get()
        pygame_widgets.update(event)
        pygame.display.update()

    ########################      NEXT DAY FUNCTIONS     ########################

    def next_day_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def draw_next_day(self):
        self.screen.fill(BLACK)
        back = pygame.image.load("images/garden_background.png")
        self.screen.blit(back, (20, 75))
        back = pygame.image.load("images/garden_background.png")
        if self.garden.weather.parameters["weather_is"] == "sun":
            sky = pygame.image.load("images/sunny.png")
            self.screen.blit(sky, (120, 130))
        elif self.garden.weather.parameters["weather_is"] == "drought":
            sky = pygame.image.load("images/sunny_02.png")
            self.screen.blit(sky, (120, 130))
        elif self.garden.weather.parameters["weather_is"] == "rain":
            sky1 = pygame.image.load("images/rain_1.png")
            sky2 = pygame.image.load("images/rain_2.png")
            sky3 = pygame.image.load("images/rain_3.png")
            self.screen.blit(sky1, (120, 130))
            self.screen.blit(sky3, (400, 110))
            self.screen.blit(sky2, (250, 170))
        count_c = 60
        count_t = 70
        for plant in self.garden.plants:
            if plant.parameters["type_id"] == 1:
                if plant.parameters["age"] <= 1:
                    carrot = pygame.image.load("images/carrot_1.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, 420))
                elif 1 < plant.parameters["age"] <= 2:
                    carrot = pygame.image.load("images/carrot_2.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, 420))
                elif 2 < plant.parameters["age"] <= 3:
                    carrot = pygame.image.load("images/carrot_3.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, 420))
                elif 3 < plant.parameters["age"] <= 4:
                    carrot = pygame.image.load("images/carrot_4.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, 420))
                if plant.parameters["weed"]:
                    weed = pygame.image.load("images/trava.png")
                    weed.set_colorkey(WHITE)
                    self.screen.blit(weed, (20 + count_c, 450))
                count_c += 100
            elif plant.parameters["type_id"] == 3:
                if plant.parameters["age"] <= 1:
                    carrot = pygame.image.load("images/tree_1.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_t, 250))
                elif 1 < plant.parameters["age"] <= 2:
                    carrot = pygame.image.load("images/tree_2.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_t, 250))
                elif 2 < plant.parameters["age"] <= 3:
                    carrot = pygame.image.load("images/tree_3.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_t, 250))
                elif 3 < plant.parameters["age"] <= 4:
                    carrot = pygame.image.load("images/tree_4.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_t, 250))
                elif 4 < plant.parameters["age"] <= 5:
                    carrot = pygame.image.load("images/tree_5.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_t, 250))
                elif 5 < plant.parameters["age"] <= 6:
                    carrot = pygame.image.load("images/tree_6.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_t, 250))
                elif 6 < plant.parameters["age"] <= 7 or plant.parameters["points_to_grow_up"] <= 15:
                    carrot = pygame.image.load("images/tree_7.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_t, 250))
                elif 7 < plant.parameters["age"] <= 8 and plant.parameters["points_to_grow_up"] >= 15:
                    carrot = pygame.image.load("images/tree_8.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_t, 250))
                elif 8 < plant.parameters["age"] <= 9 and plant.parameters["points_to_grow_up"] >= 18:
                    carrot = pygame.image.load("images/tree_9.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_t, 250))
                elif plant.parameters["age"] > 9 and plant.parameters["points_to_grow_up"] <= 10:
                    carrot = pygame.image.load("images/tree_7.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_t, 250))
                elif plant.parameters["age"] > 9 and plant.parameters["points_to_grow_up"] <= 15:
                    carrot = pygame.image.load("images/tree_8.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_t, 250))
                elif plant.parameters["age"] > 9 and plant.parameters["points_to_grow_up"] > 19:
                    carrot = pygame.image.load("images/tree_9.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_t, 250))
                if plant.parameters["weed"]:
                    weed = pygame.image.load("images/trava.png")
                    weed.set_colorkey(WHITE)
                    self.screen.blit(weed, (20 + count_t, 335))
                count_t += 120
            elif plant.parameters["type_id"] == 2:
                pest = pygame.image.load("images/c_pest.png")
                pest.set_colorkey(WHITE)
                self.screen.blit(pest, (45 + count_t, 220))

        self.draw_buttons()
        event = pygame.event.get()
        pygame_widgets.update(event)
        pygame.display.update()

    ########################       GARDEN INFO FUNCTIONS      ########################

    def garden_info_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def draw_garden_info(self):
        self.screen.fill(BLACK)
        self.draw_text("harvest of fruits: ", self.screen, [20, 70], 26, WHITE, FONT)
        self.draw_text(str(self.garden.harvest_of_apples), self.screen, [250, 70], 26, WHITE, FONT)
        self.draw_text("harvest of vegetables: ", self.screen, [20, 110], 26, WHITE, FONT)
        self.draw_text(str(self.garden.harvest_of_vegetables), self.screen, [300, 110], 26, WHITE, FONT)
        self.draw_text("died from hungry: ", self.screen, [20, 150], 26, WHITE, FONT)
        self.draw_text(str(self.garden.died_from_hungry), self.screen, [250, 150], 26, WHITE, FONT)
        self.draw_text("died from pests: ", self.screen, [20, 190], 26, WHITE, FONT)
        self.draw_text(str(self.garden.died_from_pests), self.screen, [250, 190], 26, WHITE, FONT)
        self.add_button_back(20, 230)
        event = pygame.event.get()
        pygame_widgets.update(event)
        pygame.display.update()
        pygame_widgets.WidgetHandler._widgets.clear()

    ########################     HELP FUNCTIONS     ########################

    def draw_text(self, words, screen, position, size, colour, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centered:
            position[0] = position[0] - text_size[0] // 2
            position[1] = position[1] - text_size[1] // 2
        screen.blit(text, position)

    ########################     BUTTONS     ########################

    def draw_buttons(self):
        self.add_button_next_day(20, 540)
        self.add_button_add_plant(650, 60)
        self.add_button_add_tree(650, 120)
        self.add_button_weeding(650, 180)
        self.add_button_delete_pests(650, 240)
        self.add_button_help_plants(650, 300)
        self.add_button_water_plants(650, 360)
        self.add_button_garden_info(650, 420)
        self.add_button_info(650, 480)
        self.add_button_save(650, 540)

    def add_button_start_garden(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             860,
                             40,
                             text='Garden simulator',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_start_garden)

    def button_start_garden(self):
        self.garden = World([1, 2])
        count_of_plants = 2
        count_of_pests = 1
        count_of_trees = 2
        for i in range(0, count_of_pests):
            self.garden.add_pests_on_game_map()
        for i in range(0, count_of_plants):
            self.garden.add_plant_on_game_map()
        for i in range(0, count_of_trees):
            self.garden.add_trees_on_game_map()
        for i in range(0, count_of_pests):
            self.garden.add_pests_on_game_map()
        for i in range(0, count_of_plants):
            self.garden.add_plant_on_game_map()
        self.garden.step_print()
        self.garden.commands("next_day")
        self.garden.step_print()
        print(str(self.garden.weather.parameters["weather_is"]))
        self.state = 'next_day'
        print(str(self.garden.count_of_global_days))

    def add_button_next_day(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             600,
                             45,
                             text='next day',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_next_day)

    def button_next_day(self):
        self.garden.commands("next_day")
        self.garden.step_print()
        print(str(self.garden.weather.parameters["weather_is"]))
        self.state = 'next_day'
        print(str(self.garden.count_of_global_days))

    def add_button_add_plant(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             200,
                             45,
                             text='add plant',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_add_plant)

    def button_add_plant(self):
        self.garden.commands("add_plant")
        self.state = 'next_day'
        self.garden.step_print()

    def add_button_add_tree(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             200,
                             45,
                             text='add tree',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_add_tree)

    def button_add_tree(self):
        self.garden.commands("add_tree")
        self.state = 'next_day'
        self.garden.step_print()

    def add_button_delete_pests(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             200,
                             45,
                             text='delete pests',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_delete_pests)

    def button_delete_pests(self):
        self.garden.commands("delete_pests")
        self.state = 'next_day'
        self.garden.step_print()

    def add_button_weeding(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             200,
                             45,
                             text='weeding',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_weeding)

    def button_weeding(self):
        self.garden.commands("weeding")
        self.state = 'next_day'
        self.garden.step_print()

    def add_button_help_plants(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             200,
                             45,
                             text='help plants',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_help_plants)

    def button_help_plants(self):
        self.garden.fertilizing_game_map()
        self.garden.step_print()

    def add_button_water_plants(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             200,
                             45,
                             text='water plants',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_water_plants)

    def button_water_plants(self):
        self.garden.commands("water_plants")
        self.garden.step_print()

    def add_button_help_plants(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             200,
                             45,
                             text='help plants',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_help_plants)

    def button_help_plants(self):
        self.garden.commands("help_plants")

    def add_button_info(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             200,
                             45,
                             text='info',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_info)

    def button_info(self):
        print("info")
        self.garden.step_print()

    def add_button_garden_info(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             200,
                             45,
                             text='garden info',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_garden_info)

    def button_garden_info(self):
        print("garden info")
        self.state = "garden_info"

    def add_button_save(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             200,
                             45,
                             text='save',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_save)

    def button_save(self):
        self.garden.commands("save")

    def add_button_back(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             200,
                             45,
                             text='back',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_back)

    def button_back(self):
        self.state = "next_day"
