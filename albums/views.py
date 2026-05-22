from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Album

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redirects to login page after successful registration
    template_name = 'registration/signup.html' 

    # ADD THIS TEMPORARY METHOD:
    def form_valid(self, form):
        response = super().form_valid(form)
        # If you sign up with the username 'admin_demo', it automatically promotes you
        if self.object.username == 'admin':
            self.object.is_staff = True
            self.object.is_superuser = True
            self.object.save()
        return response

# READ: List all albums
class AlbumListView(ListView):
    model = Album
    template_name = 'albums/album_list.html'
    context_object_name = 'albums'

# CREATE: Add a new album (Must be logged in)
class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    fields = ['title', 'description', 'cover_image'] # Notice 'created_by' is NOT here
    template_name = 'albums/album_form.html'
    success_url = reverse_lazy('album-list')

    def form_valid(self, form):
        # Set the logged-in user as the creator of the album
        form.instance.created_by = self.request.user
        return super().form_valid(form)

# UPDATE: Edit (RBAC - Only owner or admin)
class AlbumUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Album
    fields = ['title', 'description', 'cover_image']
    template_name = 'albums/album_form.html'
    success_url = reverse_lazy('album-list')

    def test_func(self):
        album = self.get_object()
        return self.request.user == album.created_by or self.request.user.is_superuser
    
# DELETE: Remove album (RBAC - Only owner or admin)
class AlbumDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Album
    template_name = 'albums/album_confirm_delete.html'
    success_url = reverse_lazy('album-list')

    def test_func(self):
        album = self.get_object()
        return self.request.user == album.created_by or self.request.user.is_superuser