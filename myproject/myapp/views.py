from django.shortcuts import render, redirect

from.models import MovieInfo
from.forms import MovieForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login/')
def list(request):
    recent_visits=request.session.get('recent_visits',[])
    count=request.session.get('count',0)
    count=int(count)
    count=count+1
    request.session['count']=count
    recent_movie_set=MovieInfo.objects.filter(pk__in=recent_visits)
    movie_set=MovieInfo.objects.all()
    print(movie_set)
    response=render(request,"list.html", {'recent_movies':recent_movie_set,'movies':movie_set,'visits':count})

    return response
@login_required(login_url='login/')
def create(request):
    frm=MovieForm()
    if request.POST:
        frm=MovieForm(request.POST,request.FILES)

        if frm.is_valid():
            frm.save()

        else:
            frm=MovieForm()
    return render(request,'create.html',{'frm':frm})
@login_required(login_url='login/')
def edit(request,pk):

    instance_to_be_edited = MovieInfo.objects.get(pk=pk)
    if request.POST:
        frm=MovieForm(request.POST,instance=instance_to_be_edited)
        if frm.is_valid():
            instance_to_be_edited.save()
    else:
        recent_visits=request.session.get('recent_visits',[])
        recent_visits.insert(0,pk)
        request.session['recent_visits']=recent_visits
        frm=MovieForm(instance=instance_to_be_edited)


    return render(request,'create.html',{'frm':frm})
@login_required(login_url='login/')
def delete(request,pk):
    instance=MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_set=MovieInfo.objects.all()
    return render (request,"list.html", {'movies':movie_set})