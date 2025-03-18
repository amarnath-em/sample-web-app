from django.db import models

# Create your models here.

class censorInfo(models.Model):
    rating=models.CharField(max_length=10,null=True)
    certified_by=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.certified_by


class director(models.Model):
    name=models.CharField(max_length=300)
    def __str__(self):
        return self.name

class Actor(models.Model):
    name=models.CharField(max_length=300)
    def __str__(self):
        return self.name

class MovieInfo(models.Model):
    title=models.CharField(max_length=250)
    year=models.IntegerField(null=True)
    description=models.TextField()
    poster=models.ImageField(upload_to='images/',null=True)
    censor_details=models.OneToOneField(censorInfo,on_delete=models.SET_NULL,related_name='movie',null=True)


    directed_by=models.ForeignKey(director,null=True,
                                  on_delete=models.CASCADE,
                                  related_name='directed_movies')
    acters=models.ManyToManyField(Actor,related_name='acted_movies')


    def __str__(self):
        return self.title


    