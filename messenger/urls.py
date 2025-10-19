from django.urls import path
from . import views

app_name = 'messenger'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('sent/', views.sent, name='sent'),
    path('compose/', views.compose, name='compose'),
    path('compose/<int:reply_to>/', views.compose, name='compose-reply'),
    path('<int:pk>/', views.message_detail, name='message-detail'),
    path('<int:pk>/delete/', views.delete_message, name='message-delete'),
]
