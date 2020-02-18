from django.shortcuts import render
from .forms import ContactForm
from towers.forms import SearchForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Products
from .models import Images


############################################################# INDEX VIEWS ############################################
def index(request):
    products = Products.objects.filter(images__manufacturer="ndt")

    context = {
        'products': products,
    }
    

    return render(request, "pages/index.html", context)
############################################################# ABOUT VIEWS ############################################
def about(request):
    return render(request, "pages/about.html")

############################################################# CONTACT VIEWS ############################################
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            form = ContactForm()
            messages.success(request, 'Thanks!! Someone will contact you soon')
            return HttpResponseRedirect(reverse('contact'))

    else:
        form = ContactForm()

    context = {
        'form': form,
    } 
    return render(request, 'pages/contact.html', context)


############################################################# ACCESSORIES VIEWS ############################################
def accessories(request):

    products = Products.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'pages/accessories.html', context)


def accessory(request, query):


    products = Products.objects.filter(category=query)

    context = {
        'products': products
    }
    
    return render(request, 'pages/accessories.html', context)

############################################################# BIMINIS VIEWS ############################################
def biminis(request):

    form = SearchForm()

    context = {
        'form': form
    }
    
    return render(request, 'pages/biminis.html', context)

############################################################# INSTALLATION VIEWS ############################################
def installation(request):
    return render(request, 'pages/installation.html')

############################################################# FAQ VIEWS ############################################
def faq(request):
    return render(request, 'pages/faq.html')

    

############################################################# FAQ VIEWS ############################################
def sitemap(request):
    return render(request, 'pages/sitemap.html')


############################################################# FAQ VIEWS ############################################
def orders(request):
    return render(request, 'pages/orders.html')


######################################################## product views #########################################
def product(request):
    return render(request, 'pages/product.html')