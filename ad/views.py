from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 

from .models import Category, Post
from .forms import PostForm, SignupForm

def getNav():
    return Category.objects.all()

def index(request):
    data = {}
    categories = Category.objects.all()
    for category in categories:
        recent_posts = Post.objects.filter(category=category).order_by('-published_date')[:5]
        data[category] = recent_posts 
        
    context = {'cat_posts' : data, 'nav_categories': getNav()}    
    return render(request, 'ad/index.html', context)

def category(request, category_id):
    category = Category.objects.get(pk=category_id)
    return render(request, 'ad/category.html', { 'category' : category, 'nav_categories': getNav()})

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    other_posts = Post.objects.filter(category=post.category).exclude(pk=post_id).order_by('-published_date')
    return render(request, 'ad/post.html', { 'post' : post, 'other_posts': other_posts, 'nav_categories': getNav()})

@login_required(redirect_field_name='next')
def createAd(request):
    if request.method == 'POST':

        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.published_date = timezone.now()
            new_post.save()
            messages.add_message(request, messages.INFO, "Your post was added successfully!")
            
            return HttpResponseRedirect(reverse('ad:post', args=[(new_post.id)] ))
    else:
        form = PostForm()
    return render(request, 'ad/new-post.html', {'form': form, 'nav_categories': getNav})    

@login_required
def profile(request, user_id):
    posts = Post.objects.filter(author_id=user_id)
    return render(request, 'ad/profile.html', {'posts': posts, 'nav_categories': getNav})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            firstName = form.cleaned_data['first_name']
            lastName = form.cleaned_data['last_name']
            email = form.cleaned_data['email']

            User.objects.create_user(username, email=email, password=password, first_name=firstName, last_name=lastName)
            messages.add_message(request, messages.INFO, "User account created successfully!")
            return HttpResponseRedirect(reverse('ad:login'))
    else:
        form = SignupForm()
    return render(request, 'registration/sign_up.html', {'form': form, 'nav_categories': getNav()})    

def userPosts(request, user_id):
    posts = Post.objects.filter(author_id=user_id)
    return render(request, 'ad/profile.html', {'posts': posts, 'nav_categories': getNav()})