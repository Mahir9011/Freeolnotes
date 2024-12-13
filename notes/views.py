from django.shortcuts import render
from .models import Resource, BlogPost  # Import BlogPost here

# Homepage View
def home(request):
    return render(request, 'home.html')

# Subjects List View
def subjects(request):
    # Get a list of unique subjects from the database
    subjects = Resource.objects.values_list('subject', flat=True).distinct()
    return render(request, 'subjects.html', {'subjects': subjects})

# Resources View (for a specific subject)
def resources(request, subject):
    # Get all resources for the selected subject
    resources = Resource.objects.filter(subject=subject)
    return render(request, 'resources.html', {'resources': resources, 'subject': subject})

def blog_list(request):
    # Get all blog posts
    blog_posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog_list.html', {'blog_posts': blog_posts})

def blog_detail(request, pk):
    # Get a specific blog post by ID
    blog_post = BlogPost.objects.get(pk=pk)
    return render(request, 'blog_detail.html', {'blog_post': blog_post})