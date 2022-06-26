from django.conf import settings
from django.core.files.storage import FileSystemStorage


def photo():
    return FileSystemStorage(location='/home/danaukes/Desktop/photos')


def cache():
    return FileSystemStorage(location=settings.BASE_DIR / 'cache')
