####################### THIS IS THE PYTHON FILE FOR HANDLING BUSINESS LOGIC ##########################################

from django.shortcuts import render 
from django.http import HttpResponseRedirect

from .models import (Resource, Booking)

from django.views.generic import (TemplateView, ListView, DetailView)
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)

from django.urls import reverse_lazy

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.messages.views import * # SuccessMessageMixin,
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group

from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth

from django.db.models import Q

from django.http import JsonResponse


#############################THE CREATE VIEWS FOR ALL THE MODELS IN reservationapp#####################################

class ResourceCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView): 
	model = Resource
	template_name = 'resources/resource_new.html'
	fields = "__all__"
	success_message = 'Added New Record Successfully'
	permission_required = ('reservationapp.add_Resource',)

class BookingCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
	model = Booking
	template_name = 'bookings/booking_new.html'
	fields = ['resource', 'reservation_date', 'return_date']
	success_message = 'Added New Record Successfully'
	permission_required = ('reservationapp.add_Booking',)

#########################THE LIST VIEWS FOR ALL THE MODELS IN reservationapp#############################################

# The Resource List View
class ResourceListView(LoginRequiredMixin, PermissionRequiredMixin,  ListView):
	model = Resource
	template_name = 'resources/resource_list.html'
	context_object_name = 'resources'
	permission_required = ('reservationapp.view_Resource',)

# The Booking List View
class BookingListView(LoginRequiredMixin, PermissionRequiredMixin,  ListView):
	model = Booking
	template_name = 'bookings/booking_list.html'
	context_object_name = 'bookings'
	permission_required = ('reservationapp.view_Booking',)

#############################THE DETAILED VIEWS FOR ALL THE MODELS IN reservationapp#####################################

# The Resource's Detail View
class ResourceDetailView(UserPassesTestMixin, PermissionRequiredMixin, DetailView):
	model = Resource
	template_name = 'resources/resource_detail.html'
	permission_required = ('reservationapp.view_Resource',)
	
	def test_func(self):
		return self.request.user.is_authenticated

# The Booking's Detail View
class BookingDetailView(UserPassesTestMixin, PermissionRequiredMixin, DetailView):
	model = Booking
	template_name = 'bookings/booking_detail.html'
	permission_required = ('reservationapp.view_Booking',)
	
	def test_func(self):
		return self.request.user.is_authenticated

#############################THE DETAILED VIEWS FOR ALL THE MODELS IN reservationapp#####################################

# The resource Update View
# @method_decorator(user_passes_test(lambda u: Group.objects.get(name='') in u.groups.all()), name='dispatch')
class ResourceUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
				model = Resource
				template_name = 'resources/resource_edit.html'
				fields = "__all__"
				success_message = 'Record Updated Successfully'

# The booking Update View
# @method_decorator(user_passes_test(lambda u: Group.objects.get(name='') in u.groups.all()), name='dispatch')
class BookingUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
				model = Booking
				template_name = 'bookings/booking_edit.html'
				fields = ['status', 'reservation_date', 'return_date']
				success_message = 'Record Updated Successfully'

############################# THE DELETE VIEWS FOR ALL THE MODELS IN reservationapp #####################################

# The resource delete view
# @method_decorator(user_passes_test(lambda u: Group.objects.get(name='') in u.groups.all()), name='dispatch')
class ResourceDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView): 
				model = Resource
				template_name = 'resources/resource_delete.html'
				success_message = 'Record Deleted Successfully'
				success_url = reverse_lazy('resource_list')

# The booking delete view
# @method_decorator(user_passes_test(lambda u: Group.objects.get(name='') in u.groups.all()), name='dispatch')
class BookingDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView): 
				model = Booking
				template_name = 'bookings/booking_delete.html'
				success_message = 'Record Deleted Successfully'
				success_url = reverse_lazy('booking_list')


# Chart Creation Views
def daily_booking_chart(request):
    data = []
    labels = []

    queryset = Booking.objects.values('resource__resource_name').annotate(daily_count=Count('pk')).order_by(
        '-daily_count')
    for entry in queryset:
        labels.append(entry['resource__resource_name'])
        data.append(entry['daily_count'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
