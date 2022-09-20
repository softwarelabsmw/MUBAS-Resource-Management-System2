################################### THIS IS THE PYTHON FILE FOR HANDLING USER REQUESTS #####################################

from django.urls import path

from .views import (
	# Import all list views from reservationapp
	ResourceListView,  BookingListView,

	# Import all detailed views from reservationapp
	ResourceDetailView, BookingDetailView,

	# Import all create views from reservationapp
	ResourceCreateView, BookingCreateView,

	# Import all update views from reservationapp
	ResourceUpdateView, BookingUpdateView,

	# Import all delete views from reservationapp
	ResourceDeleteView, BookingDeleteView,
)

from .views import daily_booking_chart

urlpatterns = [
	################################ THE CREATE_VIEW URLS ###########################################################
	path('resource/new/', ResourceCreateView.as_view(), name = 'resource_new'),
	path('booking/new/', BookingCreateView.as_view(), name = 'booking_new'),

	################################### THE LIST VIEW URLS ###########################################################
	path('resources/', ResourceListView.as_view(), name = 'resource_list'),
	path('bookings/', BookingListView.as_view(), name = 'booking_list'),
	
	################################# THE DETAILED_VIEW URLS #########################################################
	path('resource/<str:pk>/', ResourceDetailView.as_view(), name = 'resource_detail'),
	path('booking/<str:pk>/', BookingDetailView.as_view(), name = 'booking_detail'),
	
	################################ THE UPDATE VIEW URLS ############################################################
	path('resource/<str:pk>/edit/', ResourceUpdateView.as_view(), name = 'resource_edit'),
	path('booking/<str:pk>/edit/', BookingUpdateView.as_view(), name = 'booking_edit'),
	
	################################ THE DELETE VIEW URLS ############################################################
	path('resource/<str:pk>/delete', ResourceDeleteView.as_view(), name = 'resource_delete'),
	path('booking/<str:pk>/delete', BookingDeleteView.as_view(), name = 'booking_delete'),

	################################ CHART VIEW URLS ############################################################
	path('daily_booking/', daily_booking_chart, name = 'daily_booking'),
	]