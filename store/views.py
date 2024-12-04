from django.shortcuts import render,redirect
from .models import NationalPark,Trail
from .forms import NationalParkForm,TrailForm
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views import View
from django.http import JsonResponse
# Create your views here.
def dashboard_view(request):
    return render(request, 'dashboard.html')
  
  

def create_or_edit_park_view(request, id=None):
    # Handles both create and edit cases
    park = None if id is None else get_object_or_404(NationalPark, id=id)
    
    if request.method == 'POST':
        form = NationalParkForm(request.POST, request.FILES, instance=park)
        if form.is_valid():
            form.save()
            if park:
                messages.success(request, 'National Park updated successfully!')
            else:
                messages.success(request, 'National Park created successfully!')
            return redirect('list_parks_view')
    else:
        form = NationalParkForm(instance=park)
    
    return render(request, 'store/park_modal.html', {'form': form, 'park': park})


# View for listing all parks
def list_parks_view(request):
    parks = NationalPark.objects.all()
    return render(request, 'store/park.html', {'parks': parks})
  
  
def delete_park_view(request, id):
    park = get_object_or_404(NationalPark, id=id)
    park.delete()  
    messages.success(request, 'National Park deleted successfully!')
    return redirect('list_parks_view') 

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