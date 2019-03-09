from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
choices=(
    ('5"x5"','5x5'),
    ('10"x10"','10x10'),
)
class Art(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='art/')
    description = models.TextField()
    best_size = models.CharField(max_length=15, blank=True, choices=choices)
    pub_date = models.DateField('publish date')

    def __str__(self):
        return f"{self.name}"

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
