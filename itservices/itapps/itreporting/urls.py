from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.urls import reverse
urlpatterns =[
path('', views.home, name='itreporting-home'),
path('about/', views.about, name='itreporting-about'),
path('contact/', views.contact, name='itreporting-contact'),
path('product/', views.product, name='itreporting-product'),
path('product/', PostListView.as_view(), name='itreporting-product'),
path('issue/<int:pk>', PostDetailView.as_view(), name='issue-detail'),
path('issue/new/', PostCreateView.as_view(), name='issue-create'),
path('issue/<int:pk>/update/', PostUpdateView.as_view(), name='issue-update'),
path('issue/<int:pk>/delete/', PostDeleteView.as_view(), name='issue-delete'),

]