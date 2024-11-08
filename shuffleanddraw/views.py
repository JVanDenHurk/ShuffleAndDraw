from django.shortcuts import render
from .models import Card

def home(request):
    cards = Card.objects.all()
    return render(request, 'shuffleanddraw/home.html', {'cards': cards})

def card_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    return render(request, 'shuffleanddraw/card_detail.html', {'card': card})
