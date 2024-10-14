from pytest_check import check
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_homepage():
    driver = setup()

    title = driver.title
    assert title == "Practice Software Testing - Toolshop - v5.0"
    driver.implicitly_wait(50000)
    
def test_header():
    driver = setup()
  
    # Checking an attribute in Webelements e.g. innerText\
    # Home linktext
    home_linkText = driver.find_element(By.XPATH, "//li[@class='nav-item']/a[@class='nav-link active']")
    assert 'Home' == home_linkText.text
    print('Home button link is displayed')

    ##Contact Linktext
    contact_linkText = driver.find_element(By.XPATH, "//li[@class='nav-item']/a[@data-test='nav-contact']")
    assert 'Contact' == contact_linkText.text
    print('Contact button link is displayed')

    ## Sign in Lintext Verification
    ## -s it display the print result
    signIn_linkText = driver.find_element(By.XPATH, "//li[@class='nav-item']/a[@data-test='nav-sign-in']")
    assert 'Sign in' == signIn_linkText.text
    print('Sign in button link is displayed')

    driver.implicitly_wait(10)

def test_header_categories():
    driver = setup()

    # categories_linkText = driver.find_element(By.XPATH, "//li[@class='nav-item dropdown']//a[@data-test='nav-categories']")
    # assert "Categories" == categories_linkText.text


    cat_dropdown_items = ["Hand Tool", "Power Tools", "Other", "Special", "Rentals"]
    # dropdown_btn = driver.find_elements(By.CSS_SELECTOR, "ul[class='dropdown-menu show'] a")
    # for drpdwn_btn in driver.find_elements(By.CSS_SELECTOR, '.dropdown-menu.show a'):

    print("Test", [dropdown.text for dropdown in driver.find_elements(By.XPATH, "//ul[@class='dropdown-menu show']//a[@class='dropdown-item']")])
    # for dropdown1 in driver.find_elements(By.XPATH, "//ul[@class='dropdown-menu show']//a[@class='dropdown-item']"):
    #     print("Test1" + dropdown1.text)
 

    # for drpdwn in drpdwn_btn:
    #     values = drpdwn.text
    #     print(values)
    #     if "Hand Tool" == values:
    #         assert True
    #     else: False


    # for dropdown_btn in driver.find_elements(By.CSS_SELECTOR, "ul[class='dropdown-menu show']"):
    #     values = dropdown_btn.find_element(By.XPATH, "//ul[@class='dropdown-menu show']//a[@class='dropdown-item']")
        
    #     assert "Hand Tool" == values.text
    #     print(values.text)





def setup():
    driver = webdriver.Chrome()
    driver.get('http://localhost:4200/')
    return driver

def teardown(driver):
    driver.quit()