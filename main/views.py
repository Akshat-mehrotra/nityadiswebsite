from django.shortcuts import render

import os

from .models import Art, Commission
from .forms import Art_get_form, Upload_art_form


recent_art = Art.objects.all().order_by('-id')[:3]

# Create your views here.
def getit(request, pk):
    if request.method == 'GET':

        form = Art_get_form()
        return render(request, 'main/getit.html', {'form':form, 'recent_art':recent_art})

    elif request.method == 'POST':
        form = Art_get_form(request.POST, request.FILES)
        art_piece = Art.objects.get(pk=pk)

        if form.is_valid():
            # form.save(commit=False)
            # form.art = art_piece
            # form.save()

            new = Commission(
            name=form.cleaned_data['name'],
            address=form.cleaned_data['address'],
            art=art_piece,
            size=form.cleaned_data['size'],
            details=form.cleaned_data['details'],
            phone_number=form.cleaned_data['phone_number'],
            email=form.cleaned_data['email'],
            attachment=form.cleaned_data['attachment']
            )
            new.save()

            last_ten = Art.objects.all().order_by('-id')[:10]
            return render(request, "main/index.html", {"art":last_ten, 'Recent_art':recent_art})

def art(request):
    art_work = Art.objects.all()

    return render(request, "main/portfolio.html", {'art':art_work, 'Recent_art':recent_art})

def about(request):
    return render(request, 'main/about.html', {'Recent_art':recent_art})

def buy(request, pk):
    art_piece = Art.objects.get(pk=pk)
    if request.method == 'GET':
        form = Art_get_form()
        arts = []

        if art_piece.picture2:
            arts.append(art_piece.picture2)
            if art_piece.picture3:
                arts.append(art_piece.picture3)
                if art_piece.picture4 :
                    arts.append(art_piece.picture4)

        return render(request, 'main/portfolio-single.html', {'form':form,"arts":arts, "art":art_piece, 'Recent_art':recent_art})

    elif request.method == 'POST':
        form = Art_get_form(request.POST, request.FILES)
        if form.is_valid():

            new = Commission(
            name=form.cleaned_data['name'],
            address=form.cleaned_data['address'],
            art=art_piece,
            size=form.cleaned_data['size'],
            details=form.cleaned_data['details'],
            phone_number=form.cleaned_data['phone_number'],
            email=form.cleaned_data['email'],
            attachment=form.cleaned_data['attachment']
            )

            new.save()
            last_ten = Art.objects.all().order_by('-id')[:10]
            return render(request, "main/index.html", {"art":last_ten, 'Recent_art':recent_art, 'message':'Your request has been recived'})

    form = Art_get_form()

    return render(request, "main/portfolio-single.html", {'form':form, "art":art_piece, 'Recent_art':recent_art})

def home(request):
    last_ten = Art.objects.all().order_by('-id')[:10]
    return render(request, "main/index.html", {"art":last_ten, 'Recent_art':recent_art})
