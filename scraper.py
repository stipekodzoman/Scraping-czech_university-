from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import pandas as pd
from config import BASE_URL

def _extracted_from_startScraping_8(chrome_options):
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options,
    )
    driver.get(BASE_URL)
    sleep(3)
    publication_type=""
    author_name=""
    date=""
    title=""
    details=""
    # initial_year=2023
    # for i in range(6):
    driver.find_element(By.CSS_SELECTOR,"input[name=\'autori_operator\']").click()
    sleep(0.5)
    driver.find_element(By.CSS_SELECTOR,"select[name=\'fakulta\']").click()
    driver.find_element(By.CSS_SELECTOR,"select[name=\'fakulta\']").find_element(By.CSS_SELECTOR,"option[value=\'FIS\']").click()
    sleep(0.5)
    driver.find_element(By.CSS_SELECTOR,"select[onchange=\'fetch_select(this.value);\']").click()
    driver.find_element(By.CSS_SELECTOR,"select[onchange=\'fetch_select(this.value);\']").find_element(By.CSS_SELECTOR,"option[value=\'0\']").click()
    sleep(0.5)
    driver.find_element(By.CSS_SELECTOR,"select[name=\'rok[]\']").find_element(By.CSS_SELECTOR,f"option[value=\'2023\']").click()
    driver.find_element(By.CSS_SELECTOR,"select[name=\'rok[]\']").find_element(By.CSS_SELECTOR,f"option[value=\'2022\']").click()
    driver.find_element(By.CSS_SELECTOR,"select[name=\'rok[]\']").find_element(By.CSS_SELECTOR,f"option[value=\'2021\']").click()
    driver.find_element(By.CSS_SELECTOR,"select[name=\'rok[]\']").find_element(By.CSS_SELECTOR,f"option[value=\'2020\']").click()
    driver.find_element(By.CSS_SELECTOR,"select[name=\'rok[]\']").find_element(By.CSS_SELECTOR,f"option[value=\'2019\']").click()
    driver.find_element(By.CSS_SELECTOR,"select[name=\'rok[]\']").find_element(By.CSS_SELECTOR,f"option[value=\'2018\']").click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR,"select[name=\'typ\']").click()
    driver.find_element(By.CSS_SELECTOR,"select[name=\'typ\']").find_element(By.CSS_SELECTOR,"option[value=\'CJ\']").click()
    publication_type=driver.find_element(By.CSS_SELECTOR,"select[name=\'typ\']").text
    sleep(1)
    driver.find_element(By.CSS_SELECTOR,"input[name=\'submitSearch\']").click()
    sleep(4)
    article_elements=driver.find_elements(By.CSS_SELECTOR,"div[id=\'content\']>table")
    del article_elements[0]
    for i,article_element in enumerate(article_elements):
        print(article_element.text)
    driver.back()
    # initial_year-=1
    sleep(1000)
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--force-dark-mode")
chrome_options.add_argument("--start-maximized")
try:
    _extracted_from_startScraping_8(chrome_options)
except Exception as e:
        print(e)
