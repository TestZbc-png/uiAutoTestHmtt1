import pytest

from utils import DriverUtil

@pytest.mark.run(order=1)
class TestBegin:

    def test_begin(self):
        DriverUtil.set_mp_auto_quit(False)

