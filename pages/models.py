from django.db import models

# Create your models here.
class Female(models.Model):
    name = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.name_Female
class Male(models.Model) :
    name_male = models.CharField(max_length=50, null=True)


girls = models.OneToOneField(Female, on_delete=models.CASCADE)
def __str__(self):
    return self.name_Male