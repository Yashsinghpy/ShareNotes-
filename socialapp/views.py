from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import reg,notes,shared
from .forms import RegForm,LoginForm,NotesForm
# Create your views here.

def registration(request):
          if request.method=="POST":
                    form=RegForm(request.POST)
                    if form .is_valid():
                              username=form.cleaned_data['name']
                              password=form.cleaned_data['password']
                              try:
                                       user= User.objects.get(username=username)
                                       return render(request, 'registration.html', {'form':form,'error_message':'username already  exists'})
                              except User.DoesNotExist:
                                        user=User.objects.create_user(username=username,password=password)
                                        obj=reg.objects.create(**form.cleaned_data)
                                        return redirect('login')
                    else:
                              form=RegForm()
          else:
                    form = RegForm()
                    
          return render(request, 'registration.html', {'form':form})

def note(request):
          if request.method=="POST":
                    form=NotesForm(request.POST)
                    if form .is_valid():
                               dataa=form.cleaned_data['contents']
                               obj=notes.objects.create(contents=dataa,user=request.user)
                               return redirect('home')
                    else:
                              form=NotesForm()
          else:
                    form = NotesForm()
                    
          return render(request, 'add.html', {'form':form})

def login(request):
          if request.method=="POST":
                    form=LoginForm(request.POST)
                    if form .is_valid():
                              username=form.cleaned_data['name']
                              password=form.cleaned_data['password']
                              user=auth.authenticate(username=username,password=password)
                              if user is not None:
                                            auth.login(request,user)
                                            return redirect('home')
                              else:
                                  return render(request, 'login.html', {'form':form ,'error_message':'invalid'})
                    else:
                              form=LoginForm()
          else:
                    form = LoginForm()
                    
          return render(request, 'login.html', {'form':form})

def home(request):
          log_user=request.user
          data=reg.objects.all()
          datas=notes.objects.filter(user=log_user)
          return render(request, 'show.html', {'datas':datas,'data':data})

def edit(request ,id):
         data=notes.objects.get(id=id)
         if request.method=="POST":
                   form=NotesForm(request.POST)
                   if form .is_valid():
                             datas=form.cleaned_data['contents']
                             data.contents=datas
                             data.save()
                             return redirect('home')
                   else:
                             form=NotesForm()
         else:
                   form = NotesForm()
         return render(request, 'edit.html', {'form':form})
          
def  delete(request ,id):
         data=notes.objects.get(id=id)
         data.delete()
         return redirect('home')

def share(request,id,name):
           a=notes.objects.get(id=id)
           b=reg.objects.get(name=name)
           contents=a.contents
           name=b.name
           user=a.user
           data=shared.objects.create(contents=contents,recevier=name,sender=user)
           return redirect('home')
  
          


def check(request):
          log_user=request.user
          datas=shared.objects.filter(recevier=log_user)
          return render(request, 'share.html', {'datas':datas,})
          
          

          
          
          
                    
