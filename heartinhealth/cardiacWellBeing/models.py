from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class CwbArticle(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(
        max_length=50,
        choices=[
            ("Stress", "Stress Management"),
            ("Exercice", "Physical Activity"),
            ('Nutrition', 'Nutrition & Diet'),
            ("MindBody","Mind-Body Practices"),
        ],
        null=True,
    )
    description= models.CharField(max_length=200, null=True)
    content = CKEditor5Field('Content', config_name='extends')
    keywords = models.CharField(max_length=500, help_text="comma-separated keywords")
    search_queries = models.CharField(max_length=200, help_text="csv", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    primary_image = models.ImageField(upload_to="CWB/primary_images")
    video_URL = models.URLField(blank=True, null=True)
    links = models.TextField(
        help_text="enter multiple URLs as csv", blank=True, null=True
    )
    is_active = models.BooleanField(default=True)
    is_important = models.BooleanField(default=False)
    is_highlighted = models.BooleanField(default=False)

    def __str__(self):
        return self.title



class AttachedFile(models.Model):
    Article = models.ForeignKey(
        CwbArticle, on_delete=models.CASCADE, related_name="attached_files"
    )
    attached_file = models.FileField(
        upload_to="CWB/attached_files", blank=True, null=True
    )
