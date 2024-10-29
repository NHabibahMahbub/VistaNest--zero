from .models import Platform
from django.shortcuts import render, redirect
from . import forms


def add_platform(request):
    if request.method == "POST":
        form = forms.PlatformForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = forms.PlatformForm()
    return render(request, 'forms.html', {
        "form": form
    })


def update_platform(request, p_id):
    p = Platform.objects.get(pk=p_id)
    if request.method == "POST":
        form = forms.PlatformForm(request.POST or None, request.FILES, instance=p )
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = forms.PlatformForm(instance=p)
    return render(request, 'forms.html', {
        "form": form
    })


def delete_platform(request, p_id):
    Platform.objects.get(pk=p_id).delete()
    return redirect("home")


from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Property, Favorite

@login_required
def add_to_favorites(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)
    Favorite.objects.get_or_create(user=request.user, property=property_obj)
    return redirect('property_detail', property_id=property_id)

@login_required
def remove_from_favorites(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)
    Favorite.objects.filter(user=request.user, property=property_obj).delete()
    return redirect('property_detail', property_id=property_id)

@login_required
def view_favorites(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'favorites.html', {'favorites': favorites})
