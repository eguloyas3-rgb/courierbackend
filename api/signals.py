from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import *



@receiver(post_save, sender=Label)
def send_label_email(sender, instance, created, **kwargs):
    if created:  
        subject = f"Shiparama Logistics - New Label Created for {instance.track.tracking_id}"
        message = (
            f"Dear {instance.name},\n\n"
            f"We are pleased to inform you that a new shipment has been created for your tracking ID: {instance.track.tracking_id}.\n"
            f"Your shipment is now being processed and is on its way. You can track the status of your items anytime on our website:\n"
            f"https://shiparamax.com/\n\n"
            f"If you have any questions or need assistance, please do not hesitate to contact our customer support team.\n\n"
            f"Thank You,\n"
            f"Shiparama Logistics"
        )
        recipient = instance.email

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,  
            [recipient],                 
            fail_silently=False,
        )









@receiver(post_save, sender=Complaint)
def send_complaint_email(sender, instance, created, **kwargs):
    if created:  # Only send email when a new complaint is created
        subject = f"Shiparama Logistics - New Complaint for {instance.track.tracking_id}"
        message = (
            f"Dear {instance.user_name},\n\n"
            f"A new complaint has been submitted by for tracking ID {instance.track.tracking_id}.\n"
            f"{instance.message}\n"
            f"Please contact customer support to take action.\n\n"
            f"Best regards,\n"
            f"Shiparama Logistics"
        )
        # admin_email = settings.ADMIN_EMAIL  # Set this in settings.py
        recipient = instance.email

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [recipient],
            fail_silently=False,
        )





# signals.py


@receiver(post_save, sender=ContactMessage)
def send_contact_email(sender, instance, created, **kwargs):
    if created:
        subject = f"New Contact Message from {instance.name}"
        message = (
            f"Name: {instance.name}\n"
            f"Email: {instance.email}\n\n"
            f"Message:\n{instance.message}\n"
        )
        admin_email = settings.EMAIL_HOST_USER  # set this in settings.py

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [admin_email],
            fail_silently=False,
        )
