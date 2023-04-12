from django.shortcuts import render, get_object_or_404
from .models import Issue, Electronic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
def home(request):
    return render(request, 'itreporting/home.html')

def about(request):
    return render(request, 'itreporting/about.html', {'title': 'About Us'} )

def contact(request):
    return render(request, 'itreporting/contact.html', {'title': 'Contact Us'} )

def product(request):
    daily_report= {
        'issues': Issue.objects.all()
    }

    return render(request, 'itreporting/product.html', daily_report)

def electronic(request):
    daily_reports= {
        'electronics': Electronic.objects.all()
    }
    return render(request, 'itreporting/electronictemplate.html', daily_reports)

def tablet(request):
    daily_reports= {
        'tablets': Electronic.objects.all()
    }
    return render(request, 'itreporting/tablet.html', daily_reports)

def smartphone(request):
    daily_reports= {
        'smartphones': Electronic.objects.all()
    }
    return render(request, 'itreporting/smartphone.html', daily_reports)

def smartTv(request):
    daily_reports= {
        'smartTvs': Electronic.objects.all()
    }
    return render(request, 'itreporting/smartTv.html', daily_reports)

class PostListView(ListView):
    model = Issue
    template_name = 'itreporting/product.html'
    context_object_name = 'issues'
    ordering = ['-date_submitted']
    paginate_by = 5
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issues = self.get_queryset()
        paginator = Paginator(issues, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['issues'] = issues
        return context
class PostDetailView(DetailView):
    model = Issue


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    fields = [ 'rating', 'details']
    def form_valid(self, form):
        form.instance.author_name = self.request.user
        form.instance.id2_id = self.request.GET.get('id2')  # set the id2 foreign key value
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Issue
    fields = [  'rating','details']
    def test_func(self):
            issue = self.get_object()
            if self.request.user == issue.author_name:
                    return True
            return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Issue
    success_url = '/electronic'
    def test_func(self):
            issue = self.get_object()
            if self.request.user == issue.author_name:
                    return True
            return False
    
##

class PostListView2(ListView):
    model = Electronic
    template_name = 'itreporting/electronictemplate.html'
    context_object_name = 'electronics'
    ordering = ['-date_submitted']

class PostListView3(ListView):
    model = Electronic
    template_name = 'itreporting/tablet.html'
    context_object_name = 'tablets'
    ordering = ['-date_submitted']

class PostListView4(ListView):
    model = Electronic
    template_name = 'itreporting/smartphone.html'
    context_object_name = 'smartphones'
    ordering = ['-date_submitted']

class PostListView5(ListView):
    model = Electronic
    template_name = 'itreporting/smartTV.html'
    context_object_name = 'smartTvs'
    ordering = ['-date_submitted']

class PostDetailView2(DetailView):
    model = Electronic
    
    def get_context_data(self, **kwargs):
            reviews = Issue.objects.filter(id2 = self.object).order_by('-date_reviewed')
            context = super(PostDetailView2, self).get_context_data(**kwargs)
            context.update({'title': 'List of Issues', 'Reviews': reviews})
            return context

class PostCreateView2(LoginRequiredMixin, CreateView):
    model = Electronic
    fields = ['prod_name', 'brand ', 'avg_cost', 'category', 'date_released', 'description', 'image']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView2(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Electronic
    fields = ['prod_name', 'brand ', 'avg_cost', 'category', 'date_released', 'description', 'image']
    def test_func(self):
            issue = self.get_object()
            if self.request.user == issue.prod_name:
                    return True
            return False
    
class PostDeleteView2(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Electronic
    success_url = '/report'
    def test_func(self):
            issue = self.get_object()
            if self.request.user == issue.prod_name:
                    return True
            return False


