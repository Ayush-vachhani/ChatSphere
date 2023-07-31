from django.db import models

class Information(models.Model):
    objects = None
    id = models.AutoField
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.name

class Signup(models.Model):
    objects = None
    id = models.AutoField
    name= models.CharField(max_length=50,default="")
    last_name= models.CharField(max_length=50,default="")
    initials = models.CharField(max_length=2, default="")
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    isloggedin = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.name and self.last_name:
            self.initials = self.name[0] + self.last_name[0]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email