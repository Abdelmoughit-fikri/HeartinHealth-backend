from django.db import models
from django_ckeditor_5.fields import CKEditor5Field



class CdArticle(models.Model):
    title = models.CharField(max_length=200) 
    category = models.CharField(
        max_length=50,
        choices=[
            ("Heart Diseases", "Heart Diseases"),
            ("Vascular Diseases", "Vascular Diseases"),
            (
                "Systemic Diseases",
                "Systemic Diseases",
            ),
        ],
    )
    sub_category = models.CharField(
        max_length=50,
        choices=[
            ("Congenital Heart Diseases", "Congenital Heart Diseases"),
            ("Valvular Heart Diseases", "Valvular Heart Diseases"),
            ("Myocardial Diseases", "Myocardial Diseases"),
            ("Ischemic Heart Diseases", "Ischemic Heart Diseases"),
            ("Thromboembolic Diseases", "Thromboembolic Diseases"),
            ("Arrhythmias", "Arrhythmias"),
            ("Hypertensive Heart Diseases", "Hypertensive Heart Diseases"),
            ("Heart Failure", "Heart Failure"),
            ("Pericardial Diseases", "Pericardial Diseases"),
            ("Metabolic Disorders", "Metabolic Disorders"),
            ("Arterial Diseases", "Arterial Diseases"),
            ("Venous Diseases", "Venous Diseases"),
        ],
        null=True,
    )
    description= models.CharField(max_length=200, null=True)
    content = CKEditor5Field('Content', config_name='extends')
    keywords = models.CharField(max_length=500, help_text="comma-separated keywords")
    search_queries = models.CharField(max_length=200, help_text="csv", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    primary_image = models.ImageField(upload_to="CD/primary_images")
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
        CdArticle, on_delete=models.CASCADE, related_name="attached_files"
    )
    attached_file = models.FileField(
        upload_to="CD/attached_files", blank=True, null=True
    )
