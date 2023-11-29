from django.core.validators import RegexValidator
from django.db import models as django_models
import string, random

# Create your models here.
# models = framework in python allows us easily write and use dbs w/out specific code
# basic rule=fat models, thin views, ie most logic in models
def generate_user_id():
    length = 10
    while True:
        characters = string.ascii_letters + string.digits
        user_id = ''.join(random.choices(characters, k=length))
        if User.objects.filter(user_id=user_id).count() == 0:
            break
    return user_id

class User(django_models.Model):
    user_id = django_models.CharField(max_length=10, default=generate_user_id)
    firstName = django_models.CharField(max_length=20, unique=True, null=False, blank=False,
                                  validators=[RegexValidator(regex='^[A-Za-z]*$', message='Only letters are allowed.')])
    lastName = django_models.CharField(max_length=20, unique=True, null=False, blank=False,
                                validators=[RegexValidator(regex='^[A-Za-z]*$', message='Only letters are allowed.')])
    email = django_models.EmailField(max_length=50, unique=True, null=False, blank=False)
    phone = django_models.IntegerField(max_length=10, unique=True, null=False, blank=False)
    #customer_id = django_models.IntegerField(max_length=15, unique=True, null=False, blank=False)

    # User methods