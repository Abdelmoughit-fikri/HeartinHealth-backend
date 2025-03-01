from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
import bleach

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
    
class Newsletter(models.Model):
    subject = models.CharField(max_length=200)
    message = CKEditor5Field(config_name='extends')
    image = models.ImageField(upload_to='newsletter/')
    recipients = models.ManyToManyField(Subscriber)
    sent_at = models.DateTimeField(auto_now=True)
    sent = models.BooleanField(default=False)
    def __str__(self):
        return self.subject
     