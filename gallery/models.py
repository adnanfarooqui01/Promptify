from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]
        unique_together = ('slug',)

    def __str__(self):
        return self.name
    

class ImagePrompt(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
    prompt = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="images")
    is_trending = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Image Prompt"
        verbose_name_plural = "Image Prompts"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
