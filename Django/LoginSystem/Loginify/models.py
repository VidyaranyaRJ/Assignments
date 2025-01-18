from django.db import models

class UserDetails(models.Model):
    username = models.CharField(max_length=50, unique=True)  # Unique username
    email = models.EmailField(unique=True)  # Ensure unique email
    password = models.CharField(max_length=128, blank=True)  # Increased max_length for secure password storage

    def __str__(self):  # Fix the typo in method name
        return self.username
