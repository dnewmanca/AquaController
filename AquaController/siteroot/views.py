from django.shortcuts import render
from siteroot.models import MenuItem
from django.core.urlresolvers import reverse

def getMenu():
    return [
        MenuItem(Href=reverse('siteroot:home') , Text='Home'), 
        MenuItem(Href=reverse('admin:index') , Text='Admin'), 
        ]

def index(request):
    menu = getMenu()
    menu[0].CssClass = 'selected'

    content = 'Hello, world!'

    context = {'menu':menu, 'content':content}

    return render(request, 'siteroot/index.html', context)