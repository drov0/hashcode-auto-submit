from inblc import *
from outblc import *
from random import randint
import os
import time

if __name__ == "__main__":
    from selenium import webdriver
    import pyautogui
    dirs = os.listdir("input")
    for file in dirs:
        data = read_input('input/' + file)

        vehicles_nb = data['vehicles'].__len__()

        for ride in data['rides']:
            id = randint(0, vehicles_nb-1)
            data['vehicles'][id]['rides'].append(ride['id'])

        filename = file.split('.')

        write_output('output/' + filename[0] + ".out", data)

    driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.
    for runs in range(1000):
        driver.get('https://hashcodejudge.withgoogle.com/#/rounds/4868850726207488/submissions/');
        time.sleep(1.5)
        if (runs == 0):
            driver.find_element_by_class_name("md-primary").click()
            time.sleep(0.5)
            driver.switch_to.window(driver.window_handles[1])
            driver.find_element_by_id("identifierId").send_keys("username")
            driver.find_element_by_id("identifierNext").click()
            time.sleep(1)
            driver.find_element_by_name("password").send_keys("password")
            time.sleep(0.5)
            driver.find_element_by_id("passwordNext").click()
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(0.5)

        driver.find_element_by_class_name("md-primary").click()
        time.sleep(0.5)
        for id, elem in enumerate(driver.find_elements_by_css_selector('[aria-label="Upload"]')) :
            elem.click()
            time.sleep(0.5)
            if (id == 0):
                pyautogui.press('down')
                pyautogui.press('enter')
                time.sleep(0.5)
            if (id == 2):
                pyautogui.press('down')
                time.sleep(0.5)
            elif (id == 3):
                pyautogui.press('down')
                pyautogui.press('down')
                time.sleep(0.2)
            elif (id == 4):
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('down')
            elif (id == 5):
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('down')

            pyautogui.press('enter')

        driver.find_element_by_css_selector('[ng-click="submissionsCtrl.createSubmission()"]').click()
        time.sleep(10)
