from django.db import models

class AppUser(models.Model):
    first_name = models.CharField(max_length=30)  

    last_name = models.CharField(max_length=30)   

    email = models.EmailField(unique=True)       

    password = models.CharField(max_length=128)   

    created_at = models.DateTimeField(auto_now_add=True)  

    
        
        