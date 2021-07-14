from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="article", null=True)
    # User가 탈퇴했을 때, 게시글은 알 수 없음과 같은 창이 뜨게끔
    # User가 Article을 접근할 때 사용하는 이름이므로 article이라고 해줌

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)