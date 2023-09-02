import pytest

# @pytest.mark.skip(reason="no way of currently testing this")
# def test_example_skip():
#     print("test")
#     assert 1 == 1

@pytest.mark.slow
def test_example_skip():
    print("test")
    assert 1 == 1


def test_example():
    # print("Running first test")
    assert 1 == 1

