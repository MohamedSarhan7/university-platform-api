
# Create your views here.
from .models import NewUser
from .serializers import UserSerializer
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class CustomAuthToken(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        if serializer.is_valid():
    
            user = serializer.validated_data['user']
        
            token ,  created = Token.objects.get_or_create(user=user)
            # user.user_type = serializers.StringRelatedField(read_only=True)
        
            return Response({
            'status':'true',
            'token': token.key,
            'user_type': user.user_type,
            'email': user.email,
            'username':user.username,
            'fullname':user.fullname,
            
            'image':user.image.url,
            'about':user.about,
            'gender':user.gender,
            'date_of_birth':user.date_of_birth,
                })
        else:
            return Response({
                 'status':'false',
                 'msg': "Unable to log in with provided credentials."
            })    

class UserDetailApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated, )

    def get(self,request):
        user = self.request.user
        user = NewUser.objects.get(pk=user.pk)
        
        serializer = UserSerializer(user)

        return Response( {
                'status':"true",
                'msg':"success",
                'data': serializer.data,
                    })
    
    def put(self,request):
        
        user = NewUser.objects.get(pk=self.request.user.pk)
        serializer=UserSerializer(user,data=self.request.data)
        if serializer.is_valid():
           
           
            serializer.save()
            
            return Response( {
                'status':"true",
                'msg':"success",
                'data': serializer.data,
                    })
        return  Response( {
                'status':"false",
                'msg':"err",
                'data': serializer.data,
                    })   





@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        
        
        
        