from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

"""
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
browser = webdriver.Chrome(options=chrome_options)
"""

PANEL_URL = "http://half_chain:48763"
def view_user_comments():
    for ele in browser.find_elements(By.CLASS_NAME, "btn-ghost"):
        if ele.text == "查看":
            ele.click()
            break
    
    for ele in browser.find_element(By.CLASS_NAME, "h-full").find_elements(By.TAG_NAME, "a"):
        print(f"currently click at {ele.text}")
        ele.click()
        sleep(0.1)

def edit(cid:int, n_ctx:str):
    for ele in browser.find_elements(By.CLASS_NAME, "btn-ghost"):
        if ele.text == "修改":
            ele.click()
            break
    sleep(1)
    num, ctx = browser.find_elements(By.CLASS_NAME, "textarea")
    num.send_keys(str(cid))
    ctx.send_keys(n_ctx)
    browser.find_element(By.TAG_NAME, "button").click()

from logging import info, basicConfig, INFO
basicConfig(level=INFO)
sleep(10)
info("supervisor started")
while True:
    browser = webdriver.Remote(
        command_executor='http://selenium-hub:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME
    )
    info("fetching first page")
    browser.get(f"{PANEL_URL}")
    sleep(1)

    info("add cookie")
    from os import getenv
    browser.add_cookie({'name' : 'SUPER_SECRET_ADMIN_TOKEN', 'value' : getenv("SUPER_SECRET_ADMIN_TOKEN", "48763")})

    info("view user comment")
    view_user_comments()
    browser.quit()
    sleep(60)