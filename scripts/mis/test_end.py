import time

import pytest

from utils import DriverUtil

@pytest.mark.run(order=1003)
class TestEnd:

    def test_end(self):
        DriverUtil.set_mp_auto_quit(True)
        time.sleep(2)
        DriverUtil.get_mis_quit()

