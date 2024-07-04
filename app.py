import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

def main():
    # Path to the ChromeDriver
    driver_path = r"C:\Users\Raul\Desktop\PROGRAMMING\chromedriver.exe"
    
    # Initialize the undetected Chrome driver with specified executable path
    options = uc.ChromeOptions()
    options.add_argument("--window-size=800,600")  # Set window size
    
    driver = None
    
    try:
        # Launch the browser
        driver = uc.Chrome(options=options, driver_executable_path=driver_path)
        
        # Open the website
        driver.get("https://wiktionary.org/")
        
        # Wait for the page to load
        time.sleep(2)
        
        # Locate the search input field and enter "hello"
        search_input = driver.find_element(By.ID, "searchInput")
        search_input.send_keys("привет")
        
        # Submit the form
        search_input.send_keys(Keys.RETURN)
        
        # Wait for the results page to load
        time.sleep(3)
        
        try:
            # Find the Pronunciation section header
            pronunciation_header = driver.find_element(By.XPATH, "//h3[@id='Pronunciation']")
            
            # Find the ul element that follows the Pronunciation section header
            pronunciation_ul = pronunciation_header.find_element(By.XPATH, "./following::ul[1]")
            
            # Extract and print the content of each li element within the ul
            li_elements = pronunciation_ul.find_elements(By.TAG_NAME, "li")
            for li in li_elements:
                print(li.text)
            
        except NoSuchElementException:
            print("Pronunciation section or content not found.")
        
        # Wait for 10 seconds to see the results
        time.sleep(10)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if driver:
            try:
                driver.quit()
            except Exception as e:
                print(f"Error during driver quit: {e}")

if __name__ == "__main__":
    main()
