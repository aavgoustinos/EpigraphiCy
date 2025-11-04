from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import *



def base(request):
    return render(request, 'core/base.html',)

# HomePage
def homepage(request):
    monuments = Monument.objects.all()
    context = {
        'monuments': monuments
    }
    return render(request, 'core/index.html', context)

# Monument detail single monument with all epigraphy
def monument_detail(request, monument_id):
    monument = get_object_or_404(Monument, id=monument_id)
    iconographic_elements = IconographicElement.objects.all()
    epigraphy = monument.epigraphy_set.all()
    epigraphy_count = monument.epigraphy_set.count()
  

    context = {
        'monument': monument,
        'epigraphy': epigraphy,
        'iconographic_elements':iconographic_elements,
        'epigraphy_count':epigraphy_count,
        
    }
  
    return render(request, 'monument/monument_detail.html', context)

# List of all monuments 
def monument_list(request):
    monuments = Monument.objects.all()
    context = {
        'monuments': monuments
    }
    return render(request, 'monument/monument_list.html', context)


# epigraphy_detail

def epigraphy_detail(request, epigraphy_id):
    epigraphy = get_object_or_404(Epigraphy, pk=epigraphy_id)
    return render(request, 'epigraphy/epigraphy_detail.html', {'epigraphy': epigraphy})

# about page

def about_view(request):
    return render(request, 'about.html')
    
    
# Team page

def team_view(request):
    return render(request, 'team.html')
    
# Platform page

def platform_view(request):
    return render(request, 'platform.html')

