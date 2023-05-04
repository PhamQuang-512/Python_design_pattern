from __future__ import annotations
from abc import abstractmethod, ABC
import datetime


class IEmployee(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def do_task(self) -> None:
        pass

    def show_basic_info(self) -> None:
        print("------")
        print("Basic info of ", self.name)

    @property
    @abstractmethod
    def name(self) -> str:
        pass


class Employee(IEmployee):
    def __init__(self, name: str) -> None:
        self._name = name

    def do_task(self) -> None:
        print(f"{self.name} is doing his job")

    @property
    def name(self):
        return self._name


class EmployeeDecorator(IEmployee):
    @property
    def name(self) -> str:
        return self._employee.name

    @property
    def employee(self):
        return self._employee

    @abstractmethod
    def __init__(self, _employee: IEmployee) -> None:
        self._employee = _employee


class TeamMember(EmployeeDecorator):
    def do_task(self) -> None:
        self.employee.do_task()

    def __init__(self, _employee: IEmployee) -> None:
        super().__init__(_employee)

    def report_task(self):
        print(f"{self.name} is reporting task!")

    def coordinate_with_others(self):
        print(f"{self.name} is coordinating with other members of his team.")


class TeamLeader(EmployeeDecorator):

    def do_task(self) -> None:
        self.employee.do_task()
        self.planning()
        self.motivate()
        self.monitor()

    def __init__(self, _employee: IEmployee) -> None:
        super().__init__(_employee)

    def planning(self):
        print(f"{self.name} is planning")

    def motivate(self):
        print(f"{self.name} is motivating his members")

    def monitor(self):
        print(f"{self.name} is monitoring his members")


class Manager(EmployeeDecorator):
    def create_requirement(self):
        print(f"{self.name} is creating requirement")

    def assign_task(self):
        print(f"{self.name} is assigning new task")

    def manage_progress(self):
        print(f"{self.name} is managing the progress")

    def do_task(self) -> None:
        self.employee.do_task()
        self.create_requirement()
        self.assign_task()
        self.manage_progress()

    def __init__(self, _employee: IEmployee) -> None:
        super().__init__(_employee)


if __name__ == '__main__':
    employee = Employee("John")
    employee = TeamMember(employee)
    employee.do_task()

    print("")

    employee = TeamLeader(employee)
    employee.do_task()

    print("")

    employee = Manager(employee)
    employee.do_task()
