from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    supra_category = models.CharField(max_length=50, choices=[
        ('heart diseases', 'heart diseases'),
        ('vascular diseases', 'vascular diseases'),
        ('Systemic & Inflammatory Cardiovascular Diseases',
         'Systemic & Inflammatory Cardiovascular Diseases')
    ])
    sub_category = models.CharField(max_length=50, choices=[
        ('Congenital Heart Diseases', 'Congenital Heart Diseases'),
        ('Valvular Heart Diseases', 'Valvular Heart Diseases'),
        ('Myocardial Diseases' , 'Myocardial Diseases'),
        ('Ischemic Heart Diseases' , 'Ischemic Heart Diseases'),
        ('Electrical Disorders' , 'Electrical Disorders'),
        ('Hypertensive Heart Disease' , 'Hypertensive Heart Disease'),
        ('Heart Failure' , 'Heart Failure'),
        ('Pericardial Diseases' , 'Pericardial Diseases'),
        ('Arterial Diseases' , 'Arterial Diseases'),
        ('Venous Diseases' , 'Venous Diseases'),
    ], null=True)
    overView = models.TextField()
    content = models.TextField()
    keywords = models.CharField(
        max_length=500, help_text='comma-separated keywords')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    primary_image = models.ImageField(upload_to='cwb/primary_images')
    video_URL = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class SecondaryImage(models.Model):
    Article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='secondary_images')
    secondary_image = models.ImageField(
        upload_to='cwb/secondary_images', blank=True, null=True)


class AttachedFile(models.Model):
    Article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='attached_files')
    attached_file = models.FileField(
        upload_to='cwb/attached_files', blank=True, null=True)
