from selenium.common import exceptions
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



# class AddCartAndPurchaeTools():

def test_search_and_add_product_to_cart():
        driver = setup()

        text_to_search = "Pliers" #change me if needed
        username = "customer@practicesoftwaretesting.com"
        password = "welcome01"

        driver.find_element(By.ID, "search-query").send_keys(text_to_search)
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[text()='Search']").click()
        time.sleep(2)
        
        try: # handle the StaleException error
            for select_product in driver.find_elements(By.XPATH, "//div[@data-test='search_completed']//h5"):
            #   if (select_product.get_attribute("innerHTML") == text_to_search):
                action = ActionChains(driver)
                if (select_product.text == text_to_search):
                    action.click(on_element=select_product).perform()
                    time.sleep(2)
        except exceptions.StaleElementReferenceException:
              pass
        
        driver.find_element(By.XPATH, "//button[@data-test='add-to-cart']").click()
        time.sleep(5)
        toast_msg = driver.find_element(By.XPATH, '//div[@aria-label="Product added to shopping cart."]')
        assert toast_msg.text == "Product added to shopping cart."

        cart_lbl_count = driver.find_element(By.XPATH, '//span[@id="lblCartCount"]')
        assert cart_lbl_count.text == '1'
        

        # sign in to the page after adding a product to cart then view the cart page
        driver.find_element(By.XPATH, "//a[text()='Sign in']").click()
        time.sleep(3)
        driver.find_element(By.ID, 'email').send_keys(username)
        pass_btn = driver.find_element(By.ID, 'password')
        ActionChains(driver).move_to_element(pass_btn).click(pass_btn).send_keys(password).perform()
        
        driver.find_element(By.XPATH, "//input[@data-test='login-submit']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[@data-test='cart-quantity']").click()
        time.sleep(3)

        #proceed to checkout
        driver.find_element(By.XPATH, "//button[@data-test='proceed-1']").click
        

def test_proceed_to_checkout():
        driver = setup()

    
def test_signin_to_pay():
        driver = setup()




def setup():
    driver = webdriver.Chrome()
    driver.set_window_position(600, 280, windowHandle='current')
    driver.get('http://localhost:4200/')
    return driver

def teardown(driver):
    driver.quit()
