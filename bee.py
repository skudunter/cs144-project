from compass import Compass
import math


class Bee:
    def __init__(self, row: int, col: int, speed: int, perception: int,home_hive = None):
        self.icon = 'b'
        self.row = row
        self.col = col
        self.compass = Compass(row, col, speed)
        self.flower = None
        self.perception = perception
        self.home_hive = home_hive
        self.pollen = None

    def get_next_move(self):
        if (self.flower is None) and (self.pollen == None):
            return self.do_random_walk()
        elif (self.flower is not None) and (self.pollen == None):
            return self.do_perception_walk()
        elif self.pollen != None:
            return self.do_walk_to_hive()

    def do_random_walk(self):
        next_trajectory = self.compass.get_next_trajectory()
        displacement = convert_radian_to_tuple(
            next_trajectory.get_direction_in_radians())
        distance = next_trajectory.get_distance()
        new_col, new_row = int(
            displacement[0] * distance), int(displacement[1] * distance)
        return new_row + self.row, new_col + self.col

    def do_perception_walk(self):
        if self.flower is None:
            return 
        
        flower = self.flower
        flower_row, flower_col = flower.row, flower.col
        steps = self.compass.get_next_trajectory().get_distance()
        
        if self.row != flower_row and self.col != flower_col:
            if flower_row > self.row:
                self.row += 1  
            else:
                self.row -= 1  
            
            if flower_col > self.col:
                self.col += 1  
            else:
                self.col -= 1  

            steps -= 1  

        while steps > 0:
            if self.row != flower_row:
                if flower_row > self.row:
                    self.row += 1  
                else:
                    self.row -= 1  
        
            elif self.col != flower_col:
                if flower_col > self.col:
                    self.col += 1  
                else:
                    self.col -= 1  
            
            steps -= 1 
        
        
        return self.row, self.col

        
    def do_walk_to_hive(self):
        hive_row, hive_col = self.home_hive.get_position()
        row, col = self.compass.get_position()
        if abs(hive_row - row) <= self.perception and abs(hive_col - col) <= self.perception:
            return self.do_random_walk()
        else:
            return self.do_walk_to_hive()

class Wasp(Bee):
    def __init__(self, row: int, col: int, speed: int):
        super().__init__(row, col, speed, perception=0,home_hive=None)
        self.icon = 'w'


class HoneyBee(Bee):
    def __init__(self, row: int, col: int, speed: int, perception: int,home_hive=None):
        super().__init__(row, col, speed, perception,home_hive=None)
        self.icon = 'h'


class DesertBee(Bee):
    def __init__(self, row: int, col: int, speed: int, perception: int,home_hive=None):
        super().__init__(row, col, speed, perception,home_hive=None)
        self.icon = 'd'


def convert_radian_to_tuple(radians):
    return (round(math.cos(radians)), round(math.sin(radians)))
