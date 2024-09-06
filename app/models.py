from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class reservation(models.Model):
    name=models.CharField('Name', max_length=200)
    number=models.IntegerField('Phone Number')
    E_mail=models.EmailField('E_Mail', blank=False)
    Description= models.TextField('Any Special Request', max_length=200)
    Quantity = models.PositiveIntegerField('No.of People',
        validators=[MinValueValidator(5), MaxValueValidator(50)]
    )
    Event_date = models.DateField('year/month/day')
    Event_time = models.TimeField('hour/minute/second')





    def __str__(self):
        return self.name



class contact(models.Model):
    Name=models.CharField('Name', max_length=200)
    E_mail=models.EmailField('E_Mail', blank=False)
    Number=models.IntegerField('Phone Number')
    Description= models.TextField('Your message Request', max_length=200)


    def __str__(self):
        return self.Name
    


class image(models.Model):
    Name=models.CharField(max_length=25)
    Description= models.TextField('Your message Request', max_length=200)
    image_view= models.ImageField(null=True, blank=True, upload_to="imagess/")
    
    
    def __str__(self):
        return self.Name
        
        