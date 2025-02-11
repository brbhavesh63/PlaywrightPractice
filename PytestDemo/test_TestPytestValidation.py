import pytest

@pytest.fixture(scope="function")
def setup():
    print("I Run First")
    return "Pass"

@pytest.fixture(scope="module")
def postsetup():
    print("I Run First as postsetup")
    yield
    print("I run last as postsetup")

def test_initialCheck(setup,postsetup):
    print("This is my first pytest")
    assert setup == "Pass"

def test_secondCheck(presetup):
    print("This is my second pytest")
