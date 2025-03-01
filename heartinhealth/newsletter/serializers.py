from rest_framework import serializers
from .models import Subscriber, Newsletter

class SubscriberSRZ(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = [
            'email',
            'first_name',
            'last_name'
        ]
   
class NewsletterSRZ(serializers.ModelSerializer):
    recipients = SubscriberSRZ(many=True, read_only=True)
    class Meta:
        model = Newsletter
        fields = ["subject", "message", "image", "recipients"]
        

    def create(self, validated_data):
        recipients = validated_data.pop("recipients", [])
        newsletter = Newsletter.objects.create(**validated_data)
        newsletter.recipients.set(recipients)
        return newsletter