from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    update_date = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(blank=True, null=True, upload_to="accounts/avatar/%Y/%m/%d",
                               help_text="48px * 48px 크기의 png/jpg 파일을 업로드해주세요.")
