from django.db import models

# Create your models here.
class BaseUser(models.Model):
	first_name = models.CharField( max_length=30, blank=True)
	last_name = models.CharField( max_length=30, blank=True)

class Provide(BaseUser):
	provider_name = models.CharField(('provider_name'), max_length=30, blank=True)
	user_id = models.IntegerField(null=True)
	user = models.ForeignKey(BaseUser, null=True, blank=True, related_name="The user who vouches that self.user is a provider.")
	father_key = models.ForeignKey('self', 'id', null=True)  

