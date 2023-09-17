import pytest

@pytest.fixture(autouse=False)
def global_fixture_setup():
    print("global lecture_pytest fixture setup")
    yield
    print("global lecture_pytest fixture teardown")