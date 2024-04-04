from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from .models import Profile
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.serializers import Serializer
from .serializers import ProfileSerializer
from .forms import *


@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def ProfileList(request):

    profiles = Profile.objects.all()
    if request.GET:
        form = ProfileForm(request.GET)
        if form.is_valid():
            if form.cleaned_data["name"]:
                profiles = profiles.filter(name__contains=form.cleaned_data['name'])
    
    else :
        form = ProfileForm()

    if 'HX-Request' in request.headers:
        return Response({'profiles': profiles},template_name="template.html")

    return Response({'form':form,'profiles': profiles},template_name="profileList.html")
    
