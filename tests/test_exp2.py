import pytest

# @pytest.fixture(scope="session")
# def fixtures():
#     print("Running fixture 1")
#     return 1

@pytest.fixture(scope="session")
def yield_fixtures():
    print("Running fixture 1")
    yield 1
    print("Ending fxiture 1")

def test_method(yield_fixtures):
    print("Running example1")
    assert yield_fixtures == 1

def test_method1(yield_fixtures):
    print("Running example2")
    assert yield_fixtures == 1