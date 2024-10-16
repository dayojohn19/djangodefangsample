from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET','POST','DELETE','PUT'])
def getRoutes(request):
    routes = [
        {
        'Endpoint':'/notes/',
        'method':'GET',
        'body':None,
        'description':'Returns an array of notes'
    },
    {
        'Endpoint':'/notes/id',
        'method':'GET',
        'body':None,
        'description':'Returns a single note'
    },
    ]
    return Response(routes)

