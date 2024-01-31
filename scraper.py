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
import mysql.connector
def _extracted_from_startScraping_8(chrome_options):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="czech_university"
        )
        cursor=connection.cursor()
        print("Database connected")
    except Exception as e:
        print("Error occured while connecting to database")
    driver = webdriver.Chrome(
        options=chrome_options,
    )
    actions=ActionChains(driver)
    driver.get(BASE_URL)
    wait=WebDriverWait(driver,10)
    sleep(3)
    publication_type="Články v časopise"
    author_name=""
    publication_date=2023
    title=""
    details=""
    count=1
    for i in range(6):
        try:
            driver.find_element(By.CSS_SELECTOR,"input[name=\'autori_operator\']").click()
            sleep(0.3)
            driver.find_element(By.CSS_SELECTOR,"select[name=\'fakulta\']").click()
            driver.find_element(By.CSS_SELECTOR,"select[name=\'fakulta\']").find_element(By.CSS_SELECTOR,"option[value=\'FIS\']").click()
            sleep(0.3)
            driver.find_element(By.CSS_SELECTOR,"select[onchange=\'fetch_select(this.value);\']").click()
            driver.find_element(By.CSS_SELECTOR,"select[onchange=\'fetch_select(this.value);\']").find_element(By.CSS_SELECTOR,"option[value=\'0\']").click()
            sleep(0.3)
            driver.find_element(By.CSS_SELECTOR,"select[name=\'rok[]\']").find_element(By.CSS_SELECTOR,f"option[value=\'{publication_date}\']").click()
            sleep(0.3)
            driver.find_element(By.CSS_SELECTOR,"select[name=\'typ\']").click()
            driver.find_element(By.CSS_SELECTOR,"select[name=\'typ\']").find_element(By.CSS_SELECTOR,"option[value=\'CS\']").click()
            sleep(0.3)
            driver.find_element(By.CSS_SELECTOR,"input[name=\'submitSearch\']").click()
            sleep(2)
        except Exception as e:
            print(e)
        article_elements=driver.find_elements(By.CSS_SELECTOR,"div[id=\'content\']>table")
        del article_elements[0]
        waiting_time=3
        for i,article_element in enumerate(article_elements):
            if i%2==0:
                try:
                    article_element.find_elements(By.TAG_NAME,"table")[1].find_element(By.TAG_NAME,"a").click()
                    sleep(waiting_time)
                    if(waiting_time>2):
                        waiting_time-=0.5
                    details=driver.find_element(By.CSS_SELECTOR,"table.detaily").text
                    driver.find_element(By.CSS_SELECTOR,"img[alt=\'Click to Close\']").click()
                except Exception as e:
                    print(e)
            else:
                try:
                    article=article_element.text
                    author_name=article.split(".")[0]
                    title=article.split(".")[1]
                except Exception as e:
                    print(e)
                #print("{publication_type:",publication_type,",author_name:",author_name,",title:",title,",publication_date:",publication_date,",details:",details,"}")
                query=f"INSERT INTO article (publication_type,author_name,publication_date,title,details) VALUES (%s,%s,%s,%s,%s);"
                try:
                    cursor.execute(query,(publication_type,author_name,publication_date,title,details))
                    connection.commit()
                    print(f"{count} dataset has been added to the database")
                    count+=1
                except Exception as e:
                    print(e)
                    print("Can't save data to database")
        driver.back()
        publication_date-=1
    # initial_year-=1
    connection.close()
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--force-dark-mode")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")
try:
    _extracted_from_startScraping_8(chrome_options)
except Exception as e:
        print(e)
