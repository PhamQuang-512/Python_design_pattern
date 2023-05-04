from abc import ABC, abstractmethod


class TemplateComputer(ABC):
    def __init__(self, name: str):
        self._name: str = name

    @abstractmethod
    def battery_left(self) -> bool:
        pass

    def turn_on(self) -> None:
        print(f"{self._name} Turning on")

    def use(self) -> None:
        print(f"using computer: {self._name}")

    def turn_off(self) -> None:
        print(f"{self._name}Turning off")

    def go(self):
        self.turn_on()
        if self.battery_left():
            self.use()
        self.turn_off()

    @property
    def name(self):
        return self._name


class Laptop(TemplateComputer):
    def __init__(self):
        super().__init__('laptop')

    def battery_left(self) -> bool:
        return False


class Desktop(TemplateComputer):
    def __init__(self):
        super().__init__('desktop')

    def battery_left(self) -> bool:
        return True


if __name__ == '__main__':
    laptop = Laptop()
    laptop.go()

    desktop = Desktop()
    desktop.go()
