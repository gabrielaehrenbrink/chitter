import re

class PostParametersValidator:
    def __init__(self, post_content):
        self.post_content = post_content


    def is_valid(self):
        if not self.is_post_content_valid():
            return False
        return True
        
    
    def generate_errors(self):
        errors = []
        if not self.is_post_content_valid():
            errors.append("Content must not be blank")
        return errors

    def get_valid_post_content(self):
        if not self.is_post_content_valid():
            raise ValueError("Cannot get valid content")
        return self.post_content
    
    def is_post_content_valid(self):
        if self.post_content is None:
            return False
        if self.post_content == "":
            return False
        return True
    
