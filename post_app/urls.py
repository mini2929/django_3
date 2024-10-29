from django.urls import path
from .import views


# 순서3 - 브라우저에서 들어온 url 패턴을 확인해서 view.py
# 주소창에  localhost:8000/posts라는 요청이 들어오면 아래 url 턴이 인지해서 views.py 에 있는 posts함수 실행
urlpatterns = [
  path('posts', views.posts, name='posts'),
  path('posts/<slug:slug>/', views.posts_detail, name='post-detail')
]