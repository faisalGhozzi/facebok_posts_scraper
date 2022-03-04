from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from getpass import getpass
import time
from Project.db_conf import collection

username = input("username : ")
password = getpass("password : ")
search_term = input("term to search : ")

chrome_options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values.notifications' : 2,
    'intl.accept_languages': 'fr,fr_FR'
}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-extensions")

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

time.sleep(1)

links = driver.find_elements(By.TAG_NAME, 'a')
time.sleep(10)
links = [a.get_attribute('href') for a in links]
links = [a for a in links if '/photos/' in str(a)]

links = links[1:]

for link in links:
    driver.get(link)
    text = driver.find_elements(By.XPATH, "//span[contains(@class,'d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q a3bd9o3v b1v8xokw oo9gr5id')]")
    img = driver.find_elements_by_tag_name("img")
    all_text = []
    for txt in text:
        all_text.append(txt.text)
    image = img[0].get_attribute('src')
    collection.insert_one({
        "page" : all_text[0],
        "description" : all_text[1],
        "comments": all_text[2:],
        "image": image,
    })

    time.sleep(2)

    cursor = collection.find()
    for record in cursor:
        print(record)