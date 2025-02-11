import pytest


@pytest.fixture(scope="session")
def presetup():
    print("I Run First My Browser Instances")
