from django.contrib import admin
from .models import Social


class SocialAdmin(admin.ModelAdmin):
	list_display = ('order','media','link')
	ordering = ('order',)

admin.site.register(Social,SocialAdmin)
