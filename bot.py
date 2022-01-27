import time
from selenium.webdriver.common.by import By
from selenium import webdriver



def main():
    # Inputs for collecting profile, product, delivery and payment data
    username = input ("Unesi mail: ")
    password = input ("Unesit pass svog računa: ")
    proizvod = input ("Koji proizvod želis naručiti: ")
    dostava: int = input ("Unesi tip dostave\n(1-Dostavna služba\n2-DUS\n3-Paketomat\n4-Osobna dostava\n5-Ekspresna dostava)\n  -  ")
    if dostava == "3":
        grad: int = input ("Unesi grad\n(1- Varaždin\n2-Zagreb\n3-Zadar\n4-Koprivnica\n5-Buzin\n  -  ")
    elif dostava == "4":
        grad: int = input ("Unesi grad\n(1- Zagreb\n2-Zadar\n3-Slavonski Brod\n4-Split\n5-Osijek\n  -  ")
        if grad == "1":
            lokacija: int = input ("Unesite lokaciju pickUp\n1-Velesajam\n2-Dubrava\n3-Rugvica\n  -  ")
        else:
            pass
    else:
        pass
    placanje: str = input ("Unesite nacin placanja\n(1-Vrimansko\n2-Gotovina)\n3-Kartica\n  -  ")
    if placanje == "3":
        kartica: int = input ("Unesi karticu\n(1- VISA\n2-Mastercard\n3-Maestro\n4-Diners\n  -  ")
    else:
        pass
    brnar = input ("Unesite broj narudžbi: ")
    nar = int (brnar)

    for i in range (nar):
        options = webdriver.ChromeOptions ()
        driver = webdriver.Chrome ('C:/webdriver/chromedriver_win32/chromedriver.exe', options=options)
        driver.maximize_window ()
        driver.get ('https://pprod.ekupi.hr/hr/login')#QA environment address
        time.sleep (2)
        # Login with email and password entered via input
        driver.find_elements (By.ID, 'j_username') [ 0 ].send_keys (username)
        driver.find_elements (By.ID, 'j_password') [ 0 ].send_keys (password)
        time.sleep (2)
        driver.find_elements (By.ID, 'webpushr-deny-button') [ 0 ].click ()
        time.sleep (2)
        driver.find_elements (By.ID, 'submit') [ 0 ].click ()
        time.sleep (2)
        # Navigating to product
        driver.get ('https://pprod.ekupi.hr/p/' + proizvod)
        time.sleep (3)
        driver.find_elements (By.ID, 'addToCartButton') [ 0 ].click ()
        driver.find_elements (By.CLASS_NAME, 'js-cookie-notification-accept') [ 0 ].click ()
        time.sleep (2)
        # Starting checkout process
        driver.get ('https://pprod.ekupi.hr/hr/checkout/multi/delivery-address/add/')
        time.sleep (2)
        driver.find_elements (By.XPATH, '/html/body/main/div[5]/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/button') [
            0 ].click ()
        time.sleep (2)
        driver.find_elements (By.XPATH, '//*[@id="addressbook"]/div[1]/form/button') [ 0 ].click ()
        time.sleep (3)
        # Choosing selected delivery method
        if dostava == "1":
            driver.find_elements (By.XPATH, '//input[@value="addressDelivery"]') [ 0 ].click ()
        elif dostava == "2":
            driver.find_elements (By.XPATH, '//input[@value="freeFlatDelivery"]') [ 0 ].click ()
        elif dostava == "3":
            driver.find_elements (By.XPATH, '//input[@value="parcelLockerDelivery"]') [ 0 ].click ()
            if grad == "1":
                driver.find_elements (By.XPATH, '//option[@value="Varaždin"]') [ 0 ].click ()
            elif grad == "2":
                driver.find_elements (By.XPATH, '//option[@value="Zagreb"]') [ 0 ].click ()
            elif grad == "3":
                driver.find_elements (By.XPATH, '//option[@value="Zadar"]') [ 0 ].click ()
            elif grad == "4":
                driver.find_elements (By.XPATH, '//option[@value="Koprivnica"]') [ 0 ].click ()
            elif grad == "5":
                driver.find_elements (By.XPATH, '//option[@value="Buzin"]') [ 0 ].click ()
            # elif grad == "6":
            #   driver.find_elements (By.XPATH, '//option[@value="Sisak"]') [ 0 ].click ()
            # elif grad == "7":
            #   driver.find_elements (By.XPATH, '//option[@value="Požega"]') [ 0 ].click ()
            # elif grad == "8":
            #    driver.find_elements (By.XPATH, '//option[@value="Slavonski Brod"]') [ 0 ].click ()
        elif dostava == "4":
            driver.find_elements (By.XPATH, '//input[@value="personalPickup"]') [ 0 ].click ()
            if grad == "1":
                driver.find_elements (By.XPATH, '//option[@value="ZAGREB"]') [ 0 ].click ()
                if lokacija == "1":
                    time.sleep (2)
                    pickup1 = driver.find_element (By.XPATH, "//*[text()[contains(.,'eKupi&poKupi - Velesajam')]]")
                    pickup1.click ()
                elif lokacija == "2":
                    time.sleep (2)
                    pickup = driver.find_element (By.XPATH, "//*[text()[contains(.,'eKupi&poKupi Kaufland Dubrava')]]")
                    pickup.click ()
                elif lokacija == "3":
                    driver.execute_script ("window.scrollTo(0, 200)")
                    time.sleep (2)
                    pickup2 = driver.find_element (By.XPATH, "//*[text()[contains(.,'eKupi&poKupi – Rugvica')]]")
                    pickup2.click ()
            elif grad == "2":
                driver.find_elements (By.XPATH, '//option[@value="ZADAR"]') [ 0 ].click ()
            elif grad == "3":
                driver.find_elements (By.XPATH, '//option[@value="SLAVONSKI BROD"]') [ 0 ].click ()
            elif grad == "4":
                driver.find_elements (By.XPATH, '//option[@value="SPLIT"]') [ 0 ].click ()
            elif grad == "5":
                driver.find_elements (By.XPATH, '//option[@value="OSIJEK"]') [ 0 ].click ()
        time.sleep (3)

        inputElement = driver.find_element (By.ID, 'deliveryMethodSubmit')
        inputElement.send_keys ("\n")
        time.sleep (5)
        # Choosing selected payment method
        if placanje == "1":
            driver.find_elements (By.XPATH, '//input[@value="WIRE_TRANSFER"]') [ 0 ].click ()
        elif placanje == "2":
            driver.find_elements (By.XPATH, '//input[@value="CASH_ON_DELIVERY"]') [ 0 ].click ()
        elif placanje == "3":
            driver.find_elements (By.XPATH, '//input[@value="CREDIT_CARD"]') [ 0 ].click ()
            if kartica == "1":
                driver.find_elements (By.XPATH, '//input[@value="VISA"]') [ 0 ].click ()
            elif kartica == "2":
                driver.find_elements (By.XPATH, '//input[@value="MASTER"]') [ 0 ].click ()
            elif kartica == "3":
                driver.find_elements (By.XPATH, '//input[@value="MAESTRO"]') [ 0 ].click ()
            elif kartica == "4":
                driver.find_elements (By.XPATH, '//input[@value="DINERS"]') [ 0 ].click ()
        time.sleep (2)
        driver.execute_script ("window.scrollTo(0, 100)")
        inputElementnew = driver.find_element (By.ID, 'submit_silentOrderPostForm')
        inputElementnew.send_keys ("\n")
        time.sleep (5)
        if placanje == "3":
            #Testing card BINs
            VISA = 4574180527069023
            MASTER = 5488661621675007
            MAESTRO = 6761121391891017
            DINERS = 30569309025904
            if kartica == "1":
                driver.find_elements (By.ID, 'card_number') [ 0 ].send_keys (VISA)
                driver.find_elements (By.ID, 'modal_month') [ 0 ].send_keys ('11')
                driver.find_elements (By.ID, 'modal_year') [ 0 ].send_keys ('29')
                driver.find_elements (By.ID, 'field_cvv') [ 0 ].send_keys ('000')
            elif kartica == "2":
                driver.find_elements (By.ID, 'card_number') [ 0 ].send_keys (MASTER)
                driver.find_elements (By.ID, 'modal_month') [ 0 ].send_keys ('11')
                driver.find_elements (By.ID, 'modal_year') [ 0 ].send_keys ('29')
                driver.find_elements (By.ID, 'field_cvv') [ 0 ].send_keys ('000')
            elif kartica == "3":
                driver.find_elements (By.ID, 'card_number') [ 0 ].send_keys (MAESTRO)
                driver.find_elements (By.ID, 'modal_month') [ 0 ].send_keys ('11')
                driver.find_elements (By.ID, 'modal_year') [ 0 ].send_keys ('29')
                driver.find_elements (By.ID, 'field_cvv') [ 0 ].send_keys ('000')
            elif kartica == "4":
                driver.find_elements (By.ID, 'card_number') [ 0 ].send_keys (DINERS)
                driver.find_elements (By.ID, 'modal_month') [ 0 ].send_keys ('11')
                driver.find_elements (By.ID, 'modal_year') [ 0 ].send_keys ('29')
                driver.find_elements (By.ID, 'field_cvv') [ 0 ].send_keys ('000')
            time.sleep (5)
            driver.find_element (By.XPATH, '//*[@id="corvuspay"]/div/form/div[3]/div[2]/button[2]').click ()
            time.sleep (10)
            driver.find_element (By.ID, 'submit').click ()
            time.sleep (5)
            driver.close ()


if __name__ == '__main__':
    main ()
