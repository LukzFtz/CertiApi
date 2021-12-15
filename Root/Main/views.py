from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .serializers import ExtensoSerializer
from rest_framework.renderers import JSONRenderer
from .models import Number
from .functions import transformNumToStr

@require_http_methods(["GET"])
def extenso(request, pathRequest):

    if(int(pathRequest)):

        pathInt = int(pathRequest)

        if pathInt >= -99999 and pathInt <= 99999:


            number = transformNumToStr(str(pathInt))

            pathObject = Number(extenso= str(number))
            serializer = ExtensoSerializer(pathObject)
            serializer.data

            json = JSONRenderer().render(serializer.data)
            json

            return HttpResponse( json )

# Create your views here.
