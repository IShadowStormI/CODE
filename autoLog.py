from selenium import webdriver
from selenium.webdriver.common.by import By
# from time import sleep

def automaticLogin(username, password):
    gmail_url = "https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"

    #chromedriver path (\Downloads\chromedriver_win32\chromedriver.exe)
    PATH = ""

    driver = webdriver.Chrome(PATH)
    driver.get(url)
    driver.maximize_window()

    driver.find_element(By.ID, "identifierId").send_keys(username)
    # sleep(3)
    driver.find_element(By.ID, "identifierNext").click()
    # sleep(2)
    driver.find_element(By.NAME, "password").send_keys(password)
    # sleep(2)
    driver.find_element(By.ID, "passwordNext").click()

    print("Successfully Logged")
