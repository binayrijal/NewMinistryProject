from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.encoding import smart_str,force_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .utils import Util
from .models import Course,Video
from .models import Timer
from django.utils.html import escape

User=get_user_model()




class RegisterModelSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model= User
        fields=['email','name','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }


    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.pop('password2')
        if password != password2:
           raise serializers.ValidationError('password and password2  need to match') 
        return attrs
    
    def create(self, validate_data):

        return User.objects.create_user(**validate_data)
    
class LoginModelSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model= User
        fields= ['email','password']



class ProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=['id','email','name']


    
class PasswordChangeSerializer(serializers.Serializer):
    password=serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True)
    password2=serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True)
    class Meta:
        fields=['password','password2']
    

    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        user=self.context.get('user')
        if password!=password2:
            raise serializers.ValidationError('password and password2 must match for change password')
        user.set_password(password) 
        user.save()  
        return attrs
    
class SendMailPasswordResetSerializer(serializers.Serializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        fields=['email']

    def validate(self, attrs):
        email=attrs.get('email')
        if User.objects.filter(email=email).exists():
            user=User.objects.get(email=email)
            uid=urlsafe_base64_encode(force_bytes(user.id))
            print('UID',uid)
            token=PasswordResetTokenGenerator().make_token(user)
            print('Password Reset token',token)
            link='http://localhost:8080/password-reset/'+uid+'/'+token
            print('Reset password Send Mail  Link',link)
            link = escape(link)
            body = f'Click the following link to reset your password: {link}'
            # reset_url = reverse('password-reset', kwargs={'uid': uid, 'token': token})
            # link = self.context['request'].build_absolute_uri(reset_url)
            # body = f'Click the following link to reset your password: <a href="{link}">Reset Password</a>'
            #mail send 
            data={
                'subject':'This email is send for reset password',
                'body':body,
                'to_email':user.email
            }
            Util.send_mail(data)
        else:
            raise serializers.ValidationError('user doesnot exist with that email')

        return attrs
    

class DoPasswordResetSerializer(serializers.Serializer):
    password=serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True)
    password2=serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True)
    class Meta:
        fields=['password','password2']
    

    def validate(self, attrs):
        try:
         password=attrs.get('password')
         password2=attrs.get('password2')
         uid=self.context.get('uid')
         token=self.context.get('token')
         if password!=password2:
             raise serializers.ValidationError('password and password2 must match for change password')
         id=smart_str(urlsafe_base64_decode(uid))
         user=User.objects.get(id=id)
         if not PasswordResetTokenGenerator().check_token(user,token):
             raise serializers.ValidationError('token is expird or invalid token')

         user.set_password(password) 
         user.save()   
         return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user,token)
            raise serializers.ValidationError('token is expired or invalid token')
        
        
        


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id','title', 'video_file']

class CourseSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id','title', 'category', 'classnumber', 'videos']
        
class TimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timer
        fields = ['user', 'time']