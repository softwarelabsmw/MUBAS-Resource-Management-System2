from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User

class UserAdmin(UserAdmin):
	add_fieldsets = (
		(None, {
			'fields': ('reg_no', 'email', 'username', 'password1', 'password2'),
			}),
		)
	add_form = UserCreationForm
	form = UserChangeForm
	model = User
	list_display = ['reg_no', 'username', 'email', 'first_name', 'last_name', 'gender', 'department', 'user_type', 'is_staff', 'is_active' ]
	# Add a "customised user" fields to the User admin page.
	fieldsets = tuple(
		# For the "Personal info" fieldset, drill down to the fields,
		# preserving everything else.
		(fieldset[0], {
			# Preserve any entries in the dict other than "fields".
			**{key: value for (key, value) in fieldset[1].items() if key != 'fields'},
			# Add the "customised" fields to the existing fields
			'fields': fieldset[1]['fields'] + ('reg_no', 'gender', 'phone', 'department', 'user_type', 'photo',)
		})
		# Preserve any fieldsets other than "Personal info".
		if fieldset[0] == 'Personal info'
		else fieldset
		for fieldset in UserAdmin.fieldsets
	)

# registering the models in the adminApp
admin.site.register(User, UserAdmin)