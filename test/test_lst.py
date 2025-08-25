from typing import Callable

from pytest import raises

# Todo:
# - ability to register a new observer
# - ability to call the listener, and when that happens, the observers should be called
# - ability to pass some argument or an event from the caller to the observer
#
# Done:
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

class EventListener[Key]:
    def add(self, key: Key, observer: Callable):
        raise NotCallable()

    def send(self, key: Key):
        raise NotRegistered()

class NotRegistered(Exception):
    pass

class NotCallable(Exception):
    pass
