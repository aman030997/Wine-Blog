from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Table1
from .forms import PostForm
from django.contrib import messages
from django.db.models import Q,F
# Create your views here.
def wine_list(request):
    wines_list=Table1.objects.all()
    paginator = Paginator(wines_list, 20)
    page = request.GET.get('page')
    try:
        wines = paginator.page(page)
    except PageNotAnInteger:
        wines = paginator.page(1)
    except EmptyPage:
        wines = paginator.page(paginator.num_pages)
    return render(request, 'Wine/wine_list.html', {'wines':wines})
def wine_detail(request,pk):
    wines=get_object_or_404(Table1,pk=pk)
    return render(request, 'Wine/wine_detail.html', {'wines': wines})
def wine_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('wine_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'Wine/wine_add.html', {'form': form})


"""def search(request):
    list = Table1.objects.all()
    filter = UserFilter(request.GET, queryset=list)
    return render(request, 'wine/search.html', {'filter': filter})

def Search(request):
    if request.method=='POST':
        srch=request.POST['srh']

        if srch:
            match=Table1.objects.filter(Q(winery__istartswith=srch))
            if match:
                return render(request,'Wine/search.html',{'sr':match})
            else:
                messages.error(request,'No result Found')
        else:
            return redirect('Search')
    return render(request,'Wine/search.html')"""
