from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, coord) -> None:
        self.coord = coord


class Grass(Entity):
    def __init__(self, sprite, coord) -> None:
        super().__init__(coord)
        self.sprite = sprite


class Rock(Entity):
    def __init__(self, sprite, coord) -> None:
        super().__init__(coord)
        self.sprite = sprite


class Tree(Entity):
    def __init__(self, sprite, coord) -> None:
        super().__init__(coord)
        self.sprite = sprite


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
