# from ast import Global
# import json

# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404
from app.permissions import GlobalDefaultPermission
from genres.models import Genre

# from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from genres.serializers import GenreSerializer

# from genres.permissions import GenrePermissionClass
# Create your views here.

# @csrf_exempt
# def genre_create_list_view(request):
#     if request.method == 'GET':
#         genres = Genre.objects.all()
#         data = [{'id': genre.id, 'name': genre.name} for genre in genres]
#         return JsonResponse({'genres': data})
#     elif request.method =='POST':
#         data = json.loads(request.body.decode('utf-8'))
#         print(">>>", type(data), data)
#         genre = Genre(name=data['name'])
#         genre.save()
#         return JsonResponse({'id': genre.id, 'name': genre.name}, status=201)


class GenreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, GlobalDefaultPermission]


# @csrf_exempt
# def genre_details_update_delete_view(request, pk):
#     genre = get_object_or_404(Genre, pk=pk)
#     if request.method == 'GET':
#         data = {'genre': {'id':genre.id, 'name':genre.name}}
#         return JsonResponse(data)
#     elif request.method == 'PUT':

#         data = json.loads(request.body.decode('utf-8'))
#         genre.name = data['name']
#         genre.save()
#         return JsonResponse({'genre': {'id':genre.id, 'name':genre.name}})
#     elif request.method == 'DELETE':
#         genre.delete()
#         return JsonResponse({'message': 'Genre deleted succesfully!'}, status=202)


class GenreRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticated, GlobalDefaultPermission]
