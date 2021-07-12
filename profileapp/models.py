from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    #User 객체가 삭제된다면, 연결되어 있는 Profile 객체도 사라지게(CASCADE)

    image = models.ImageField(upload_to='profile/', null= True)
    #이미지가 업로드 된다면, media/profile/ 경로에 업로드 됨
    #꼭 이미지 사진을 업로드 안해도 됨

    nickname = models.CharField(max_length=20, unique=True, null=True)
    #Profile 객체 안에서 nickname은 유일해야 함

    message = models.CharField(max_length=100, null=True)