from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post,PostTexts
from .forms import PostForm

def index(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def post(request, *args, **kwargs):
    post_id = kwargs.get('post_id')
    # post_text
    print(kwargs)
    print(post_id)
    print(post_id)
    print(post_id)
    post = Post.objects.get(id=post_id)
    # texts = PostTexts.objects.get(post_id=post_id)
    return render(request, 'post.html', {'post': post})

def create_post(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print('Valid')
            print('Valid')

            # post = Post(til)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')
        else:
            print('Invalid')
            print('Invalid')
    else:
        form = PostForm()

        return render(request, 'new_post.html', {'form': form})

def edit_post(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print('Valid')
            print('Valid')
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')
        else:
            print('Invalid')
            print('Invalid')
    else:
        form = PostForm()

        return render(request, 'new_post.html', {'form': form})
