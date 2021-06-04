from django.db import models

# Create your models here.
class Job(models.Model):
	image = models.ImageField(upload_to='image/')
	summary = models.CharField(max_length=100)
	

	def __str__(self):
		t_sum= self.summary[0:10]
		return t_sum