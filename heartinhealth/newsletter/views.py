from django.shortcuts import render
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from django.utils.timezone import now
from .models import Subscriber, Newsletter
from .serializers import SubscriberSRZ, NewsletterSRZ


class SubscriberViewSet(CreateModelMixin, GenericViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSRZ


class SendNewsletterViewSet(CreateModelMixin, GenericViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSRZ

    def perform_create(self, serializer):
        newsletter = serializer.save()  # Save the newsletter in the database

        # Get recipients' details
        recipients_data = newsletter.recipients.values("email", "first_name", "last_name")

        if not recipients_data:
            return  # No recipients, nothing to send

        # Send email to each recipient with their personalized name
        for recipient in recipients_data:
            email = recipient["email"]
            first_name = recipient["first_name"] or ""  # Handle missing names
            last_name = recipient["last_name"] or ""
            full_name = f"{first_name} {last_name}".strip()

            # Generate absolute image URL (if request is available)
            image_url = None
            if hasattr(self, "request") and newsletter.image:
                image_url = self.request.build_absolute_uri(newsletter.image.url)

            # Prepare email content
            html_content = render_to_string("newsletter_template.html", {
                "subject": newsletter.subject,
                "full_name": full_name,  # ✅ Now includes full name
                "body": newsletter.message,
                "image_url": image_url,
            })

            # Send email
            plain_text_content = strip_tags(newsletter.message)
            email_message = EmailMultiAlternatives(
                subject=newsletter.subject,
                body=plain_text_content,  # Fallback text content
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[email],
            )
            email_message.attach_alternative(html_content, "text/html")
            email_message.send()

        # Mark newsletter as sent
        newsletter.sent_at = now()
        newsletter.save()
