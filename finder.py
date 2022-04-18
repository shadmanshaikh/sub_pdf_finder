from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service
import time
print('''
                     SUBJECTS
          DAA - 18cs42 \t-design-and-analysis-of-algorithms-notes/ 
          OS   - 18cs43 \t-operating-systems-notes/
          MES - 18cs44 \t-microcontroller-and-embedded-systems-notes/
          OOC - 18cs45 \t-object-oriented-concepts-notes/
          DC   - 18cs46 \t-data-communication-notes/
          MATHS - 18mat41 \t-complexity-analysis-probability-and-statistics-methods-notes/
 ''' )

print("COPY AND PASTE ABOVE SUBJECTS FOR DOWNLOADING MODULE")
print("\nAUTHOR: SHADMAN\n")


find = input("Enter The Subject code: ")
path = r'C:\Users\XAN\Desktop\sel\chromedriver.exe'
s = Service(path)
driver = webdriver.Chrome(service=s)
driver.maximize_window()
action_chains = ActionChains(driver)

#def select_subject(argument):
 #       switcher = {
 #               1: "M-1",
  #              2: "M-2"
  #              3:"M-3"
  #              4:"M-4"
   #     }
    #    return switcher.get(argument, "nothing")
   # output =input("enter the module:")
   # print(output)
    

Insertelement = driver.get("https://www.vtupulse.com/cbcs-cse-notes/" + find)
time.sleep(2)
Insertelement = driver.find_element_by_partial_link_text("M-1")
Insertelement.click()
action_chains.key_down(Keys.CONTROL).send_keys("s").key_up(Keys.CONTROL).perform()
time.sleep(2)

Insertelement = driver.get("https://www.vtupulse.com/cbcs-cse-notes/" + find)
Insertelement = driver.find_element_by_partial_link_text("M-2")
Insertelement.click()
time.sleep(2)
action_chains.key_down(Keys.CONTROL).send_keys("s").key_up(Keys.CONTROL).perform()

Insertelement = driver.get("https://www.vtupulse.com/cbcs-cse-notes/" + find)
Insertelement = driver.find_element_by_partial_link_text("M-3")
Insertelement.click()
time.sleep(2)
action_chains.key_down(Keys.CONTROL).send_keys("s").key_up(Keys.CONTROL).perform()

Insertelement = driver.get("https://www.vtupulse.com/cbcs-cse-notes/" + find)
Insertelement = driver.find_element_by_partial_link_text("M-4")
Insertelement.click()
time.sleep(2)
action_chains.key_down(Keys.CONTROL).send_keys("s").key_up(Keys.CONTROL).perform()

Insertelement = driver.get("https://www.vtupulse.com/cbcs-cse-notes/" + find)
Insertelement = driver.find_element_by_partial_link_text("M-5")
Insertelement.click()
time.sleep(2)
action_chains.key_down(Keys.CONTROL).send_keys("s").key_up(Keys.CONTROL).perform()

driver.close()
