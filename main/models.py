from django.db import models
from django.core.validators import RegexValidator

from image_cropping import ImageRatioField

import os
from PIL import Image
# Create your models here.
choices=(
    ('5x5','5x5'),
    ('10x10','10x10'),
)
class Art(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='art/')
    picture2 = models.ImageField(upload_to='art/', blank=True, null=True)
    picture3 = models.ImageField(upload_to='art/', blank=True, null=True)
    picture4 = models.ImageField(upload_to='art/', blank=True, null=True)
    description = models.TextField()
    best_size = models.CharField(max_length=15, blank=True, choices=choices)
    pub_date = models.DateField('publish date')
    cropped =  models.ImageField(upload_to='art_croped/', blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


    def save(self, *args, **kwargs):
        basepath = 'art_croped'
        homepath = '/home/priya/Akshat/nityarepo/v0.5/nityadiswebsite/media/art_croped'

        if self.picture :
            image  = Image.open(self.picture)
            width  = image.size[0]
            height = image.size[1]

            aspect = width / float(height)

            ideal_width = 430
            ideal_height = 360

            ideal_aspect = ideal_width / float(ideal_height)

            if aspect > ideal_aspect:
                # Then crop the left and right edges:
                new_width = int(ideal_aspect * height)
                offset = (width - new_width) / 2
                resize = (offset, 0, width - offset, height)
            else:
                # ... crop the top and bottom:
                new_height = int(width / ideal_aspect)
                offset = (height - new_height) / 2
                resize = (0, offset, width, height - offset)

            thumb = image.crop(resize).resize((ideal_width, ideal_height), Image.ANTIALIAS)

            thumb.save(os.path.join(homepath,self.picture.name.split('/')[-1]))
            self.cropped = os.path.join(basepath,self.picture.name.split('/')[-1])

        super(Art, self).save(*args, **kwargs)


class Commission(models.Model):
    name = models.CharField(max_length=50)
    art = models.ForeignKey(Art, on_delete=models.PROTECT)
    size = models.CharField(max_length=15, choices=choices)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    details = models.TextField()
    attachment = models.ImageField(upload_to='attachment/', blank=True, null=True)
    email = models.EmailField()
    address = models.CharField(max_length=100)

    pub_date = models.DateField('asked on')
    sub_date = models.DateField('submited on')
    done = models.BooleanField('submited?',default=False)

    def __str__(self):
        return f"{self.name}s {self.art.name}"

    def get_model_fields(model):
        return model._meta.fields
