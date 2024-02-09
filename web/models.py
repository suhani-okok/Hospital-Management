from django.db import models


class Address(models.Model):
    id = models.BigAutoField(primary_key=True)
    line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.line1}, {self.city}, {self.state}, {self.pincode}"


class Member(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    username = models.CharField(max_length=30)
    email = models.EmailField(default='default_email@example.com')
    password = models.CharField(max_length=12)
    confirm_password = models.CharField(max_length=12, default='default_value')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.username})"
