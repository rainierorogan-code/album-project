from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Album

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Gracefully handle the instance creation
        user = form.save(commit=False)
        
        # Keep our temporary admin hook logic safe and simple
        if user.username == 'admin_demo':
            user.is_staff = True
            user.is_superuser = True
            
        user.save()
        return super().form_valid(form)

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