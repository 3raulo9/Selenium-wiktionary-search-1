import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def main():
    # Path to the ChromeDriver
    driver_path = r"C:\Users\Raul\Desktop\PROGRAMMING\chromedriver.exe"
    
    # Initialize the undetected Chrome driver with specified executable path
    options = uc.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    options.add_argument("--window-size=800,600")  # Set window size
    
    driver = None
    
    try:
        # Launch the browser
        driver = uc.Chrome(options=options, driver_executable_path=driver_path)
        
        # Word to search for
        word = "привет"
        
        # Open the specific Wiktionary page for the word
        driver.get(f"https://en.wiktionary.org/wiki/{word}")
        
        try:
            # Wait for the Pronunciation section header to be present
            wait = WebDriverWait(driver, 10)
            pronunciation_header = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[@id='Pronunciation']")))
            
            # Find the ul element that follows the Pronunciation section header
            pronunciation_ul = pronunciation_header.find_element(By.XPATH, "./following::ul[1]")
            
            # Extract and print the content of each li element within the ul
            li_elements = pronunciation_ul.find_elements(By.TAG_NAME, "li")
            for li in li_elements:
                print(li.text)
            
        except (NoSuchElementException, TimeoutException):
            print("Pronunciation section or content not found.")
        
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
