from django.db import models

# Create your models here.
class Members(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.IntegerField()
    image = models.ImageField()
    email = models.EmailField(max_length=50)
    passwd = models.CharField(max_length=50)

    def __str__(self):
        return self.fname + '' + self.lname