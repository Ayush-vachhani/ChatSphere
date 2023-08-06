from django.db import models

class Signup(models.Model):
    objects = None
    id = models.AutoField
    name= models.CharField(max_length=50,default="")
    last_name= models.CharField(max_length=50,default="")
    full_name= models.CharField(max_length=50,default="")
    initials = models.CharField(max_length=2, default="")
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    isloggedin = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.name and self.last_name:
            self.initials = self.name[0] + self.last_name[0]
            self.full_name = self.name + " " + self.last_name
            user = UserNames(full_name=self.full_name)
            user.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

class UserNames(models.Model):
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

class Chat(models.Model):
    user1_name = models.CharField(max_length=50)
    user2_name = models.CharField(max_length=50)
    messages = models.JSONField(default=list)

    def __str__(self):
        return f"{self.user1_name} and {self.user2_name}'s chat"

    def save(self, *args, **kwargs):
        # Sort the user names alphabetically
        self.user1_name, self.user2_name = sorted([self.user1_name, self.user2_name])
        super().save(*args, **kwargs)