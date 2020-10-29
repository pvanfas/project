from django.db import models

# Create your models here.
SOCIAL_CHOICES = (
	('android', 'android'),('apple', 'apple'),('behance', 'behance'),('dribbble', 'dribbble'),('envelope', 'email'),
	('facebook', 'facebook'),('flickr', 'flickr'),('foursquare', 'foursquare'),('google', 'google'),
	('instagram', 'instagram'),('linkedin', 'linkedin'),('meetup', 'meetup'),('pinterest', 'pinterest'),
	('reddit', 'reddit'),('rss', 'RSS'),('soundcloud', 'soundcloud'),('snapchat-ghost', 'snapchat'),
	('skype', 'skype'),('spotify', 'spotify'),('telegram', 'telegram'),('tumblr', 'tumblr'),('twitter', 'twitter'),
	('vimeo', 'vimeo'),('whatsapp', 'whatsapp'),('yahoo', 'yahoo'),('youtube-play', 'youtube'),
)

class Social(models.Model):
	order = models.IntegerField(unique=True)
	media = models.CharField(max_length=15,choices=SOCIAL_CHOICES)
	link = models.CharField(max_length=150)

	class Meta:
		ordering = ('order', )
		verbose_name = ('Social Media')
		verbose_name_plural = ('Social Medias')

	def __str__(self):
		return str(self.media)
