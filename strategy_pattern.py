from abc import ABC, abstractmethod


class GoAlgorithm(ABC):
    @abstractmethod
    def go(self) -> None:
        pass


class GoByDriving(GoAlgorithm):
    def go(self) -> None:
        print("driving")


class GoByFlying(GoAlgorithm):
    def go(self) -> None:
        print("flying")


class GoByFlyingFast(GoAlgorithm):
    def go(self) -> None:
        print("flying fast")


class Vehicle(ABC):
    def __init__(self, name) -> None:
        self.go_algorithm: GoAlgorithm | None = None
        self.name: str = name

    def set_go_algorithm(self, algorithm: GoAlgorithm) -> None:
        self.go_algorithm = algorithm

    def go(self) -> None:
        print(f"{self.name}: ", end="")
        self.go_algorithm.go()


class Car(Vehicle):
    def __init__(self) -> None:
        super().__init__('car')
        self.set_go_algorithm(GoByDriving())


class Helicopter(Vehicle):
    def __init__(self) -> None:
        super().__init__('helicopter')
        self.set_go_algorithm(GoByDriving())


class Jet(Vehicle):
    def __init__(self) -> None:
        super().__init__('jet')
        self.set_go_algorithm(GoByDriving())


if __name__ == '__main__':
    car = Car()
    car.go()

    helicopter = Helicopter()
    helicopter.go()
    helicopter.set_go_algorithm(GoByFlying())
    helicopter.go()

    jet = Jet()
    jet.go()
    jet.set_go_algorithm(GoByFlying())
    jet.go()
    jet.set_go_algorithm(GoByFlyingFast())
    jet.go()
