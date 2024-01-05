from flask import Flask, request, send_file
import os
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select

app = Flask(__name__)

@app.route('/<string:param>', methods=['GET'])
def web_scrape(param):
    
    # add https:// to the url
    url = "https://" + param
    
    # set up Selenium options 
    options = Options()
    options.page_load_strategy = 'eager' 
    
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--remote-debugging-port=9222')

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    # open page
    driver.get(url)
    driver.implicitly_wait(10)
    
    # save page's html to a text file
    with open('page_source.txt', 'w') as file:
        file.write(driver.page_source)
    
    # close the driver
    driver.quit()
    
    # return the file as a download
    return send_file('page_source.txt', as_attachment=True)
    
if __name__ == '__main__':
    # use the PORT environment variable if it's defined, otherwise default to 8080
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
    