
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select


def test_header_categories():
    driver = setup()

    categories_linkText = driver.find_element(By.XPATH, "//li[@class='nav-item dropdown']//a[@data-test='nav-categories']")
    assert "Categories" == categories_linkText.text


    cat_dropdown_items = ["Hand Tools", "Power Tools", "Other", "Special Tools", "Rentals"]

    dropdown1 = driver.find_element(By.XPATH, "//li/a[@role='button']")
    dropdown1.click()
    driver.implicitly_wait(2)

    # print("\nHere's the list: ", [dropdown.text for dropdown in driver.find_elements(By.XPATH, "//ul[@aria-label='nav-categories']/li/a[@class='dropdown-item']")])
    
    captured_values = []
    for dropdown_list in driver.find_elements(By.XPATH, "//ul[@aria-label='nav-categories']/li/a[@class='dropdown-item']"):
        if (dropdown_list.get_attribute("innerHTML") != "null") :
            captured_values.append(dropdown_list.get_attribute("innerHTML"))
            # print(captured_values) #print the list of the element

    # assert len(cat_dropdown_items) == len(captured_values)
    assert all([a==b for a, b in zip(cat_dropdown_items, captured_values) ]) # loop assertion 
    # print(all([a==b for a, b in zip(cat_dropdown_items, captured_values) ])) # print the loop assertion : TRUE or FALSE

def test_header_language():
    driver = setup()

    langauage_lists = ["DE", "EN", "ES", "FR", "NL", "TR"]
    lang_captured_values =[]

    globe_icon = driver.find_element(By.XPATH, "//*[@class='svg-inline--fa fa-globe']")
    assert globe_icon.is_displayed

    lang_btn_text = driver.find_element(By.XPATH, "//*[@id='language']")
    assert lang_btn_text.text == "EN"

    lang_btn_text.click()
    driver.implicitly_wait(2)

    for lang_drpdwn_list in driver.find_elements(By.XPATH, "//ul[@aria-labelledby='language']//a[@class='dropdown-item']"):
        if (lang_drpdwn_list.get_attribute('innerHTML') != "null") :
            lang_captured_values.append(lang_drpdwn_list.get_attribute("innerHTML"))

            assert all([a==b for a,b in zip(langauage_lists, lang_captured_values)])


def setup():
    driver = webdriver.Chrome()
    driver.get('http://localhost:4200/')
    # WebDriverWait(driver, timeout=5)
    return driver

def teardown(driver):
    driver.quit()