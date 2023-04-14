from django.shortcuts import render, get_object_or_404
from .models import Review, Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    return render(request, 'itreporting/home.html')

def about(request):
    return render(request, 'itreporting/about.html', {'title': 'About Us'} )

def contact(request):
    return render(request, 'itreporting/contact.html', {'title': 'Contact Us'} )
  
def product(request):
    daily_report= {
        'reviews': Review.objects.all()
    }

    return render(request, 'itreporting/product.html', daily_report)

def product(request):
    daily_reports= {
        'products': Product.objects.all()
    }
    return render(request, 'itreporting/producttemplate.html', daily_reports)

def tablet(request):
    daily_reports= {
        'tablets': Product.objects.all()
    }
    return render(request, 'itreporting/tablet.html', daily_reports)

def smartphone(request):
    daily_reports= {
        'smartphones': Product.objects.all()
    }
    return render(request, 'itreporting/smartphone.html', daily_reports)

def smartTv(request):
    daily_reports= {
        'smartTvs': Product.objects.all()
    }
    return render(request, 'itreporting/smartTv.html', daily_reports)

class PostListView(ListView):
    model = Product
    template_name = 'itreporting/producttemplate.html'
    context_object_name = 'products'
    ordering = ['-date_released']
    paginate_by = 2
    
class PostDetailView(DetailView):
    model = Review


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = [ 'rating', 'details']
    def form_valid(self, form):
        form.instance.author_name = self.request.user
        form.instance.id2_id = self.request.GET.get('id2')  # set the id2 foreign key value
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Review
    fields = [  'rating','details']
    def test_func(self):
            review = self.get_object()
            if self.request.user == review.author_name:
                    return True
            return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    success_url = '/product'
    def test_func(self):
            review = self.get_object()
            if self.request.user == review.author_name:
                    return True
            return False
    
##

class PostListView2(ListView):
    model = Product
    template_name = 'itreporting/producttemplate.html'
    context_object_name = 'products'
    ordering = ['-date_submitted']

class PostListView3(ListView):
    model = Product
    template_name = 'itreporting/tablet.html'
    context_object_name = 'tablets'
    ordering = ['-date_submitted']

class PostListView4(ListView):
    model = Product
    template_name = 'itreporting/smartphone.html'
    context_object_name = 'smartphones'
    ordering = ['-date_submitted']

class PostListView5(ListView):
    model = Product
    template_name = 'itreporting/smartTV.html'
    context_object_name = 'smartTvs'
    ordering = ['-date_submitted']

class PostDetailView2(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
            reviews = Review.objects.filter(id2 = self.object).order_by('-date_reviewed')
            context = super(PostDetailView2, self).get_context_data(**kwargs)
            context.update({'title': 'List of Reviews', 'Reviews': reviews})
            return context
    
class PostCreateView2(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['prod_name', 'brand ', 'avg_cost', 'category', 'date_released', 'description', 'image']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView2(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Product
    fields = ['prod_name', 'brand ', 'avg_cost', 'category', 'date_released', 'description', 'image']
    def test_func(self):
            review = self.get_object()
            if self.request.user == review.prod_name:
                    return True
            return False
    
class PostDeleteView2(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/report'
    def test_func(self):
            review = self.get_object()
            if self.request.user == review.prod_name:
                    return True
            return False


