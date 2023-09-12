import pytest


# Function to test
def add(a, b):
    return a + b


# Simple test function
def test_addition():
    result = add(2, 3)
    assert result == 5


# Test function with parametrization
@pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (0, 0, 0), (-2, 5, 3)])
def test_parametrized_addition(a, b, expected):
    result = add(a, b)
    assert result == expected


# Test function using a fixture
@pytest.fixture
def setup_teardown():
    print("Setup")
    yield
    print("Teardown")


def test_using_fixture(setup_teardown):
    print("Test logic")


# Skipped test function
@pytest.mark.skip(reason="Test is not ready yet")
def test_skipped_function():
    assert False


# Expected to fail test function
@pytest.mark.xfail(reason="Expected to fail due to known issue")
def test_expected_to_fail():
    result = add(2, 3)
    assert result == 10


# Expected to fail with parametrization
@pytest.mark.parametrize("a, b, expected", [(2, 3, 10), (0, 0, 0), (-2, 5, -10)])
@pytest.mark.xfail(reason="Expected to fail for some cases")
def test_parametrized_expected_to_fail(a, b, expected):
    result = add(a, b)
    assert result == expected


# Test function with timeout
@pytest.mark.timeout(3)  # 3 seconds timeout
def test_timeout_function():
    import time
    time.sleep(5)  # Sleep longer than the timeout


# Conditional skip using a condition
some_condition = False


@pytest.mark.skipif(some_condition, reason="Skipping test based on condition")
def test_conditionally_skipped_function():
    assert True


if __name__ == '__main__':
    pytest.main([__file__])
