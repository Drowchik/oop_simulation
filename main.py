from abc import ABC, abstractmethod


class Point:
    def __init__(self, x: int, y: int) -> None:
        if isinstance(x, int) and isinstance(y, int):
            self.x = x
            self.y = y

    def __eq__(self, other) -> bool:
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self) -> int:
        return hash((self.x, self.y))


class Entity(ABC):
    def __init__(self, coord: Point, sprite: str) -> None:
        self.coord = coord
        self.sprite = sprite


class Grass(Entity):
    def __init__(self, coord, sprite="G") -> None:
        super().__init__(coord, sprite)


class Rock(Entity):
    def __init__(self, coord, sprite="R") -> None:
        super().__init__(coord, sprite)


class Tree(Entity):
    def __init__(self, coord, sprite="T") -> None:
        super().__init__(coord, sprite)


class Creature(Entity, ABC):
    def __init__(self, speed, health, coord, sprite) -> None:
        super.__init__(coord, sprite)
        self.speed = speed
        self.health = health

    @abstractmethod
    def makeMove(self, map):
        pass


class Herbivore(Creature):
    def __init__(self, speed, health, coord, sprite="H") -> None:
        super().__init__(speed, health, sprite, coord)

    def makeMove():
        """ Если путь больше 1, то мы идём, если меньше, то мы кушаем травку

        Returns:
            _type_: _description_
        """


class Predator(Creature):
    def __init__(self, speed, health, power, coord, sprite="P") -> None:
        super().__init__(speed, health, sprite, coord)
        self.power = power

    def makeMove():
        pass

    def atack(self, obj: Herbivore, map):
        if Herbivore.health <= self.power:
            map.delete_obj(Herbivore.coord)
        else:
            obj.health -= self.power


class Map:
    def __init__(self, height: int, width: int) -> None:
        if isinstance(height, int) and isinstance(width, int):
            self.height = height
            self.width = width
        self.map_coord_dict = dict()

    def add_object(self, obj: Entity):
        point = obj.coord
        self.map_coord_dict[point] = obj
        return self.map_coord_dict[point]

    def map_size(self):
        return self.height, self.width

    def delete_obj(self, point):
        del self.map_coord_dict[point]

    def get_object(self, x, y):
        point = Point(x, y)
        return self.map_coord_dict[point]


class Simulation:
    def __init__(self, height, weight) -> None:
        self.height = height
        self.weight = weight
        self.matrix = Map(self.height, self.weight)
        self.render = Render(self.matrix)

    def next_turn():
        pass

    def start_simulation(self):
        a = Tree(Point(0, 2))
        b = Rock(Point(4, 4))
        self.matrix.add_object(a)
        self.matrix.add_object(b)
        self.render.draw()

    def pause_simulation():
        pass


class Actions:
    def init_actions():
        pass

    def turn_actions():
        pass


class Render:
    def __init__(self, maps: Map, counter=None):
        self.map_coord = maps
        self.counter = counter

    @staticmethod
    def print_info():
        dict_info_object = {
            'P': 'predator',
            'H': 'herbivores',
            'G': 'grass',
            'R': 'rock',
            'T': 'tree',
        }
        for key, value in dict_info_object.items():
            print(f'{key} - {value}')
        print()

    def draw(self):
        for i in range(self.map_coord.width):
            for j in range(self.map_coord.height):
                if self.map_coord.map_coord_dict.get(Point(i, j), False):
                    print(
                        "|" + self.map_coord.map_coord_dict[Point(i, j)].sprite + "|", end="")
                else:
                    print("| |", end="")
            print()


if __name__ == "__main__":
    a = Simulation(10, 10)
    a.start_simulation()
