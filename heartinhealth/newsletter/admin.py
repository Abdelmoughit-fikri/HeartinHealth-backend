from django.contrib import admin
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import format_html
from django.urls import path
from django.shortcuts import redirect
from django.contrib import messages
from .models import Subscriber, Newsletter

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('subject', 'sent_at', 'preview_image', 'send_newsletter_button')

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" height="50" style="border-radius:5px;" />', obj.image.url)
        return "No Image"
    preview_image.short_description = "Image Preview"

    def send_newsletter_button(self, obj):
        return format_html(
            '<a class="button" style="background:#28a745;color:white;padding:5px 10px;border-radius:5px;text-decoration:none;" href="{}">Send</a>',
            f"send-newsletter/{obj.id}/"
        )
    send_newsletter_button.short_description = "Send Newsletter"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('send-newsletter/<int:newsletter_id>/', self.admin_site.admin_view(self.send_newsletter))
        ]
        return custom_urls + urls

    def send_newsletter(self, request, newsletter_id):
        newsletter = Newsletter.objects.get(id=newsletter_id)
        recipients = newsletter.recipients.values("email", "first_name", "last_name")

        if not recipients:
            self.message_user(request, "No recipients found!", level=messages.WARNING)
            return redirect("..")

        for recipient in recipients:
            email = recipient["email"]
            first_name = recipient["first_name"] or ""
            last_name = recipient["last_name"] or ""
            full_name = f"{first_name} {last_name}".strip()

            # Build the absolute image URL
            image_url = request.build_absolute_uri(newsletter.image.url) if newsletter.image else None

            # Render personalized HTML email template
            html_content = render_to_string("newsletter_template.html", {
                "title": newsletter.subject,
                "full_name": full_name,  # ✅ Now the name is included!
                "body": newsletter.message,
                "image_url": image_url
            })

            # Send email with alternative HTML content
            email_message = EmailMultiAlternatives(
                subject=newsletter.subject,
                body=newsletter.message,  # Fallback text content
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[email],
            )
            email_message.attach_alternative(html_content, "text/html")
            email_message.send()

        self.message_user(request, "Newsletter sent successfully!", level=messages.SUCCESS)
        return redirect("..")
