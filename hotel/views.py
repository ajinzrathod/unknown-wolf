from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.


def hotel_image_view(request):

    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            new_article = Hotel.objects.create(
                user_id=User.objects.get(pk=request.user.id),
                hotel_Main_Img=form.cleaned_data["hotel_Main_Img"],
            )
            # thought = form.save(commit=False)
            # print(request.user)
            # thought.user = User.objects.get(pk=request.user.id)
            new_article.save()
            print("==============ashdkjsahdkjh==================")
            return redirect('success')
    else:
        form = HotelForm()
    return render(request, 'hotel_image_form.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')
