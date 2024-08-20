from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import AppUser

@api_view(['POST'])
def regster_user(request):
    if request.method == 'POST':
        
        print(request.data)
        print('Register User End point')


        email = request.data.get('email')
        password = request.data.get('password')
        first_name = request.data.get('fname')
        last_name = request.data.get('lname')

        if AppUser.objects.filter(email=email).exists():
            msg= 'User Already Exist'
            print(msg)

            res= Response(data=msg,status=status.HTTP_400_BAD_REQUEST)

        else:
            new_user = AppUser(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password  )
        
            new_user.save()

            msg= 'User Registered'
            print(msg)
        
            res = Response(data=msg,status=status.HTTP_201_CREATED)

    return res








@api_view(['POST'])
def login_user(request):
    
    email = request.data.get('email')
    password = request.data.get('password')
    #User exists
    if AppUser.objects.filter(email=email, password=password).exists():

        return Response("LoggedIn",status=status.HTTP_200_OK)
    else:
        return Response("Bad Credentials ",status=status.HTTP_400_BAD_REQUEST)
    


