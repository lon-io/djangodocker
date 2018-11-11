from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post,PostText
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
    post_text = PostText.objects.get(post=post)
    # texts = PostTexts.objects.get(post_id=post_id)
    return render(request, 'post.html', {'post': post, 'post_text': post_text})

def create_post(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print('Valid')
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']

            current_user = request.user

            post = Post(title=title, created_by=current_user)
            post.save()

            postText = PostText(text=text, author=current_user, post=post, version=1)
            postText.save()

            # Todo: check auth
            # if request.user.is_authenticated():
            #     # Do something for authenticated users.
            # else:
            #     # Do something for anonymous users.

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

def edit_post(request, *args, **kwargs):
    post_id = kwargs.get('post_id')
    post = Post.objects.get(id=post_id)
    post_text = PostText.objects.get(post=post)

    form = PostForm(initial={'title': post.title, 'text': post_text.text}, is_edit_mode=True)

    return render(request, 'edit_post.html', {'form': form, 'post': post, 'post_text': post_text})

def update_post(request, *args, **kwargs):
    post_id = kwargs.get('post_id')
    post = Post.objects.get(id=post_id)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print('Valid')
            text = form.cleaned_data['text']

            current_user = request.user

            prev_post_text = PostText.object.get(post=post)

            print(prev_post_text)
            print(prev_post_text)
            print(prev_post_text)

            new_post_text = PostText(text=text, post=post, version=prev_post_text.version + 1, author=current_user)
            new_post_text.save()

            # Todo: check auth
            # if request.user.is_authenticated():
            #     # Do something for authenticated users.
            # else:
            #     # Do something for anonymous users.

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(f'/posts/{post.id}')
        else:
            print('Invalid')
            print('Invalid')
