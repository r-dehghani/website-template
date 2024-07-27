from django.db import models

from myproject.common.models import BaseModel


class Post(BaseModel):
    title = models.CharField(max_length=250)
    