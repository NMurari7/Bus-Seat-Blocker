from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
while True:
    # create a new Chrome browser instance
    driver = webdriver.Chrome()

    # navigate to a webpage
    driver.get('https://m.gotour.co.in/search/bangalore-to-manvi?fromStationCode=STF3OEX206&toStationCode=ST1B8419E&onwardDate=2023-04-11')

    # To get seat layout
    wait = WebDriverWait(driver, 10)
    div_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.col-6.text-left')))

    # click on the div element
    div_element.click()

    #  To select the seat and click
    div_element_1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-code="BLMAIF55153"]')))

    # click the element
    div_element_1.click()

    # to click on next button
    button_element = wait.until(EC.element_to_be_clickable((By.ID, 'selected-seat-next')))
    button_element.click()

    # to select boarding point
    li_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[data-code="STP8E598644"]')))
    li_element.click()

    # to select the dropping point
    li_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[data-code="STPE56872E8"]')))
    li_element.click()

    # to enter the credentials

    input_field = driver.find_element_by_id("pass-mobile")
    input_field.send_keys("9448765432")


    # find the input tag by class name
    input_element = driver.find_element_by_class_name('form-control.pass-name')
    input_element.send_keys('anon')

    input_element = driver.find_element_by_class_name('form-control.pass-age')
    input_element.send_keys('29')

    # for clicking on gender button
    label = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="pass-m0"]')))
    label.click()


    #  To agree terms and conditions
    label = driver.find_element_by_xpath('//label[@for="pass-terms" and @class="custom-control-label"]')
    driver.execute_script("arguments[0].click();", label)

    time.sleep(5)

    email_input = driver.find_element_by_id("pass-email")
    email_input.clear()  # clear any existing value
    email_input.send_keys("annon@gmail.com")

    continue_bt = wait.until(EC.element_to_be_clickable((By.ID, 'block-ticket-btn')))
    continue_bt.click()
    time.sleep(5)
    driver.quit()
    time.sleep(620)