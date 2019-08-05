from django.db import models

# Create your models here.
class Project(models.Model):
  name=models.CharField(max_length=40)
  image=models.ImageField(upload_to='projects/',default='tech.jpeg')
  # user=models.ForeignKey(User,on_delete=models.CASCADE)
  description=models.TextField()
  link=models.CharField(max_length=60,default='site.com')

  def __str__(self):
    return self.name

  def project_save(self):
    self.save()

  def project_delete(self):
    self.delete()

  class Meta:
    ordering=['name']

