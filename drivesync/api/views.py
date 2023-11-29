from django.shortcuts import render
from rest_framework import generics, status
from .serializers import UserSerializer, CreateUserSerializer
from models.user import User
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
#def main(request):
#    return HttpResponse("<h1>DriveSync<h1>")

class UserView(generics.ListAPIView): #or (List/Create)APIView lists json data no UI
    """View and create user objects"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateUserView(APIView):
    """Creates user view"""
    serializer_class = CreateUserSerializer

    def post(self, request, format=None):
        # creates session if not exists
        if not self.request.session.exist(self.request.session.session_key):
            self.request.session.create()

        # translates objects into python formatted data
        serilizer = self.serializer_class(data=request.data)
        if serilizer.is_valid():
            user_id = self.request.session.session_key #may give error cuz not inputted user field
            firstName = serilizer.data.get('firstName')
            lastName = serilizer.data.get('lasttName')
            email = serilizer.data.get('email')
            phone = serilizer.data.get('phone')
            #customer_id = serilizer.data.get('customer_id')
            queryset = User.objects.filter(user_id=user_id)
            
            if queryset.exists():
                user = queryset[0] #first instance of creating user var
                user.firstName = firstName
                user.lastName = lastName
                user.email = email
                user.phone = phone
                #user.customer_id = customer_id
                user.save(update_fields=['firstName', 'lastName', 'email', 'phone'])
                return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
            else:
                user = User(user_id=user_id, firstName=firstName, lastName=lastName, email=email, phone=phone)
                user.save()
                return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)   
