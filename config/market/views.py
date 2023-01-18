from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    product = Product.objects.all()
    category = Category.objects.all()

    context = {
        'product': product,
        'category': category,
    }
    return render(request, template_name='market/base.html', context=context)