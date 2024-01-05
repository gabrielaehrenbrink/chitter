from playwright.sync_api import Page, expect
import requests


def test_get_homepage(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    text_content = page.locator('h5')
    expect(text_content).to_have_text("See what's happening in the world right now... ")

def test_get_posts(page, test_web_address, db_connection):
    db_connection.seed('seeds/posts.sql')
    page.goto(f"http://{test_web_address}/posts")
    text_content = page.locator('h2')
    expect(text_content).to_have_text(['\n                Just In: Penguins found dancing in the streets of Tokyo!  #PenguinParty #TokyoAdventures \n                 gab123\n            ', '\n                Taylor Swift Drops Surprise Album: Fans in Shock!  #SwiftiesReact #SurpriseAlbum \n                 b0b\n            ', '\n                Amazing Discovery: Unicorns spotted in the Amazon Rainforest!  #UnicornAdventure #AmazonDiscovery \n                 user123\n            ', '\n                Exciting News: Just heard that Brazil won the 2026 World Cup!  #Champions #Brazil2026 \n                 gab123\n            '])

def test_get_newaccound(page, test_web_address):
    page.goto(f"http://{test_web_address}/newaccount")
    text_content = page.locator('h1')
    expect(text_content).to_have_text('New Account')


def test_get_login(page, test_web_address):
    page.goto(f"http://{test_web_address}/login")
    text_content = page.locator('h1')
    expect(text_content).to_have_text('Login')

def test_create_post(page, test_web_address, db_connection):
    db_connection.seed("seeds/posts.sql")
    page.goto(f"http://{test_web_address}/newpost")
    page.fill("input#username", "gab123")
    page.fill("input#textInput", "This is my first time using Chitter!")
    page.click('text="Post"')

    assert page.url == f"http://{test_web_address}/newpost"

    assert page.text_content('text=This is my first time using Chitter!')

def test_create_new_account(page, test_web_address, db_connection):
    db_connection.seed("seeds/posts.sql")
    page.goto(f"http://{test_web_address}/newaccount")
    page.fill("input#username", "mike11")
    page.fill("input#email", "mike11@email.com")
    page.fill("input#user_password", "mypassword11!")
    page.click('text="Create Account"')

    assert page.url == f"http://{test_web_address}/newaccount"


def test_create_new_account_blank_username(page, test_web_address, db_connection):
    db_connection.seed("seeds/posts.sql")
    page.goto(f"http://{test_web_address}/newaccount")
    page.fill("input#username", "")
    page.fill("input#email", "mike11@email.com")
    page.fill("input#user_password", "mypassword11!")
    page.click('text="Create Account"')

    errors_tag = page.locator(".t-errors")
    expect(errors_tag).to_have_text("Your submission contains errors: Username is required., Password or email is not valid. Must enter valid email. Password must have at least 8 characters, including a letter, a number and special character")

def test_create_new_account_blank_email(page, test_web_address, db_connection):
    db_connection.seed("seeds/posts.sql")
    page.goto(f"http://{test_web_address}/newaccount")
    page.fill("input#username", "mike11")
    page.fill("input#email", "")
    page.fill("input#user_password", "mypassword11!")
    page.click('text="Create Account"')

    errors_tag = page.locator(".t-errors")
    expect(errors_tag).to_have_text("Your submission contains errors: Email is required., Password or email is not valid. Must enter valid email. Password must have at least 8 characters, including a letter, a number and special character")




def test_create_new_account_invalid_email(page, test_web_address, db_connection):
    db_connection.seed("seeds/posts.sql")
    page.goto(f"http://{test_web_address}/newaccount")
    page.fill("input#username", "mike112")
    page.fill("input#email", "email")
    page.fill("input#user_password", "mypassword11!")
    page.click('text="Create Account"')

    errors_tag = page.locator(".t-errors")
    expect(errors_tag).to_have_text("Your submission contains errors: Password or email is not valid. Must enter valid email. Password must have at least 8 characters, including a letter, a number and special character")



