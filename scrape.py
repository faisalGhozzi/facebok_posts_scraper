from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from getpass import getpass
import time

username = input("username : ")
password = getpass("password : ")
search_term = input("term to search : ")

chrome_options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values.notifications' : 2,
    'intl.accept_languages': 'fr,fr_FR'
}
chrome_options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
driver.get("https://www.facebook.com")

username_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

username_field.clear()
username_field.send_keys(username)
password_field.clear()
password_field.send_keys(password)

button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(30)
driver.get("https://www.facebook.com/search/photos/?q="+search_term)
time.sleep(5)
see_all = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Voir tout"))).click()

# Add scroll code here if needed

time.sleep(10)

links = driver.find_elements(by=By.TAG_NAME, value='a')
time.sleep(10)
links = [a.get_attribute('href') for a in links]
links = [a for a in links if '/photos/' in str(a)]
