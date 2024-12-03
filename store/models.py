from django.db import models

# Create your models here.
class NationalPark(models.Model):
  id = models.AutoField(primary_key=True)
  name=models.CharField(max_length=255, null=False, blank=False)
  state=models.CharField(max_length=255, null=False, blank=False)
  picture=models.ImageField(max_length=255, null=False, blank=False)
  created=models.DateTimeField(auto_now_add=True)
  established=models.DateTimeField()
  
  def __str__(self):
    return self.name
  
  
  
class DifficultyType(models.Model):
  id = models.AutoField(primary_key=True)
  name=models.CharField(max_length=255, unique=True, null=False, blank=False)
  def __str__(self):
    return self.name
  
class Trail(models.Model):
  id = models.AutoField(primary_key=True)
  name=models.CharField(max_length=255, null=False, blank=False)
  distance=models.CharField(max_length=255, null=False, blank=False)
  elevation=models.CharField(max_length=255, null=False, blank=False)
  date_created=models.DateTimeField(auto_now_add=True)
  difficultyType=models.ForeignKey(
    DifficultyType, on_delete=models.CASCADE, related_name='trails'
  ) 
  nationalPark=models.ForeignKey(
    NationalPark, on_delete=models.CASCADE, related_name='trails'
  )
  def __str__(self):
    return self.name