from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.decorators import api_view


@authentication_classes([])
@permission_classes([])
@api_view(['POST'])
def upload_image(request):

    final_list = []
    for file in request.FILES:
        print(file, file.name)
        # fss = FileSystemStorage()
        # file = fss.save(file.name, file)
        # file_url = fss.url(file)
        # final_list.append(file_url)

    return JsonResponse({'urls': ", ".join(final_list)})


