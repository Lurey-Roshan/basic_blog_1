from django.db import models
import datetime

from django.utils import timezone
# Create your models here.
class Blog(models.Model):

	title =models.CharField(max_length=100)
	date = models.DateTimeField(default=timezone.now )
	content = models.TextField()
	image = models.ImageField(upload_to ='image/')

	def __str__(self):
		return self.title

	def summary(self):
		if len(self.content)<100:
			return self.content
		else:

			return self.content[:100]+"...."
