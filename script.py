from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Set the path to your webdriver (e.g., chromedriver.exe)
webdriver_path = 'C:/Users/chris/Desktop/chromedriver-win64/chromedriver'  # Replace with the actual path to your chromedriver executable

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=webdriver_path)

# Navigate to the website
driver.get('https://www.olightstore.ca/olight-make-a-wish-christmas')  # Replace with your website URL
WebDriverWait(driver, 20).until(EC.url_to_be('https://www.olightstore.ca/olight-make-a-wish-christmas'))

# Add a longer delay to allow the page to load
time.sleep(10)

# Click on the "Login" button
login_button_xpath = "//span[text()='Login']"

# Wait for the login button to be clickable
login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, login_button_xpath)))

# Perform actions with the login button, e.g., click
login_button.click()

# Wait for the pop-up to appear and find the "Register" option
register_option_xpath = "//span[text()='Register']"

try:
    register_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, register_option_xpath)))
    # Perform actions with the registration option, e.g., click
    register_option.click()
except TimeoutException:
    print("TimeoutException: Registration button not found or not clickable. Skipping registration.")

# Example: Fill in the registration form with an email (modify as needed)
email = 'cpffeelover7654@gmail.com'

# Find the registration form element and fill it in
email_field = driver.find_element(By.ID, 'free-solo-2-demo')  # Replace with the actual ID of the email field
email_field.clear()  # Clear any existing text in the field
email_field.send_keys(email)

# Submit the form
email_field.submit()

# Wait for the registration to complete (adjust wait time as needed)
wait = WebDriverWait(driver, 10)

# Add a wait for the URL change, assuming the registration was successful
try:
    wait.until(EC.url_to_be('https://www.olightstore.ca/'))  # Replace with the expected URL after registration
except TimeoutException:
    print("TimeoutException: URL did not change to the expected URL. Continue with the rest of the script.")

# Continue with the rest of your script...


# Click on the box that says "Make a Wish"
make_a_wish_box_xpath = '//*[@id="content-fill"]/div[2]/div/div/div/div[2]/div/div/div/div[4]/a/div'
make_a_wish_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, make_a_wish_box_xpath)))
make_a_wish_box.click()

# Click on the link to view all reviews
view_all_reviews_link_xpath = '//*[@id="navLocal"]/div[2]/div/div[1]/div/div[1]'
view_all_reviews_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, view_all_reviews_link_xpath)))
view_all_reviews_link.click()

# Assuming you want to find a comment containing specific text
target_comment_text = "I’ve been carrying the Baton4 since its release & I’m absolutely amazed by the performance of this tiny light. The Baton4 Premium is the little Olight that could. 1300 Lumens at 170 Meters and with the charge case you have the ability to charge your light up to 5x while on the go. Olight describes the Baton4 “ mini outside, mighty inside” & that is 100% truth. When clipped inside the pocket I can reach in & out with no snagging or scratching & plenty of room for other items. It’s also available in OD Green w/ a gold/brass colour pocket clip that i think is just stunning."

# Example: Locate and like the target comment on one of the pages
# You may need to adapt this based on the structure of the website

# Loop through the pages (adjust the range accordingly)
for page_number in range(1, 11):  # Assuming there are 10 pages of comments
    # Example: Replace with the actual XPath or locator for comments on the page
    comments_on_page_xpath ='//*[@id="reviews"]/div[2]/div[2]/div[2]/div[9]/div/div[2]/div[2]/div/div'

    # Find all comments on the current page
    comments_on_page = driver.find_elements(By.XPATH, comments_on_page_xpath)

    # Loop through each comment on the page
    for comment in comments_on_page:
        # Extract text content of the comment (modify as needed)
        comment_text = comment.text

        # Check if the target comment is found
        if target_comment_text in comment_text:
            # Like the comment (modify the XPath accordingly)
            like_button_xpath = './/div[@class="like-button"]/span'
            like_button = comment.find_element(By.XPATH, like_button_xpath)
            like_button.click()

            # Print a message indicating that the comment is liked
            print(f"Liked the comment: {comment_text}")

            # Exit the loop once the target comment is found and liked
            break

    # Navigate to the next page (modify the XPath accordingly)
    next_page_button_xpath = '//*[@id="reviews"]/div[2]/div[2]/div[3]/nav/ul/li[9]/button'
    next_page_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, next_page_button_xpath)))
    next_page_button.click()

    # Wait for the new page to load (adjust wait time as needed)
    wait.until(EC.presence_of_element_located((By.XPATH, comments_on_page_xpath)))

# Close the browser
driver.quit()
