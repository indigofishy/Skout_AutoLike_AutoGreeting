import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(20)

def main():
    # Open the URL
    driver.get("https://www.skout.com/")
    driver.fullscreen_window()

    #login
    login = driver.find_element(By.ID, "username")
    pw = driver.find_element(By.ID, "password")
    login.send_keys("***")
    pw.send_keys("***")
    pw.send_keys(Keys.RETURN)


    #second page
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/fieldset/div/form/div/fieldset/div/button").click()
    #driver.find_element(By.LINK_TEXT, "Go meet someone").click()
    time.sleep(3)

    while True:
        call_function = int(input("1= like only, 2= meet_message, 3= both, 4=end the code"))
        match call_function:
            case 1:
                thirty_likes()
            case 2:
                meet_message()
            case 3:
                thirty_likes()
                meet_message()
            case 4:
                break
            case _:
                print("retype:")
                continue

    # Close the browser
    input("Press ENTER to exit\n")
    driver.quit()



# Function1: 
    #Click the "Interested" button 30 times
def thirty_likes():
    count = 0
    driver.find_element(By.ID, "menu-toggle").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Interested?").click()
    for interested_click in range(30):
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[3]/div[2]/a").click()
        count = count + 1
    print("like count:", count)



# Function2:
    #Click the "Meet" button and send a message 15 times
def meet_message():
    word_list = ["Heyyy how you doing :) ", "Hi, how are you today? :)))", "Hellooo!!! :D", "Hi there! :D"]
    count = 0 
    #counting how many time before it crashes
    #it crashed for banner showing up and cant find the menu

    for skout_meet_index in range(1, 16):
        while True:
            try:
                wait = WebDriverWait(driver, 5)
                menu_button = wait.until(EC.visibility_of_element_located((By.ID, "menu-toggle")))  #wait 9s for banner go away
                menu_button.click()
                break
            except Exception as e:
                time.sleep(5)
                print("banner error")
                #print(e) for checking
                continue
        driver.find_element(By.LINK_TEXT, "Meet people").click()
        time.sleep(3)
        driver.find_element(By.XPATH, f"/html/body/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/ul/li[{skout_meet_index}]/a/img").click()

        time.sleep(3)
    #click chat button
        driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/a[3]").click()
        time.sleep(3)

        meet_text_col = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div[2]/div[2]/div/div[4]/form/div/div/div[2]/div/div[1]/textarea")
        random_word = random.choice(word_list)
        meet_text_col.send_keys(random_word)
        time.sleep(3)
        meet_text_col.send_keys(Keys.RETURN)
        count = count + 1
        print("Hi * ", count)
        time.sleep(3)

main()







