from django.db.models import F
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.
def index(request):
    product = Product.objects.all()
    categorys = Category.objects.all()
    context = {
        'product': product,
        'categorys': categorys,
    }
    return render(request, template_name='market/base.html', context=context)

class ViewProduct(DetailView):
    model = Product
    template_name = 'market/views_product.html'
    context_object_name = 'product'

class CategoryView(ListView):
    template_name = 'market/category.html'
    context_object_name = 'product'
    allow_empty = False
    paginate_by = 9

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context




