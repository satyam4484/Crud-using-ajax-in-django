from django.forms import models
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .forms import postform
from .models import post
import json

# Create your views here.

# homepage 
def home(request):
    form = postform()
    data = post.objects.values()
    context={
        'form':form,
        'data':data,
    }
    return render(request,'home.html',context)

# update and save data using the id 
def savedata(request):
    if request.method == 'POST':
        form = postform(request.POST)
        if form.is_valid():
            sid=request.POST.get("sid")
            name = request.POST['name']
            email = request.POST['email']
            passw = request.POST['password']

            # if id is none then create new user 
            if(sid ==''):
                pt=post(name=name,email=email,password = passw)
            # else update the user 
            else :
                pt=post(id=sid,name=name,email=email,password = passw)
            pt.save()


            data = post.objects.values()  # list of json data 
            data = list(data)

            # return json reponse to json 
            return JsonResponse({'status':'Save','data':data})
        else :
            return JsonResponse({'status':0})
    else :
        form = postform()
    
    return HttpResponse("saved")


# delete post 
def deletedata(request):
    if request.method=="POST":
        id=request.POST.get('sid')   # get id of the post from the ajax 
        # fetch the data and delete 
        data = post.objects.get(pk=id)
        data.delete()
        return JsonResponse({"status":1})


# fetch the data from model and send to ajax to display it in the form 
def editdata(request):
    if request.method == "POST":
        id = request.POST.get("sid")  
        stud =post.objects.get(pk=id)
        data = {
            'id':stud.id,
            'name':stud.name,
            'email':stud.email,
            'password':stud.password
        }

        return JsonResponse({"status":1,"data":data})
    return JsonResponse({'status':0})
