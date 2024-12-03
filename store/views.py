from django.shortcuts import render,redirect
from .models import NationalPark,Trail
from .forms import NationalParkForm,TrailForm
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views import View
# Create your views here.
def dashboard_view(request):
    return render(request, 'dashboard.html')
  
  
def create_park_view(request):
    if request.method == 'POST':
        form = NationalParkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'National Park created successfully!')
            return redirect('list_parks_view') 
    else:
        form = NationalParkForm()
    
    return render(request, 'store/createPark.html', {'form': form})


# View for listing all parks
def list_parks_view(request):
    parks = NationalPark.objects.all()
    return render(request, 'store/park.html', {'parks': parks})
  
  

def edit_park_view(request, id):
    park = get_object_or_404(NationalPark, id=id)
    if request.method == 'POST':
        form = NationalParkForm(request.POST, request.FILES, instance=park)
        if form.is_valid():
            form.save()
            messages.success(request, 'National Park updated successfully!')
            return redirect('list_parks_view')
    else:
        form = NationalParkForm(instance=park)
    
    return render(request, 'store/editPark.html', {'form': form, 'park': park})



def delete_park_view(request, id):
    park = get_object_or_404(NationalPark, id=id)
    if request.method == 'POST':
        park.delete()
        messages.success(request, 'National Park deleted successfully!')
        return redirect('list_parks_view')

    return render(request, 'store/confirm_delete.html', {'park': park})

# Trail Views
class TrailListView(View):
    def get(self, request):
        trails = Trail.objects.all()
        return render(request, 'store/trail.html', {'trails': trails})

class TrailCreateView(View):
    def get(self, request):
        form = TrailForm()  # Use the correct form
        return render(request, 'trails/trail_form.html', {'form': form})

    def post(self, request):
        form = TrailForm(request.POST)  # Use the correct form
        if form.is_valid():
            form.save()
            messages.success(request, 'Trail created successfully!')  # Add success message
            return redirect('trail_list')  # Redirect to the trail list page
        return render(request, 'trails/trail_form.html', {'form': form})

class TrailEditView(View):
    def get(self, request, pk):
        trail = get_object_or_404(Trail, pk=pk)
        form = TrailForm(instance=trail)  # Use the correct form
        return render(request, 'trails/trail_form.html', {'form': form})

    def post(self, request, pk):
        trail = get_object_or_404(Trail, pk=pk)
        form = TrailForm(request.POST, instance=trail)  # Use the correct form
        if form.is_valid():
            form.save()
            messages.success(request, 'Trail updated successfully!')  # Add success message
            return redirect('trail_list')  # Redirect to the trail list page
        return render(request, 'trails/trail_form.html', {'form': form})

class TrailDeleteView(View):
    def get(self, request, pk):
        trail = get_object_or_404(Trail, pk=pk)
        return render(request, 'trails/trail_confirm_delete.html', {'trail': trail})

    def post(self, request, pk):
        trail = get_object_or_404(Trail, pk=pk)
        trail.delete()
        messages.success(request, 'Trail deleted successfully!')  # Add success message
        return redirect('trail_list')  # Redirect to the trail list page