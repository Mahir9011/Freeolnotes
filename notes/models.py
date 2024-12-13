from django.db import models
from tinymce.models import HTMLField  # Import TinyMCE's HTMLField

class Resource(models.Model):
    subject = models.CharField(max_length=100)
    topic = models.CharField(max_length=200)
    file_type = models.CharField(max_length=50)  # e.g., "Notes" or "Past Paper"
    file_link = models.URLField()  # Google Drive link
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.topic}"

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()  # Use TinyMCE's HTMLField for rich text editing
    subject = models.CharField(max_length=100)
    topic = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to='blog_covers/', blank=True, null=True)  # Optional cover image
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



