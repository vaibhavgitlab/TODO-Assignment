from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Todos(models.Model):
    task = models.CharField(blank = True, max_length = 100)
    status = models.CharField(blank = True, max_length = 100)
    
