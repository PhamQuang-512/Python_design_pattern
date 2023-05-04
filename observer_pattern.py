from __future__ import annotations
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, operation: str, record: int) -> None:
        pass


class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def unregister_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass


class Database(Subject):
    _instance: Database | None = None

    def __init__(self) -> None:
        if Database._instance is not None:
            raise Exception("this is singleton!!!")
        else:
            Database._instance = self
            self._observers: list[Observer] = []
            self._operation: str = ""
            self._record: int = 0

    @classmethod
    def get_instance(cls) -> Database:
        if Database._instance is None:
            Database()
        return Database._instance

    @property
    def observers(self) -> list[Observer]:
        return self._observers

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self._operation, self._record)

    def unregister_observer(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def register_observer(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def delete_record(self, record: int):
        self._operation = "delete"
        self._record = record
        self.notify_observers()

    def update_record(self, record: int):
        self._operation = "update"
        self._record = record
        self.notify_observers()


class Client(Observer):

    def update(self, operation: str, record: int) -> None:
        print(f"Client: {operation} | {record}")


class Dev(Observer):

    def update(self, operation: str, record: int) -> None:
        print(f"Dev: {operation} | {record}")


class Boss(Observer):

    def update(self, operation: str, record: int) -> None:
        print(f"Boss: {operation} | {record}")


if __name__ == "__main__":
    db = Database.get_instance()
    client = Client()
    dev = Dev()
    db.register_observer(client)
    db.register_observer(dev)
    db.delete_record(2)

    print("")

    boss = Boss()
    db.register_observer(boss)
    db.update_record(32)

    print("")

    db.unregister_observer(client)
    db.delete_record(23)
