from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import LocationForm
from .models import Location
# Create your views here.
@login_required
def locations_list_view(request):
   user = request.user
   form = LocationForm(request.POST or None)

   if(request.method == "POST"):
      if(form.is_valid()):
         cleaned = form.cleaned_data
         location = Location(
               name=cleaned['name'],
               timezone=cleaned['timezone'],
               user=user
            )

         location.save()
         form = LocationForm()
         messages.success(request, "Location {0} successfully added".format(location))


   locations = (Location.objects.filter(public=True)|Location.objects.filter(user=user)).filter(deleted=False)
   context = {
      'locations': locations,
      'form': form,
   }
   return render(request, 'locations/list.html', context)

@login_required
def delete(request, pk):
   user = request.user

   location = Location.objects.get(pk=pk)

   if(location.user.id != user.id):
      messages.error(request, "Unable to delete {0}. Not the user for this location.".format(game))
      return redirect('locations:list')

   location.deleted = True

   location.save()

   messages.success(request, "Location {0} successfully deleted".format(location))
   return redirect('locations:list')