from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, name: str):
        self.__name = name

    @abstractmethod
    def show_property(self) -> str:
        pass

    @property
    def name(self):
        return self.__name


class File(Component):
    def show_property(self) -> str:
        return f"File({self.name})"


class Folder(Component):
    def __init__(self, name: str):
        super().__init__(name)
        self.__children: list[Component] = []

    def show_property(self) -> str:
        return "Folder({name}): [{children}]".format(
            children=" | ".join([child.show_property() for child in self.__children]), name=self.name)

    def get_children(self):
        return self.__children

    def add(self, child: Component):
        if child not in self.__children:
            self.__children.append(child)


if __name__ == '__main__':
    file1 = File('file1')
    file2 = File('file2')
    folder1 = Folder('folder1')
    folder1.add(file1)
    folder1.add(file2)

    folder2 = Folder('folder2')
    file3 = File('file3')
    folder2.add(file3)
    folder2.add(folder1)
    print(folder2.show_property())
