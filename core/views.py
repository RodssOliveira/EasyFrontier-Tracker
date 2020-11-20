from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from core.models import Tracker
# Create your views here.


@csrf_exempt
def control(request):
    tracker = Tracker.objects.all()
    return render(request, 'control.html', {'tracker':tracker})


@csrf_exempt
def edit_policial(request):
    if 'id' in request.GET:
        id = request.GET.get('id')
        tracker = Tracker.objects.get(id=id)
    else:
        tracker = None

    dic = {'tracker': tracker}
    return render(request, 'edit.html', dic)

@csrf_exempt
def save_policial(request):
    pass

