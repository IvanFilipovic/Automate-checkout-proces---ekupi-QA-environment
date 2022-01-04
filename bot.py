import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def main():
    #Inputs for collecting profile, product, delivery and payment data
    username = input ("Unesi mail: ")
    password = input ("Unesit pass svog računa: ")
    proizvod = input ("Koji proizvod želis naručiti: ")
    dostava: int = input("Unesi tip dostave\n(1-Dostavna služba\n2-DUS\n3-Paketomat\n4-Osobna dostava\n5-Ekspresna dostava)\n  -  ")
    grad: int = input ("Unesi grad\n(1- Varaždin\n2-Zagreb\n3-Zadar\n4-Koprivnica\n  -  ")
    placanje: str = input("Unesite nacin placanja\n(1-Vrimansko\n2-Gotovina)\n  -  ")
    brnar = input("Unesite broj narudžbi: ")
    nar = int(brnar)

    for i in range(nar):
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome('C:/webdriver/chromedriver_win32/chromedriver.exe', options=options) #Navigate to your webdriver location
        driver.maximize_window()
        driver.get('https://www.ekupi.hr/hr/login')
        time.sleep(2)
        #Login with email and password entered via input
        driver.find_elements(By.ID, 'j_username')[0].send_keys(username)
        driver.find_elements(By.ID, 'j_password')[0].send_keys(password)
        time.sleep(2)
        driver.find_elements(By.ID, 'submit')[0].click()
        time.sleep(2)
        #Navigating to product
        driver.get('Ekupi QA environment address' + proizvod)
        time.sleep(3)
        driver.find_elements(By.ID, 'addToCartButton')[0].click()
        time.sleep(2)
        #Starting checkout process
        driver.get('https://www.ekupi.hr/hr/checkout/multi/delivery-address/add/')
        driver.find_elements(By.XPATH, '/html/body/main/div[5]/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/button')[0].click()
        time.sleep(3)
        driver.find_elements(By.XPATH, '//*[@id="addressbook"]/div/form/button')[0].click()
        time.sleep(3)
        #Choosing selected delivery method
        if dostava == "1":
            driver.find_elements (By.XPATH, '//input[@value="addressDelivery"]')[ 0 ].click ()
        elif dostava == "2":
            driver.find_elements (By.XPATH, '//input[@value="freeFlatDelivery"]')[ 0 ].click ()
        elif dostava == "3":
            driver.find_elements (By.XPATH, '//input[@value="parcelLockerDelivery"]')[ 0 ].click ()
            if grad == "1":
                driver.find_elements (By.XPATH, '//option[@value="Varaždin"]')[ 0 ].click ()
            elif grad == "2":
                driver.find_elements (By.XPATH, '//option[@value="Zagreb"]') [ 0 ].click ()
            elif grad == "3":
                driver.find_elements (By.XPATH, '//option[@value="Zadar"]') [ 0 ].click ()
            elif grad == "4":
                driver.find_elements (By.XPATH, '//option[@value="Koprivnica"]') [ 0 ].click ()
            else:
                pass
        elif dostava == "4":
            driver.find_elements (By.XPATH, '//input[@value="personalPickup"]') [ 0 ].click ()
        
        WebDriverWait (driver, 10).until (EC.element_to_be_clickable ((By.XPATH, '//*[@id="deliveryMethodSubmit"]'))).click ()

        #Choosing selected payment method
        if placanje == "1":
            driver.find_elements(By.XPATH, '//input[@value="CASH_ON_DELIVERY"]')[0].click()
        else:
            driver.find_elements(By.XPATH, '//input[@value="WIRE_TRANSFER"]')[0].click()

        time.sleep(2)
        driver.find_elements(By.ID, 'submit_silentOrderPostForm')[0].click()


if __name__ == '__main__':
    main()
