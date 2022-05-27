from tree_class import Tree
from vegetable_class import Carrot
from pest_class import Pest
from weather_class import Weather
import random
import pickle


class World:
    class Cell:
        coordinates = tuple()
        all_in_cell = list()  # не только растения
        list_for_print = list()

        def __init__(self, coordinates):
            self._coordinates = coordinates
            self.all_in_cell = list()
            self.list_for_print = list()

        def add_plant_on_cell(self, plant):  # любая сущность
            if len(self.all_in_cell) < 4:
                self.all_in_cell.append(plant)
                self.list_for_print.append(plant.parameters["symbol_on_map"])
            else:
                return

        def check_to_add_in_cell(self):
            if len(self.all_in_cell) < 4:
                return True
            else:
                return False

        def print_cell(self):
            if len(self.list_for_print) != 0:
                return self.list_for_print
            else:
                return "*"

        def remove_smth_from_cell(self, smth):
            self.all_in_cell.remove(smth)
            self.list_for_print.remove(smth.parameters["symbol_on_map"])

    game_map = list()
    map_size = tuple()
    plants = list()
    weather = Weather()
    step = 0
    harvest_of_vegetables = 0
    harvest_of_apples = 0
    died_from_pests = 0
    died_from_hungry = 0
    died_from_illness = 0
    weather_today_is = ""  # погодка

    def __init__(self, map_size):
        self.map_size = map_size
        for i in range(0, map_size[0]):
            row = list()
            for j in range(0, map_size[1]):
                row.append(World.Cell([i, j]))
            self.game_map.append(row)

    #def check_to_add_in_cell(self):
    def find_plant_position(self):
        x = random.randint(0, self.map_size[0] - 1)
        y = random.randint(0, self.map_size[1] - 1)
        if self.game_map[x][y].check_to_add_in_cell() is False:
            return self.find_plant_position()
        else:
            position = (x, y)
            return position

    def check_to_add(self):
        a = int(self.map_size[0])
        b = int(self.map_size[1])
        if len(self.plants) >= 4 * a * b:
            return False
        else:
            return True

    def add_pests_on_game_map(self):
        if self.check_to_add() is True:
            new_pest = Pest(self.find_plant_position(), self)
            self.plants.append(new_pest)
            x = int(new_pest.parameters["coordinates"][0])
            y = int(new_pest.parameters["coordinates"][1])
            self.game_map[x][y].add_plant_on_cell(new_pest)
        else:
            print("No place!")

    def add_plant_on_game_map(self):
        if self.check_to_add() is True:
            new_plant = Carrot(self.find_plant_position(), self)
            self.plants.append(new_plant)
            x = int(new_plant.parameters["coordinates"][0])
            y = int(new_plant.parameters["coordinates"][1])
            self.game_map[x][y].add_plant_on_cell(new_plant)
        else:
            print("No place!")

    def add_trees_on_game_map(self):
        if self.check_to_add() is True:
            new_plant = Tree(self.find_plant_position(), self)
            self.plants.append(new_plant)
            x = int(new_plant.parameters["coordinates"][0])
            y = int(new_plant.parameters["coordinates"][1])
            self.game_map[x][y].add_plant_on_cell(new_plant)
        else:
            print("No place!")

    def step_print(self):
        for row in self.game_map:
            for Cell in row:
                print(Cell.print_cell())
            # print("")

    def aging_in_map(self):
        for smth in self.plants:
            smth = smth.aging()
            if smth is not None:
                self.plants.remove(smth)
                smth.get_position()
                x = int(smth.parameters["coordinates"][0])
                y = int(smth.parameters["coordinates"][1])
                self.game_map[x][y].remove_smth_from_cell(smth)

    def plants_grow_up(self):
        for smth in self.plants:
            if smth.parameters["type_id"] == 1:
                if self.weather.parameters["weather_is"] == "sun":
                    smth = smth.get_rid_of_illness_check()
                    smth = smth.grow_up()
                if self.weather.parameters["weather_is"] == "rain":
                    smth = smth.get_illness_check()
                    smth = smth.grow_up()
                if self.weather.parameters["weather_is"] == "drought":
                    if not smth.parameters["watered"]:  # если не полито, то -10 хп и никакого роста
                        smth.parameters["life_points"] -= 10
                    if smth.parameters["watered"]:  # если полито, растём
                        smth = smth.grow_up()
                if smth is not None:
                    self.harvest_of_vegetables += 1
                    self.plants.remove(smth)
                    smth.get_position()
                    x = int(smth.parameters["coordinates"][0])
                    y = int(smth.parameters["coordinates"][1])
                    self.game_map[x][y].remove_smth_from_cell(smth)

    def trees_grow_up(self):
        for tree in self.plants:
            if tree.parameters["type_id"] == 3:
                if self.weather.parameters["weather_is"] == "sun":
                    tree = tree.get_rid_of_illness_check()
                    tree = tree.grow_up()
                if self.weather.parameters["weather_is"] == "rain":
                    tree = tree.get_illness_check()
                    tree = tree.grow_up()
                if self.weather.parameters["weather_is"] == "drought":
                    if not tree.parameters["watered"]:  # если не полито, то -20 хп и никакого роста
                        tree.parameters["life_points"] -= 20
                    if tree.parameters["watered"]:  # если полито, растём
                        tree = tree.grow_up()
                    if tree is not None:
                        self.harvest_of_apples += 1

    def eat_plant_on_map(self):
        for pests in self.plants:
            if pests.parameters["type_id"] == 2:
                pests.get_position()
                for plant_for_eat in self.plants:
                    if plant_for_eat.parameters["type_id"] == 1:
                        plant_for_eat.get_position()
                        if int(plant_for_eat.parameters["coordinates"][0]) == int(pests.parameters["coordinates"][0])\
                                and int(plant_for_eat.parameters["coordinates"][1]) == int(pests.parameters["coordinates"][1]):
                            plant_for_eat = pests.attack_plant(plant_for_eat)
                            if plant_for_eat is not None:
                                self.died_from_pests += 1
                                self.plants.remove(plant_for_eat)
                                self.game_map[int(plant_for_eat.parameters["coordinates"][0])][
                                     int(plant_for_eat.parameters["coordinates"][1])].remove_smth_from_cell(plant_for_eat)

    def damage_trees_on_map(self):
        for pests in self.plants:
            if pests.parameters["type_id"] == 3:
                pests.get_position()
                for plant_for_eat in self.plants:
                    if plant_for_eat.parameters["type_id"] == 1:
                        plant_for_eat.get_position()
                        if int(plant_for_eat.parameters["coordinates"][0]) == int(pests.parameters["coordinates"][0])\
                                and int(plant_for_eat.parameters["coordinates"][1]) == int(pests.parameters["coordinates"][1]):
                            plant_for_eat = pests.attack_plant(plant_for_eat)
                            if plant_for_eat is not None:
                                self.died_from_pests += 1
                                self.plants.remove(plant_for_eat)
                                self.game_map[int(plant_for_eat.parameters["coordinates"][0])][
                                    int(plant_for_eat.parameters["coordinates"][1])].remove_smth_from_cell(plant_for_eat)

    def opportunity_to_live_on_map(self):
        for smth in self.plants:
            if smth.parameters["type_id"] == 2:
                smth = smth.opportunity_to_live()
                if smth is not None:
                    smth.get_position()
                    x = int(smth.parameters["coordinates"][0])
                    y = int(smth.parameters["coordinates"][1])
                    self.game_map[x][y].remove_smth_from_cell(smth)
                    self.plants.remove(smth)
                    self.died_from_hungry += 1

    def everydays_hungry(self):
        for pests in self.plants:
            if pests.parameters["type_id"] == 2:
                pests.parameters["hungry"] = True

    def weather_today(self):
        self.weather.what_weather_today()
        if self.weather.parameters["weather_is"] == "sun" or self.weather.parameters["weather_is"] == "drought":
            for smth in self.plants:
                smth.parameters["watered"] = False
        if self.weather.parameters["weather_is"] == "rain":
            for smth in self.plants:
                smth.parameters["watered"] = True
        return self.weather.parameters["weather_is"]

    def watering_in_map(self):
        for smth in self.plants:
            if smth.parameters["type_id"] == 1 or smth.parameters["type_id"] == 3:
                smth = smth.water()
        print("Plants watered!")  # чекаем сработало ли

    def want_to_water_plants(self):
        print("weather today:", self.weather.parameters["weather_is"])
        command = ""
        while command != "y" or command != "n":
            command = input("water plants? y/n\n")
            try:
                if command == "y":
                    self.commands("water_plants")
                    break
                elif command == "n":
                    print("no water")
                    break
                else:
                    raise()
            except:
                print("Wrong command!")

    def life_cycle(self):
        self.weather_today()
        self.want_to_water_plants()
        self.plants_grow_up()
        self.trees_grow_up()
        self.eat_plant_on_map()
        self.aging_in_map()
        self.opportunity_to_live_on_map()
        self.everydays_hungry()
#        print("умерли от вредителей", self.died_from_pests)
#        print("умерло от голода", self.died_from_hungry)
#        print("урожай овощей", self.harvest_of_vegetables)
#        print("урожай яблок", self.harvest_of_apples)

    def step_save(self):
        file = open(r'saved_game.txt', 'wb')
        pickle.dump(self, file)
        for i in range(self.map_size[0]):  # по строке
            for j in range(self.map_size[1]):
                pickle.dump(self.game_map[i][j], file)
        for smth in self.plants:
            pickle.dump(smth, file)
        file.close()
        # print("garden is saved")

    def commands(self, command):
        try:
            # command = command.split(" ")
            if command == "garden_info":
                print("died from pests", self.died_from_pests)
                print("died from hungry", self.died_from_hungry)
                print("harvest of vegetables", self.harvest_of_vegetables)
                print("harvest of fruits", self.harvest_of_apples)
            elif command == "next_day":
                self.life_cycle()
            elif command == "add_plant":
                self.add_plant_on_game_map()
            elif command == "add_tree":
                self.add_trees_on_game_map()
            elif command == "add_pests":
                self.add_pests_on_game_map()
            elif command == "water_plants":
                self.watering_in_map()
            else:
                raise()
            self.step_save()
        except:
            print("Wrong command")
