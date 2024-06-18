from playwright.sync_api import Page, expect



def test_get_homepage(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    text_content = page.locator('h5')
    expect(text_content).to_have_text("See what's happening in the world right now... ")

def test_get_posts(page, test_web_address, db_connection):
    db_connection.seed('seeds/posts.sql')
    # Navigate to the posts page
    page.goto(f"http://{test_web_address}/posts")  
    # Wait for the locator to be visible
    page.wait_for_selector('h3')  
    # Locate the text content of posts
    text_content = page.locator('h3')
    # Define the expected texts
    expected_texts = [
        'Exciting News: Just heard that Brazil won the 2026 World Cup!  #Champions #Brazil2026\nPosted by: gab123',
        'Amazing Discovery: Unicorns spotted in the Amazon Rainforest!  #UnicornAdventure #AmazonDiscovery\nPosted by: user123',
        'Taylor Swift Drops Surprise Album: Fans in Shock!  #SwiftiesReact #SurpriseAlbum\nPosted by: b0b',
        'Just In: Penguins found dancing in the streets of Tokyo!  #PenguinParty #TokyoAdventures\nPosted by: gab123'
    ]
    # Check if the text content matches the expected texts
    expect(text_content).to_have_text(expected_texts)

def test_login_success(page: Page, test_web_address: str, db_connection):
    # Seed the database with the necessary test data
    db_connection.seed("seeds/accounts.sql") 
    db_connection.seed('seeds/posts.sql')

    # Navigate to the login page
    page.goto(f"http://{test_web_address}/login")

    # Fill in the login form
    page.fill("input#username", "gab123")
    page.fill("input#user_password", "password123!")

    # Submit the form
    page.click('button[type="submit"]')

    # Verify that the user is redirected to the posts page
    expect(page).to_have_url(f"http://{test_web_address}/posts")
    # Verify that the posts page contains the expected text
    text_content = page.locator('h1')
    expect(text_content).to_have_text('Latest Posts')

def test_login_failure(page: Page, test_web_address: str, db_connection):
    # Seed the database with the necessary test data
    db_connection.seed("seeds/accounts.sql") 
    db_connection.seed('seeds/posts.sql')

    # Navigate to the login page
    page.goto(f"http://{test_web_address}/login")

    # Fill in the login form with incorrect password
    page.fill("input#username", "testuser")
    page.fill("input#user_password", "wrongpassword")

    # Submit the form
    page.click('button[type="submit"]')

    # Verify that the user stays on the login page
    expect(page).to_have_url(f"http://{test_web_address}/login")
    # Verify that the error message is displayed
    error_message = page.locator('.alert.alert-danger')
    expect(error_message).to_have_text('Invalid username or password. Please try again.')

def test_get_new_account(page, test_web_address):
    page.goto(f"http://{test_web_address}/newaccount")
    text_content = page.locator('h1')
    expect(text_content).to_have_text('New Account')

def test_get_login(page, test_web_address):
    page.goto(f"http://{test_web_address}/login")
    text_content = page.locator('h1')
    expect(text_content).to_have_text('Login')

def test_create_new_account(page, test_web_address, db_connection):
    db_connection.seed("seeds/accounts.sql") 
    db_connection.seed("seeds/posts.sql")
    page.goto(f"http://{test_web_address}/newaccount")
    page.fill("input#username", "mike11")
    page.fill("input#email", "mike11@email.com")
    page.fill("input#user_password", "mypassword11!")
    page.click('text="Create Account"')

    assert page.url == f"http://{test_web_address}/newaccount"


def test_create_new_account_blank_email(page, test_web_address, db_connection):
    db_connection.seed("seeds/accounts.sql") 
    db_connection.seed("seeds/posts.sql")
    page.goto(f"http://{test_web_address}/newaccount")
    page.fill("input#username", "mike11")
    page.fill("input#email", "")
    page.fill("input#user_password", "mypassword11!")
    page.fill("input#confirm_password", "mypassword11!")
    page.click('text="Create Account"')

    errors_tag = page.locator(".t-errors")
    expect(errors_tag).to_have_text("Your submission contains errors: Email is required")


def test_create_new_account_invalid_email(page, test_web_address, db_connection):
    db_connection.seed("seeds/accounts.sql") 
    db_connection.seed("seeds/posts.sql")
    page.goto(f"http://{test_web_address}/newaccount")
    page.fill("input#username", "mike112")
    page.fill("input#email", "email")
    page.fill("input#user_password", "mypassword11!")
    page.fill("input#confirm_password", "mypassword11!")
    page.click('text="Create Account"')

    errors_tag = page.locator(".t-errors")
    expected_text = (
        "Your submission contains errors:\n"
        "You must enter a valid email"
    )
    expect(errors_tag).to_have_text(expected_text)
