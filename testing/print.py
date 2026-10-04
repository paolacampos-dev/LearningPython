# print() has a side effect: displaying the output
# Mockin print:

def greet(name):
    print(f'Hello {name}')

# 1. Dependency injection:
def greet(name, display=print):
    display(f"Hi {name}")

def mock_print(message, *args):
    mock_print.last_message = message

def test_greet():
    greet("John", display=mock_print)
    assert mock_print.last_message == "Hello John"