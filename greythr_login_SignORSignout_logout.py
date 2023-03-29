#import packages
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Open browser
driver = webdriver.Chrome(ChromeDriverManager().install())

# Maximize the window
driver.maximize_window()

#Visit the URL
driver.get("https://creativecapsule.greythr.com/")

time.sleep(5)

#Enter username
username = driver.find_element(By.ID, "username")
username.send_keys("<username>")
time.sleep(5)

#Enter Password
password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
password.send_keys("<password>")
time.sleep(5)
login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_btn.click()

#Click Sign in
time.sleep(3)
sign_in = driver.find_element(By.XPATH, "//div[@class='btn-container mt-3x flex flex-row-reverse justify-between ng-star-inserted']//gt-button[@class='hydrated']")
if sign_in.is_displayed():
    sign_in.click()
else:
    # Click sign out
    sign_out = driver.find_element(By.XPATH, "//gt-button[@class='flex justify-end hydrated']")
    sign_out.click()

time.sleep(2)
#click logout
logout = driver.find_element(By.XPATH, "//a[@title='Logout']")
logout.click()