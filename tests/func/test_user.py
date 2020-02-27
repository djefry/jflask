import pytest
from time import sleep


@pytest.mark.usefixtures("chrome_driver_init")
class Basic_Chrome_Test:
    pass


class Test_URL_Chrome(Basic_Chrome_Test):
    # Testing home page
    def test_open_url(self):
        self.driver.get("http://localhost:80")
        print(self.driver.title)

        sleep(5)
