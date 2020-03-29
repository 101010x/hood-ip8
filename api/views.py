from django.shortcuts import render, Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.parsers import FileUploadParser
import cloudinary.uploader
from .serializers import *
from .models import *

#Registration
class RegisterUser(APIView):
    '''Class view to register new users'''
    permission_classes = [AllowAny]
    def post(self, request, format=None):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



#Hood
class HoodCreateView(APIView):
    '''Class view to get a list of views & post a new hood'''
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        '''To get all the hoods'''
        if request.user.is_superuser == True:
            all_hoods = Hood.objects.all()
            serializers = HoodSerializer(all_hoods, many=True)
            return Response(serializers.data)
        else:
            return Http404

    def post(self, request, format=None):
        '''Creating a new Hood'''
        if request.user.is_superuser == True:
            serializers = HoodSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serialiazers.data, status=status.HTTP_201_CREATED)
            return Response(serialiazers.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Http404

class HoodDetailsView(APIView):
    '''Class view for a specific hood'''
    permission_classes = [IsAuthenticated] 

    def get_hood(self, id):
        try:
            return Hood.objects.get(pk = id)
        except Hood.DoesNotExist:
            return Http404
    
    #Only allow hood members
    def get(self, request, id, format=None):
        hood = self.get_hood(id)
        profile = Profile.objects.get(user=request.user)
        if profile.hood == hood:
            serializers = HoodSerializer(hood)
            return Response(serializers.data)
        elif request.user.is_staff == True:
            serializers = HoodSerializer(hood)
            return Response(serializers.data)
        else:
            return Http404()

    # Hood admin permission
    def put(self, request, id, format=None):
        if request.user.is_staff == True:   
            hood = self.get_hood(id)
            if hood.admin == request.user:
                serializers = HoodSerializer(hood, request.data)
                if serializers.is_valid():
                    serializers.save()
                    return Response(serializers.data)
                else:
                    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('User does not have permission')
            return Http404()
    
    #Hood superuser permission
    def delete(self, request, id, format=None):
        if request.user.is_superuser == True:
            hood = self.get_hood(id)
            hood.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response('User does not have permission')
            return Http404()



#Profile
class ProfileCreateView(APIView):
    '''Class view to create a profile'''
    permission_classes = [IsAuthenticated]
    parser_classes = [FileUploadParser]

    def get(self, request, format=None):
        if request.user.is_superuser == True:
            all_profiles = Profile.objects.all()
            serializers = ProfileSerializer(all_profiles)
            return Response(serializers.data)
        else:
            return Http404()

    @staticmethod
    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serialiazers.data, status=status.HTTP_201_CREATED)
        return Response(serialiazers.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileDetailsView(APIView):
    '''Class view for a specific profile'''
    permission_classes = [IsAuthenticated]
    
    def get_profile(self,id):
        try:
            return Profile.objects.get(pk=id)
        except Profile.DoesNotExist:
            return Http404()

    def get(self, request, id, format=None):
        user = User.objects.get(id = id)
        if request.user == user:
            profile = get_profile(id)
            serializers = ProfileSerializer(profile)
            return Response(serializers.data)
        else:
            return Http404()

    def put(self, request, id, format=None):
        user = User.objects.get(id = id)
        if request.user == user:
            profile = get_profile(id)
            serializers = ProfileSerializer(profile, request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            else:
                return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Http404()



#Post
class PostListCreateView(APIView):
    '''Class view for the Post Class'''
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        all_posts = Post.objects.all()
        serializers = PostSerializer(all_posts)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


#Bussiness
class BussinessListCreateView(APIView):
    '''Class view for the Bussiness Class'''
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        all_bussinesses = Bussiness.objects.all()
        serializers = BussinessSerializer(all_bussinesses)
        return Response(serializers.data)

    def post(self, request, format=None):
        if request.user.is_staff == True & request.user.is_superuser == False:
            serializers = BussinessSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('User is not allowed')
            return Http404()



#EmergencyService
class EmergencyServiceListCreateView(APIView):
    '''Class view for the Emergency Service class'''
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        all_services = EmergencyService.objects.all()
        serializers = EmergencyServiceSerializer(all_services)
        return Response(serializers.data)

    def post(self, request, format=None):
        if request.user.is_staff == True & request.user.is_superuser == False:
            serializers = EmergencyServiceSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('User is not allowed')
            return Http404()