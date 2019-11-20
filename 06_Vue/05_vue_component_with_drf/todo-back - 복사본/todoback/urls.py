from django.contrib import admin
from django.urls import path, include
# 유저네임 + 패스워드 + POST request -> token 줌
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_jwt_token),
    path('api/v1/', include('todos.urls')),
]
