from abc import ABC, abstractmethod
import copy


class HousePlan(ABC):
    @abstractmethod
    def set_basement(self, basement: str) -> None:
        pass

    @abstractmethod
    def set_structure(self, structure: str) -> None:
        pass

    @abstractmethod
    def set_roof(self, roof: str) -> None:
        pass

    @abstractmethod
    def set_interior(self, interior: str) -> None:
        pass


class House(HousePlan):
    def __init__(self):
        self._basement: str = ''
        self._structure: str = ''
        self._roof: str = ''
        self._interior: str = ''

    def set_basement(self, basement: str) -> None:
        self._basement = basement

    def set_structure(self, structure: str) -> None:
        self._structure = structure

    def set_roof(self, roof: str) -> None:
        self._roof = roof

    def set_interior(self, interior: str) -> None:
        self._interior = interior

    def __str__(self) -> str:
        return f"House: {self._basement} | {self._structure} | {self._roof} | {self._interior}"


class HouseBuilder(ABC):
    @abstractmethod
    def build_basement(self) -> None:
        pass

    @abstractmethod
    def build_structure(self) -> None:
        pass

    @abstractmethod
    def build_roof(self) -> None:
        pass

    @abstractmethod
    def build_interior(self) -> None:
        pass

    @abstractmethod
    def get_house(self) -> House:
        pass


class IglooHouseBuilder(HouseBuilder):
    def __init__(self):
        self._house: House = House()

    def build_basement(self) -> None:
        self._house.set_basement("Ice bars")

    def build_structure(self) -> None:
        self._house.set_structure("Ice blocks")

    def build_roof(self) -> None:
        self._house.set_roof("Ice carvings")

    def build_interior(self) -> None:
        self._house.set_interior("Ice dome")

    def get_house(self) -> House:
        return self._house


class TipiHouseBuilder(HouseBuilder):
    def __init__(self):
        self._house: House = House()

    def build_basement(self) -> None:
        self._house.set_basement("Wooden poles")

    def build_structure(self) -> None:
        self._house.set_structure("Wood and ice")

    def build_roof(self) -> None:
        self._house.set_roof("Fire wood")

    def build_interior(self) -> None:
        self._house.set_interior("Wood, caribou and seal skins")

    def get_house(self) -> House:
        return self._house


class CivilEngineer:
    def __init__(self, house_builder: HouseBuilder):
        self._house_builder: HouseBuilder = house_builder
        self.hi = ""

    def get_house(self) -> House:
        return self._house_builder.get_house()

    def construct_house(self) -> None:
        self._house_builder.build_basement()
        self._house_builder.build_structure()
        self._house_builder.build_roof()
        self._house_builder.build_interior()

    def set_builder(self, builder: HouseBuilder):
        self._house_builder = builder


if __name__ == '__main__':
    igloo_house_builder = IglooHouseBuilder()
    civil_engineer = CivilEngineer(igloo_house_builder)
    civil_engineer.construct_house()
    house = civil_engineer.get_house()
    print(house)
    print(id(house))

    house2 = igloo_house_builder.get_house()
    print(id(house2))

    tipi_house_builder = TipiHouseBuilder()
    civil_engineer.set_builder(tipi_house_builder)
    civil_engineer.construct_house()
    house = civil_engineer.get_house()
    print(house)
    print(id(house))
