from django.shortcuts import render
from .models import Towers, Images
from .forms import SearchForm

# Create your views here.
################################# From index page no link parameter ############# Load all towers
def index(request):


    # width = window.screen.width

    # if width > 768:


    has_id = False
    

    form = SearchForm()
    if request.method == "POST":
        selection = request.POST.get('tower_id')
        towers = Towers.objects.filter(manufacturer=selection)
        main = Images.objects.filter(manufacturer=selection, orientation='main')
        has_id = True
        # angled = Images.objects.filter(manufacturer=selection, orientation='angled')
        # back = Images.objects.filter(manufacturer=selection, orientation='back')
        # collapsed = Images.objects.filter(manufacturer=selection, orientation='collapsed')
        
    else:
        towers = Towers.objects.all()
        main = Images.objects.filter(orientation='main')
        # angled = Images.objects.filter(orientation='angled')
        # back = Images.objects.filter(orientation='back')
        # collapsed = Images.objects.filter(orientation='collapsed')
    

    context = {
        'towers': towers,
        'form': form,
        'main_img': main,
        'has_id': has_id,
        # 'width': width,
        # 'ang_img': angled,
        # 'back_img': back,
        # 'coll_img': collapsed,
    }

    return render(request, 'towers/towers.html', context)




#################################################### Render from Index manufacturer selection passes tower_id to method
def tower(request, tower_id):

    form = SearchForm()

    towers = Towers.objects.filter(manufacturer=tower_id)

    main = Images.objects.filter(manufacturer=tower_id, orientation='main')
    # angled = Images.objects.filter(manufacturer=tower_id, orientation='angled')
    # back = Images.objects.filter(manufacturer=tower_id, orientation='back')
    # collapsed = Images.objects.filter(manufacturer=tower_id, orientation='back')


    context = {
        'towers': towers,
        'form': form,
        'main_img': main,
        # 'ang_img': angled,
        # 'back_img': back,
        # 'coll_img': collapsed,
    }

    return render(request, 'towers/towers.html', context)
