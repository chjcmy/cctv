from django.db import models
from backend import settings
from imagekit.models import ProcessedImageField
from django.core.files.storage import FileSystemStorage

# Create your models here.
from user.models import User

def image_path(instance, filename):
    if instance.category == '2':
        path = 'my_db/{}/family/{}'.format(instance.user_id[0]['id'], filename)
    elif instance.category == '1':
        path = 'my_db/{}/known/{}'.format(instance.user_id[0]['id'], filename)
    elif instance.category == '0':
        path = 'my_db/{}/unknown/{}'.format(instance.user_id[0]['id'], filename)
    else:
        path = 'my_db/{}/{}/{}'.format(instance.user_id[0]['id'], instance.category, filename)
    return path

class People(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.IntegerField(blank=True)
    danger = models.IntegerField(blank=True)
    pub_date = models.DateTimeField(auto_now=True)
    fs = FileSystemStorage(location=settings.IMAGES_DIR)
    pic = models.ImageField(blank=True, null=True)
    pic = ProcessedImageField(upload_to=image_path, storage=fs)

def __str__(self):
    return self.user
