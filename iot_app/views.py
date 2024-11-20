from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from django.http import JsonResponse
import json
from.scripts.change_device_twin import upadteTwin

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@api_view(['PATCH'])
def twin(request):
    data= json.loads(request.body)

    desired_state= data.get("desiredState")
    print(desired_state)

    if desired_state:
        flag= upadteTwin(desired_state)
        if flag:
            return JsonResponse(
                {"message":"twin succesfully updated"}, status= 200
            )
        else:
            return JsonResponse(
                {"error":"there was soem issues"}, status= 400
            )




    