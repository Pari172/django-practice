from django.db import models
from django.utils.text import slugify
# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_address = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['first_name','last_name']
    
    # We are overriding save method to save objects in db according to our convention
    def save(self,*args,**kwargs):
        if self.first_name:
            self.first_name = self.first_name.strip().title()
        if self.last_name:
            self.last_name = self.last_name.strip().title()
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Post(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True,
        help_text="Enter the title of post here",
    )
    excerpt = models.CharField(
        max_length=200,
        blank=True,
        help_text="Short summery of post"
    )
    image_name = models.ImageField(
        upload_to="blog_app/images/",
        blank=True,
        null=True,
        help_text="Optional featured image"
    )
    date = models.DateField(
        auto_now_add=True,
        help_text="Date when post was created"
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        help_text="URL-firendly identifier"
    )
    content = models.TextField(
        help_text="Main body of post"
    )
    author = models.ForeignKey(
        "Author", # yes we can write model name as string, django use it to resolve ordering issue of models and when model is not defined
        on_delete=models.CASCADE,
        related_name='posts',
        help_text="Author of the post"
    )
    tags = models.ManyToManyField(
        "Tag",
        blank=True,
        related_name='posts',
        help_text="Tags associated with the post"
    )
    class Meta:
        ordering = ['-date']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)
    
class Tag(models.Model):
    caption = models.CharField(max_length=20)

    class Meta:
        ordering = ['caption']
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    
    def __str__(self):
        return self.caption