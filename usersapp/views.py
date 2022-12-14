   ?  ?                                    ?  !                   ??  ?     ?i?    *          
 ?G     >vma???Zb ?   	  #             <  	              ????@ t z r e s . d l l , - 3 8 2                                                       @ t z r e s . d l l , - 3 8 1                                                   ????    @????????     ?%????       W i n d o w s U p d a t e _ t r a c e _ l o g   C : \ W I N D O W S \ L o g s \ W i n d o w s U p d a t e \ W i n d o w s U p d 
    success_url = reverse_lazy('login')
    
    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            usr_grp = Group.objects.get(name="")
            user.groups.add(usr_grp)
            return redirect('login')
        else:
            return render(request, self.template_name, {'form': form})

# User sign up view
class UserEditView(SuccessMessageMixin, UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/edit_profile.html'
    success_message = 'Your Profile was Successfully Updated'
    success_url = reverse_lazy('edit_profile')
    
    def get_object(self):
        return self.request.user


  




  