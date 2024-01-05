import re
import sqlite3


class AccountParametersValidator:
    def __init__(self, username, email, user_password):
        self.username = username
        self.email = email
        self.user_password = user_password

    def is_valid(self):
        if not self.is_username_valid():
            return False
        if not self.is_email_valid():
            return False
        if not self.is_user_password_valid():
            return False
        return True
        
    
    def generate_errors(self):
        errors = []
        if not self.is_username_valid():
            errors.append("Content must not be blank")
        if not self.is_email_valid():
            errors.append("You must enter a valid email")
        if not self.is_user_password_valid():
            errors.append("Password must have at least 8 characters, include a letter, number and special character")
        return errors

    def get_valid_username(self):
        if not self.is_username_valid():
            raise ValueError("Cannot get valid username")
        return self.username
    
    def get_valid_email(self):
        if not self.is_email_valid():
            raise ValueError("Cannot get valid email")
        return self.email
    
    def get_valid_user_password(self):
        if not self.is_user_password_valid():
            raise ValueError("Cannot get valid password")
        return self.password

    def is_username_valid(self):
        if self.username is None:
            return False
        if self.username == "":
            return False
        return True


    # add def is_password_valid 
    def is_user_password_valid(self):
        if self.user_password is None or self.user_password == "":
            return False
        if len(self.user_password) < 8:
            return False

        # Check if the password includes letters, numbers, and special characters
        has_letters = any(char.isalpha() for char in self.user_password)
        has_numbers = any(char.isdigit() for char in self.user_password)
        has_special_chars = re.search(r"[!@#$%^&*(),.?\":{}|<>]", self.user_password) is not None

        return has_letters and has_numbers and has_special_chars

    # add def is_email_valid 
    def is_email_valid(self):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            return False
        return True


