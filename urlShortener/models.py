from hashlib import md5

from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from graphql import GraphQLError


class URL(models.Model):
    full_url = models.URLField(unique=True)
    url_hash = models.URLField(unique=True)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def clicked(self):
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:
            # self.url_hash = md5(self.full_url.encode()).hexdigest()[:10]
            self.url_hash = "temp"
        validate = URLValidator()
        try:
            validate(self.full_url)
        except ValidationError as e:
            raise GraphQLError('invalid url')

        
        return super().save(*args, **kwargs)

def urlEncode(full_url):
    client_obj = URL.objects.get(full_url=full_url)
    urlID = client_obj.id
    validstr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    encodedURL = ""
    base = len(validstr)
    if(urlID == 0):
        return encodedURL + validstr[0]

    while (urlID > 0):
        encodedURL = encodedURL + validstr[((int)(urlID % base)) - 1]
        urlID = (int)(urlID / base)
    encodedURL = ''.join(reversed(encodedURL))
    URL.objects.filter(full_url=full_url).update(url_hash=encodedURL)
    return encodedURL

def createHash(full_url):
   url = URL(full_url=full_url)
   url.save()
   hashed_url = urlEncode(full_url)
   return hashed_url