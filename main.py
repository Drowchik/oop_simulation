from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, coord) -> None:
        self.coord = coord


class Grass(Entity):
    def __init__(self, coord) -> None:
        super().__init__(coord)
        self.sprite = "G"


class Rock(Entity):
    def __init__(self, coord) -> None:
        super().__init__(coord)
        self.sprite = "R"


class Tree(Entity):
    def __init__(self, coord) -> None:
        super().__init__(coord)
        self.sprite = "T"


class Creature(Entity, ABC):
    def __init__(self, speed, health, sprite, coord) -> None:
        super.__init__(coord)
        self.speed = speed
        self.health = health
        self.sprite = sprite

    @abstractmethod
    def makeMove():
        pass


class Herbivore(Creature):
    def __init__(self, speed, health) -> None:
        super().__init__(speed, health)

    def makeMove():
        pass


class Predator(Creature):
    def __init__(self, speed, health, power) -> None:
        super().__init__(speed, health)
        self.power = power

    def makeMove():
        pass

    def atack():
        pass


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


class Map:
    def __init__(self, height: int, width: int) -> None:
        if isinstance(height, int) and isinstance(width, int):
            self.height = height
            self.width = width
        self.map_coord_dict = {}

    def add_object(self, object, x: int, y: int):
        point = Point(x, y)
        self.map_coord_dict[point] = object
        return self.map_coord_dict[point]

    def map_size(self):
        return self.height, self.width

    def delete_obj(self, x, y):
        point = Point(x, y)
        del self.map_coord_dict[point]

    def get_object(self, x, y):
        point = Point(x, y)
        return self.map_coord_dict[point]


class Simulation:
    def __init__(self) -> None:
        pass
