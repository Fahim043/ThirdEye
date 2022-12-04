from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
# Create your views here.
def Events(request):
    item_l= Item.objects.all()
    context={
        'item_l': item_l,    
    }
    return render(request, "Event/index.html",context)

class EventsClassView(ListView):
    model = Item;
    template_name= "Event/index.html"
    context_object_name = "item_l" 


def Itemm(request):
    return HttpResponse("<h1>Nawla<h1>")

def detail(request,item_id):
    It=Item.objects.get(pk=item_id)
    context={
        'It':It,
        
    }
    return render (request,'Event/detail.html',context)

class FoodDetail(DetailView):
    model = Item
    template_name = 'Event/detail.html'

def create_item(request):
    form = ItemForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('Events:Events')
    return render(request,'Event/item-form.html',{'form':form})

#this is a class based view for create item
class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc','item_price', 'item_image']
    template_name = 'Event/item-form.html'
    
    def form_valid(self, form):
        form.instance.user_name = self.request.user
        
        return super().form_valid(form)



def update_item(request,id):
    item= Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('Events:Events')
    return render(request,'Event/item-form.html',{'form':form, 'item':item})


