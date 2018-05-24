import pytest
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture
def driver(request):
    browser_options = webdriver.ChromeOptions()
    browser_options.add_argument("--start-maximized")

    browser = webdriver.Chrome(options=browser_options)
    # browser = webdriver.Safari()

    main_window = browser.current_window_handle
    browser.switch_to.window(main_window)
    browser.maximize_window()

    print(browser.capabilities)
    request.addfinalizer(browser.quit)
    return browser


def test_google_search(driver):
    driver.get("http://www.google.com/")
    driver.find_element_by_name("q").send_keys("webdriver")
    search_box = driver.find_element_by_name("q")
    search_box.submit()
    WebDriverWait(driver, 1).until(ec.title_is("webdriver - Поиск в Google"))

    time.sleep(1)


def test_add_project(driver):
    driver.get("http://www.shipovalov.net")

    driver.find_element_by_name("username").send_keys("student")
    driver.find_element_by_name("username").send_keys(Keys.HOME)
    driver.find_element_by_name("username").send_keys(Keys.COMMAND, "A")
    driver.find_element_by_name("password").send_keys("luxoft")
    driver.find_element_by_css_selector(".button").click()

    driver.find_element_by_link_text("Manage").click()
    driver.find_element_by_link_text("Manage Projects").click()
    driver.find_element_by_css_selector("td.form-title > form > input.button-small").click()

    driver.find_element_by_name("name").send_keys(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    driver.find_element_by_name("description").send_keys("Description")
    driver.find_element_by_css_selector(".button").click()

    time.sleep(1)
