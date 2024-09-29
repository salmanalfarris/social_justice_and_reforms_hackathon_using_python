from django.shortcuts import render
from .models import LegalArticle
# Create your views here.

def home(request):
    articles = LegalArticle.objects.all()
    return render(request, 'legal_info/home.html', {'articles': articles})