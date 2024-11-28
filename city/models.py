from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class MyUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_user = models.BooleanField(default=True)
    is_employee = models.BooleanField(default=False)

class Complaint(models.Model):
    STATUS = (
        ('Submitted', 'Submitted'),
        ('Pending', 'Pending'),
        ('Resolved', 'Resolved')
    )
    COMPLAINTS = (
        ('Garbage dump', 'Garbage dump'),
        ('Overflow of Septic Tanks', 'Overflow of Septic Tanks'),
        ('Burning of Garbage', 'Burning of Garbage'),
        ('Stagnant Water', 'Stagnant Water'),
        ('Dustbins not cleaned', 'Dustbins not cleaned'),
        ('Improper Sanitization', 'Improper Sanitization'),
        ('Open Manholes or Drains', 'Open Manholes or Drains'),
    )
    user_name = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    complaint_type = models.CharField(max_length=200, null=True, choices=COMPLAINTS)
    address = models.CharField(max_length=500, null=True)
    city = models.CharField(max_length=100, null=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    thumbs_up = models.PositiveIntegerField(default=0)
    is_verified = models.BooleanField(default=False)
    voted_users = models.ManyToManyField(MyUser, related_name='voted_complaints', blank=True)
    landmark = models.CharField(max_length=200, null=True)
    info = models.CharField(max_length=200, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    complaint_date = models.DateTimeField(auto_now_add=True, null=True)
    picture = models.ImageField(null=True)
    video = models.FileField(upload_to='uploads/complaint_videos/', null=True, blank=True)
    tracking_id = models.CharField(null=True, max_length=16)
    status = models.CharField(max_length=200, null=True, default='Submitted', choices=STATUS)

    def _str_(self):
        return f"{self.user_name}"

class Queries(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=500, null=True)

    def _str_(self):
        return f"{self.user_name} - Verified: {self.is_verified}"

class Feedback(models.Model):
    person_name = models.CharField(max_length=255)
    testimonial = models.TextField()
    rating = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Feedback by {self.person_name} on {self.date}"