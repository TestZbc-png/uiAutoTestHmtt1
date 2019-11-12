import time

import pytest

from utils import DriverUtil

@pytest.mark.run(order=4)
class TestEnd:

    def test_end(self):
        DriverUtil.set_mp_auto_quit(True)
        time.sleep(2)
        DriverUtil.get_mp_quit()

