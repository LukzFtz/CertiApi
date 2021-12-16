from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .serializers import ExtensoSerializer
from rest_framework.renderers import JSONRenderer
from .models import Number
from .functions import transformNumToStr
from rest_framework.views import APIView
from rest_framework.response import Response


class extenso(APIView):

    def get(self, request, pathRequest , format=None):
        if(int(pathRequest)):

            pathInt = int(pathRequest)

            if pathInt >= -99999 and pathInt <= 99999:


                number = transformNumToStr(str(pathInt))

                pathObject = Number(extenso= str(number))
                serializer = ExtensoSerializer(pathObject)
                serializer.data

                return Response(serializer.data)
