from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import moviesdata


# Create your views here.

def home(request):
    return render(request, 'moviesdata/home.html')

# def getmoviesdata(request):
#     return HttpResponseRedirect('http://www.omdbapi.com/?i=tt3896198&apikey=5ce9377d')

def getmoviesdata(request):

    if request.method == 'GET':
            title = request.GET["title"]
    else:
        return Response(data={"Error": "You must provide title in POST request with key named title"}, status=status.HTTP_400_BAD_REQUEST)

    my_api_key = '5ce9377d'
    url = f'http://www.omdbapi.com/?t={title}&type=movie&apikey={my_api_key}'
    return HttpResponseRedirect(url)

         
     





