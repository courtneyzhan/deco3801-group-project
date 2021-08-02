from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
# from django.views.generic.edit import CreateView, UpdateView
from .models import Post
from django.contrib.auth.models import User
# from django.http import HttpResponse

# Routes
def home(request):
    # return HttpResponse('<h1>Diary Home</h1>')
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'diary/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'diary/home.html' # <app>/<model>_<viewtype>/html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostDeleteView(DeleteView):
    model = Post
    success_url = "/"

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = User.objects.get(id=1)
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = User.objects.get(id=1)
        return super().form_valid(form)

def about(request):
    # return HttpResponse('<h1>Diary About</h1>')
    return render(request, 'diary/about.html', {'title': 'About'})

