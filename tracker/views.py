from django.shortcuts import render,redirect
from django.views import View
# Create your views here.
from .forms import CarForm,SettingsForm
from django.http import HttpResponse
from .models import CarModel,Podesavanja
import allthreads3

class PodesavanjaVju(View):
    def get(self, request):
        form = SettingsForm
        return render(request, 'settings.html', {'form' : form})
    def post(self, request):
        form = SettingsForm(request.POST)
        if form.is_valid():
            proxylist = request.POST.get('proxylist')
            print(proxylist)
            status = request.POST.get('status')
            #proxylist = 
            o = Podesavanja.objects.get(id=1)
            o.status = status 
            o.proxylist = proxylist
            o.save()
            return redirect('/settings/')

class IndexView(View):
    
    
    def get(self, request):
        form = CarForm()
        o = Podesavanja.objects.get(id=1)
        if(o.status=='Stop'):
            status = 'Stopped'
        else:
            status = 'Operational'
        cars = CarModel.objects.all()
        
        return render(request, 'index.html', {'form': form, 'list' : cars, 'status' : status})

    def post(self, request):
        form = CarForm(request.POST)
        o = Podesavanja.objects.get(id=1)
        if(o.status=='Stop'):
            status = 'Stopped'
        else:
            status = 'Operational'
        cars = CarModel.objects.all()
        if form.is_valid():
            #form.save()
            #print(request.POST)
            print(request.POST)
            ime = (request.POST.get('name'))
            print(ime)
            link = (request.POST.get('link'))
            states = (request.POST.getlist('states'))
            print(states)
            allthreads3.main(states,link,ime)
            return redirect('/')
        else:
            form = CarForm()
        return render(request, 'index.html', {'form': form, 'list' : cars, 'status' : status })

class Remove(View):
    #Post = Post.objects.all()
    def get(self,request,format=None):
        idc = (int(request.GET.get('carid')))
        b = CarModel.objects.get(id=idc)
        b.delete()
        return redirect('/')
class Edit(View):
    def get(self,request,format=None):
        form = CarForm()
        idc = (int(request.GET.get('carid')))
        b = CarModel.objects.get(id=idc)
        print(b.link)
        return render(request, 'edit.html', {'form': form, 'car' : b})
    def post(self,request):
        form = CarForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            idc = (int(request.GET.get('carid')))
            print("ID: ", idc)
            #print("FORM: ", form)
            #print("POST: ", request.POST)
            #print(request.POST)
            ime = (request.POST.get('name'))
            link = (request.POST.get('link'))
            states = (request.POST.getlist('states'))
            p = CarModel.objects.get(id=idc)
            p.link = link
            p.states = states
            p.cities = ''
            p.save()
            allthreads3.main(states,link,ime)
            return redirect('/')
        else:
            form = CarForm()
        return render(request, 'index.html', {'form': form})
