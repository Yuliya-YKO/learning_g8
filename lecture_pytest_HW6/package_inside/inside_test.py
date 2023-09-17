import pytest

def test_only_automatic_fixture(automatic_fixture):
    print("Test using only automatic fixture")

def test_all_fixtures(automatic_fixture, fixture_second, ):
    print("Test using all three fixtures")
    print(type(fixture_second))

