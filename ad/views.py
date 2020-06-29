from django.shortcuts import render
from .forms import AdForm


# Create your views here.




def all_ads(request):
    pass



def all_categories(request):
    pass



def category_ads(request , id):
    pass


def add_ad(request):
    if request.method == 'POST': #save
        form = AdForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()


    else:
        form =AdForm()    

    return render(request, 'ad/post-ad.html',{'form':form})