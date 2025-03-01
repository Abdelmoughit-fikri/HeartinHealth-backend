from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


def get_default_user():
    """Fetches the first user or creates a default user if none exist."""
    user = User.objects.first()
    if user:
        return user.id  # Returns a valid user ID
    return None  # Allows NULL if no user exists


class CdArticle(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_DEFAULT,
        default=get_default_user,
        related_name="cardiacDiseasesArticles",
    )
    author_label = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(
        max_length=50,
        choices=[
            ("heart diseases", "heart diseases"),
            ("vascular diseases", "vascular diseases"),
            (
                "Systemic & Inflammatory Cardiovascular Diseases",
                "Systemic & Inflammatory Cardiovascular Diseases",
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
            ("Electrical Disorders", "Electrical Disorders"),
            ("Hypertensive Heart Disease", "Hypertensive Heart Disease"),
            ("Heart Failure", "Heart Failure"),
            ("Pericardial Diseases", "Pericardial Diseases"),
            ("Arterial Diseases", "Arterial Diseases"),
            ("Venous Diseases", "Venous Diseases"),
        ],
        null=True,
    )
    overView = models.TextField()
    content = models.TextField()
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
    is_highlighted_score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, null=True
    )

    def __str__(self):
        return self.title


class SecondaryImage(models.Model):
    Article = models.ForeignKey(
        CdArticle, on_delete=models.CASCADE, related_name="secondary_images"
    )
    secondary_image = models.ImageField(
        upload_to="CD/secondary_images", blank=True, null=True
    )


class AttachedFile(models.Model):
    Article = models.ForeignKey(
        CdArticle, on_delete=models.CASCADE, related_name="attached_files"
    )
    attached_file = models.FileField(
        upload_to="CD/attached_files", blank=True, null=True
    )
