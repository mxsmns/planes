import os

import pytest


@pytest.fixture
def resource_folder():
    return os.path.abspath(os.path.join(__file__, os.pardir, "resources"))
