from typing import Callable

from pytest import raises

# Done:
# - ability to call the listener, and when that happens, the observers should be called
# - ability to pass some argument or an event from the caller to the observer
# - ability to register a new observer
# - if trying to register an observer that's not callable, throw exception
# - if trying to call a listener that's not registered, throw exception

def test_fail_when_called_not_registered_observer():
    listener = EventListener()
    with raises(NotRegistered):
        listener.send('not registered', None)

def test_fail_when_registering_non_callable_observer():
    listener = EventListener()
    not_callable = 0  # anything that is not a callable
    with raises(NotCallable):
        listener.add('key', not_callable)

def test_register_a_new_observer():
    listener = EventListener()
    listener.add('registered', lambda event: None)
    listener.send('registered', None)

def test_call_observer_when_the_listener_is_sent_an_event():
    was_called = [False]

    def observer(event):
        was_called[0] = True

    listener = EventListener()
    listener.add('registered', observer)
    listener.send('registered', None)
    assert was_called[0]

def test_pass_event_from_caller_to_the_observer():
    called_argument = [None]

    def observer(argument):
        called_argument[0] = argument

    listener = EventListener()
    listener.add('registered', observer)
    listener.send('registered', 'my argument')
    assert called_argument[0] == 'my argument'

class EventListener[Key]:
    def __init__(self):
        self.observers: dict[Key, Callable] = {}

    def add(self, key: Key, observer: Callable):
        if not callable(observer):
            raise NotCallable()
        self.observers[key] = observer

    def send(self, key: Key, argument):
        if key not in self.observers:
            raise NotRegistered()
        self.observers[key](argument)

class NotRegistered(Exception):
    pass

class NotCallable(Exception):
    pass
