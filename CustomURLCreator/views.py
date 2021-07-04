from .models import CustomURL
from .serializers import URLSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST,HTTP_201_CREATED
import string
import random
from django.http import HttpResponseRedirect

def generate_short_string(string_length=7):
    # Generates a random string<Slug>
    random_string = ''
    alpha_numerals = string.ascii_letters + string.digits
    for _ in range(string_length):
        random_string = random_string + random.choice(alpha_numerals)
    return random_string


class AddURL(APIView):
    def post(self, request, *args, **kwargs):
        uri = request.data.get('url', None)
        if uri is None:
            return Response({"message": "Invalid request"}, status=HTTP_400_BAD_REQUEST)
        else:
            random_string = generate_short_string()
            service, created = CustomURL.objects.get_or_create(slug=random_string)
            if created:
                service.FullURL = uri
                ShortURL = f'http://127.0.0.1:8000/1/{random_string}/'
                service.ShortURL = ShortURL
                service.save()
                url_serializer = URLSerializer(service)
                return Response(data={'success': True, 'data': url_serializer.data}, status=HTTP_201_CREATED)
            else:
                return Response(data={'success': False, 'message': 'Invalid request'}, status=HTTP_400_BAD_REQUEST)
            


class Redirector(APIView):
    # validate short URL and Redirect short URL to its original URL
    def get(self, request, slug):
        try:
            service = CustomURL.objects.get(slug=slug)
            uri = service.FullURL
            if not uri.startswith('http://') and not uri.startswith('https://'):
                uri = f'http://{uri}'
            return HttpResponseRedirect(uri)
        except Exception as e:
            return Response({"message": "Short Url not created"},status=HTTP_400_BAD_REQUEST)
