from django.db import models
import time

# Create your models here.
class Diary(models.Model):
    content = models.CharField(max_length=125)
    picture = models.ImageField(
        blank=True,
        upload_to=f"diary/{time.strftime('%y/%b/%a')}/"
        )
    created_at = models.DateTimeField(auto_now_add=True)