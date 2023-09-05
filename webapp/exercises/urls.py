from django.urls import path
from . import views

urlpatterns = [
    path('roadmap/', views.roadmap_page, name='roadmap-page'),
    path('exercises/', views.get_exercise, name='get_exercise'),
    path('get_random_exercise/', views.get_random_exercise, name='get_random_exercise'),
    path('get_hint_from_chatgpt/', views.get_hint_from_chatgpt, name='get_hint_from_chatgpt'),
]
