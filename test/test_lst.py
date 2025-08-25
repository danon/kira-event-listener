# - ability to register a new observer
# - ability to call the listener, and when that happens, the observers should be called
# - ability to pass some argument or an event from the caller to the observer
# - if trying to register an observer that's not callable, throw exception
# - if trying to call a listener that's not registered, throw exception

def test_empty():
    assert True
