from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
# Create your models here.

class Condidate(models.Model):
    user=models.ForeignKey(User, verbose_name="Condidate", on_delete=models.CASCADE)
    name=models.CharField("Condidate name", max_length=200)
    fname=models.CharField(("Father name"), max_length=200)
    pname=models.CharField(("Patient name"), max_length=200)
    serviceType=models.CharField("Service Type", max_length=200)
    Entrytime=models.TimeField("Entry Time", default=datetime.now)
    Exittime=models.TimeField("Exit Time", default=datetime.now)
    date=models.DateField(("Date"), auto_now=False, auto_now_add=False,default=datetime.today)
    
    def __str__(self) -> str:
        return self.user.username