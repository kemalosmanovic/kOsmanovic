from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'itreporting/home.html')

def about(request):
    return render(request, 'itreporting/about.html', {'title': 'About Us'} )

def contact(request):
    return render(request, 'itreporting/contact.html', {'title': 'Contact Us'} )

def product(request):
    return render(request, 'itreporting/product.html', {'title': 'Products'} )