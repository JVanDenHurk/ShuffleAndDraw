from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage with all cards
    path('card/<int:card_id>/', views.card_detail, name='card_detail'),  # Card details page
]
