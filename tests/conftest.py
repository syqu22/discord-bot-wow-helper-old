import pytest
from warcraftlogs import WarcraftlogsAPI

@pytest.fixture(scope="module")
def logs():
    return WarcraftlogsAPI("KBT4c2qFNXa7t8dD")
