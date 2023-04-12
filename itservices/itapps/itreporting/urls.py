from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostListView2, PostDetailView2, PostCreateView2, PostUpdateView2, PostDeleteView2, PostListView3, PostListView4
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
##
path('electronic/', views.electronic, name='itreporting-electronictemplate'),
path('tablet/', views.tablet, name='itreporting-tablet'),
path('smartphone/', views.smartphone, name='itreporting-smartphone'),
path('smartTv/', views.smartTv, name='itreporting-smartTv'),
path('electronic/<int:pk>', PostDetailView2.as_view(), name='electronic-detail'),
]