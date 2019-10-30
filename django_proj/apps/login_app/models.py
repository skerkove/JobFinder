from django.db import models
import re


class UserManager(models.Manager):

    def basic_validator(self, postData):
        errors = {}
        if (len(postData['first_name']) < 2) or (len(postData['last_name'])
                < 2) or (len(postData['email']) < 1):
            errors["blank"] = "All fields are required!"

        if not (postData['first_name'].isalpha() and postData['last_name'].isalpha()):
            errors["syntax"] = "First and Last Name can only contain letters!"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')    
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid Email Address!"
        try:
            user = User.objects.get(email = postData['email'])
            errors ["email"] = "Email is already in use!"
        except:
            pass
        if postData["password"] != postData["pw_confirm"]:
            errors["pw_confirm"] = "Password and confirmation do not match!"
        return errors



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()