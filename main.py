


from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from googletrans import Translator
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



app = FastAPI()

@app.get("/{url:path}")
async def root(url: str):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    #driver = webdriver.Chrome()
    driver.get("https://translate.google.com/?sl=auto&tl=en&text=%E0%A4%85%E0%A4%AA%E0%A4%A8%E0%A4%BE%20%E0%A4%85%E0%A4%97%E0%A4%B2%E0%A4%BE%20%E0%A4%95%E0%A5%8B%E0%A4%B0%E0%A5%8D%E0%A4%B8%20%E0%A4%96%E0%A5%8B%E0%A4%9C%E0%A5%87%E0%A4%82%E0%A5%A4&op=websites")
    assert "Google Translate" in driver.title
    elem = driver.find_element(By.ID,"i46")
    elem.clear()
    elem.send_keys(f"{url}")
    elem.send_keys(Keys.RETURN)
    sleep(5)
    window= driver.window_handles
    driver.switch_to.window(window[1])
    urll = driver.current_url
    driver.execute_script("window.open('{}', '_blank');".format(urll))
    
    print(urll)

    driver.quit()

    return urll
