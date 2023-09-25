import pytest

@pytest.fixture(autouse=True)
def automatic_fixture():
    print("Automatic fixture inside_package setup")
    yield
    print("Automatic fixture inside_package teardown")

@pytest.fixture(autouse=False)
def fixture_second():
    return 7