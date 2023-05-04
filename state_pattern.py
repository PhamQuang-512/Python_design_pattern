from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def handle_request(self):
        pass


class NewState(State):
    def handle_request(self):
        print("Creating new document")


class SubmittedState(State):
    def handle_request(self):
        print("Submitted")


class ApprovedState(State):
    def handle_request(self):
        print("Approved")


class RejectedState(State):
    def handle_request(self):
        print("Rejected")


class Document:
    def __init__(self):
        self.__state: State = NewState()

    def set_state(self, state: State):
        self.__state = state

    def apply_state(self):
        self.__state.handle_request()


if __name__ == '__main__':
    document = Document()
    document.apply_state()

    document.set_state(SubmittedState())
    document.apply_state()

    document.set_state(RejectedState())
    document.apply_state()
