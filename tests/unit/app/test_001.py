
from datetime import datetime


def add_numbers(a, b):
    """Adds two numbers and returns the result."""
    return a + b


def test_add_numbers():
    """Test the add_numbers function from app_001."""
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    assert add_numbers(1, 2) == 3
