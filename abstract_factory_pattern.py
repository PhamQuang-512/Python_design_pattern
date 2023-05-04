from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def push(self):
        pass


class ScrollBar(ABC):
    @abstractmethod
    def scroll(self):
        pass


class LightButton(Button):
    def push(self):
        print("Light Button")


class DarkButton(Button):
    def push(self):
        print("Dark Button")


class LightScrollBar(ScrollBar):
    def scroll(self):
        print("Light Scrollbar")


class DarkScrollBar(ScrollBar):
    def scroll(self):
        print("Dark Scrollbar")


class WidgetFactory(ABC):
    @abstractmethod
    def create_scrollbar(self) -> ScrollBar:
        pass

    @abstractmethod
    def create_button(self) -> Button:
        pass


class LightWidgetFactory(WidgetFactory):
    def create_scrollbar(self) -> ScrollBar:
        return LightScrollBar()

    def create_button(self) -> Button:
        return LightButton()


class DarkWidgetFactory(WidgetFactory):
    def create_scrollbar(self) -> ScrollBar:
        return DarkScrollBar()

    def create_button(self) -> Button:
        return DarkButton()


if __name__ == '__main__':
    type = input()
    factory = None

    if type == 'l':
        factory = LightWidgetFactory()
    elif type == 'd':
        factory = DarkWidgetFactory()
    else:
        factory = LightWidgetFactory()

    button = factory.create_button()
    button.push()

    scrollbar = factory.create_scrollbar()
    scrollbar.scroll()
