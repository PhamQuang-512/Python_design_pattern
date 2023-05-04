from __future__ import annotations


class Singleton:
    _instance = None

    @staticmethod
    def get_instance() -> Singleton:
        """ Static access method. """
        if Singleton._instance is None:
            Singleton()
        return Singleton._instance

    def __init__(self):
        self.name = "singleton"
        if Singleton._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            # for case init with Singleton() but not Singleton.get_instance()
            Singleton._instance = self


if __name__ == '__main__':
    s = Singleton()
    print(s)

    s = Singleton.get_instance()
    print(s)

    ss = Singleton.get_instance()
    print(ss)
