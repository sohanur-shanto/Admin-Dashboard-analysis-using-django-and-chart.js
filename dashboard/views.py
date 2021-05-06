from django.shortcuts import render, redirect
from .models import CountryData
from .forms import CountryDataFrom

def index(request):

    data = CountryData.objects.all()
    if request.method == 'POST':
        form = CountryDataFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CountryDataFrom()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'dashboard/index.html', context)