from django.shortcuts import render
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404

# Create your views here.
def main(request):
    
    path=request.GET["path"]
    
    return render(request, "remote/main.html", {"path" : path})
    
def launch(request):
    return HttpResponse("---")
    
def pause(request):
    return HttpResponse("---")
    
def play(request):
    return HttpResponse("---")
    
