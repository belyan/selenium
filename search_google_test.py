import pytest
import time
import datetime
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    chromeOptions = webdriver.ChromeOptions()
    # chromeOptions.add_argument("--start-fullscreen")
    wd = webdriver.Chrome('./chromedriver', options=chromeOptions)

    # wd = webdriver.Safari()
    wd.maximize_window()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_google_search(driver):
    driver.get("http://www.google.com/")
    driver.find_element_by_name("q").send_keys("webdriver")
    search_box = driver.find_element_by_name('q')
    search_box.submit()
    WebDriverWait(driver, 1).until(EC.title_is("webdriver - Поиск в Google"))

def test_add_project(driver):
    driver.get("http://www.shipovalov.net")
    driver.find_element_by_name("username").send_keys("student")
    driver.find_element_by_name("password").send_keys("luxoft")
    driver.find_element_by_css_selector(".button").click()

    driver.find_element_by_link_text("Manage").click()
    driver.find_element_by_link_text("Manage Projects").click()
    driver.find_element_by_css_selector("td.form-title > form > input.button-small").click()

    driver.find_element_by_name("name").send_keys(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    driver.find_element_by_name("description").send_keys("Description")
    driver.find_element_by_css_selector(".button").click()

    time.sleep(10)
