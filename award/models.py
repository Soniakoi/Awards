from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
  name=models.CharField(max_length=40)
  image=models.ImageField(upload_to='projects/',default='')
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  description=models.TextField()
  link=models.CharField(max_length=60,default='site.com')
  project_image = models.ImageField(upload_to = 'projects/')

  @classmethod
  def search_by_title(cls,search_term):
    award = cls.objects.filter(title__icontains=search_term)
    return news

  def __str__(self):
    return self.name

  def project_save(self):
    self.save()

  def project_delete(self):
    self.delete()

  class Meta:
    ordering=['name']


class Profile(models.Model):
  prof_pic = models.ImageField(upload_to='profile/',default='')
  bio=models.TextField()
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  contact=models.IntegerField()
  name=models.CharField(max_length=60)

  def __str__(self):
    return self.contact

  def profile_save(self):
    self.save()

  def profile_delete(self):
    self.delete()

  


