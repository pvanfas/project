from .models import Social


def main_context(request):
    return {
        'domain' : request.META['HTTP_HOST'],
        'socials' : Social.objects.all(),
    }
