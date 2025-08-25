from typing import Callable

from pytest import raises

# Todo:
# - ability to call the listener, and when that happens, the observers should be called
# - ability to pass some argument or an event from the caller to the observer
#
# Done:
# - ability to register a new observer
# - if trying to register an observer that's not callable, throw exception
# - if trying to call a listener that's not registered, throw exception

def test_if_trying_to_call_observer_that_is_not_registered__throw_exception():
    listener = EventListener()
    with raises(NotRegistered):
        listener.send('not registered')

def test_if_trying_to_register_an_observer_that_is_not_callable__throw_exception():
    listener = EventListener()
    not_callable = 0  # anything that is not a callable
    with raises(NotCallable):
        listener.add('key', not_callable)

def test_register_a_new_observer():
    listener = EventListener()
    listener.add('registered', lambda: None)
    listener.send('registered')

class EventListener[Key]:
    def __init__(self):
        self.observers: list[Key] = []

    def add(self, key: Key, observer: Callable):
        if not callable(observer):
            raise NotCallable()
        self.observers.append(key)

    def send(self, key: Key):
        if key not in self.observers:
            raise NotRegistered()

class NotRegistered(Exception):
    pass

class NotCallable(Exception):
    pass
