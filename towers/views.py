from django.shortcuts import render
from .models import Towers, Images
from .forms import SearchForm

# Create your views here.
################################# From index page no link parameter ############# Load all towers
def index(request):

    has_id = False
    

    form = SearchForm()
    if request.method == "POST":
        selection = request.POST.get('tower_id')
        towers = Towers.objects.filter(manufacturer=selection)
        main = Images.objects.filter(manufacturer=selection, orientation='main')
        has_id = True

        
    else:
        towers = Towers.objects.all()
        main = Images.objects.filter(orientation='main')

    

    context = {
        'towers': towers,
        'form': form,
        'main_img': main,
        'has_id': has_id,
    }

    return render(request, 'towers/towers.html', context)




#################################################### Render from Index manufacturer selection passes tower_id to method
def tower(request, tower_id):

    form = SearchForm()

    towers = Towers.objects.filter(manufacturer=tower_id)

    main = Images.objects.filter(manufacturer=tower_id, orientation='main')
    get_id = True

    if tower_id == '':
        get_id = False

    context = {
        'towers': towers,
        'form': form,
        'main_img': main,
        'id': tower_id,
        'get_id': get_id,
    }
    

    return render(request, 'towers/towers.html', context)
