from abc import ABC, abstractmethod


class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass


class Sparrow(Bird):
    def fly(self):
        print("flying")

    def make_sound(self):
        print("Chirp Chirp")


class ToyDuck(ABC):
    @abstractmethod
    def squeak(self):
        pass


class PlasticToyDuck(ToyDuck):

    def squeak(self):
        print("Squeak")


class BirdToToyDuckAdapter(ToyDuck):
    def __init__(self, bird: Bird):
        self._bird: Bird = bird

    def squeak(self):
        self._bird.make_sound()


if __name__ == '__main__':
    bird = Sparrow()
    bird.make_sound()

    toy_duck = PlasticToyDuck()
    toy_duck.squeak()

    p_toy_duck = BirdToToyDuckAdapter(bird)
    p_toy_duck.squeak()
    pass
