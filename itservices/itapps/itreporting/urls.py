from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostListView2, PostDetailView2, PostCreateView2, PostUpdateView2, PostDeleteView2, PostListView3, PostListView4
from django.urls import reverse
urlpatterns =[
path('', views.home, name='itreporting-home'),
path('about/', views.about, name='itreporting-about'),
path('contact/', views.contact, name='itreporting-contact'),
path('review/<int:pk>', PostDetailView.as_view(), name='review-detail'),
path('review/new/', PostCreateView.as_view(), name='review-create'),
path('review/<int:pk>/update/', PostUpdateView.as_view(), name='review-update'),
path('review/<int:pk>/delete/', PostDeleteView.as_view(), name='review-delete'),
##
path('product/', PostListView.as_view(), name='itreporting-producttemplate'),
path('category/tablet/', views.tablet, name='itreporting-tablet'),
path('category/smartphone/', views.smartphone, name='itreporting-smartphone'),
path('category/smartTv/', views.smartTv, name='itreporting-smartTv'),
path('product/<int:pk>', PostDetailView2.as_view(), name='product-detail'),

]