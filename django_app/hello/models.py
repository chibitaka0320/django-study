import re
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ValidationError

def number_only(value):
    if (re.match(r"^[0-9]*$", value) == None):
        raise ValidationError("%(value)s is no Number!", params={"value": value})

class Friend(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(150)
    ])
    birthday = models.DateField()
    
    def __str__(self):
        return f"<Friend:id={str(self.id)}, {self.name}({str(self.age)})>"

class Message(models.Model):
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"<Message:id={str(self.id)}, {self.title}({str(self.pub_date)})>"
    
    class Meta:
        ordering = ("pub_date",)