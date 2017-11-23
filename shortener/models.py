from django.db import models
# Create your models here.

from .utils import code_generator
from .utils import create_shortcode

class KirrURL(models.Model):
    url = models.CharField(max_length=220,)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    # shortcode = models.CharField(max_length=15, null=False, blank=False)
    # shortcode = models.CharField(max_length=15, null = True)
    # shortcode = models.CharField(max_length=15 , default='')

    updated     = models.DateTimeField(auto_now = True) # everytime the model is saved
    timestamp   = models.DateTimeField(auto_now_add = True) # when model was created

    # override
    def save(self, *args, **kwargs):
        # shortcode 가 존재하지 않을 경우
        if self.shortcode is None or self.shortcode == "" :
            # self.shortcode = code_generator()
            self.shortcode = create_shortcode(self)

        super(KirrURL, self).save(*args, **kwargs)

    # def my_save(self):
    #     self.save()

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

'''
python manage.py makemigrations
python manage.py migrate
'''