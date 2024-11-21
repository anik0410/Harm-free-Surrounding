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
    area = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=100, null=True)
    pincode = models.CharField(max_length=6, null=True)
    thumbs_up = models.PositiveIntegerField(default=0)
    is_verified = models.BooleanField(default=False)
    voted_users = models.ManyToManyField(MyUser, related_name='voted_complaints', blank=True)
    landmark = models.CharField(max_length=200, null=True)
    info = models.CharField(max_length=200, null=True)
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

    def __str__(self):
        return f"{self.user_name} - Verified: {self.is_verified}"

class Feedback(models.Model):
    person_name = models.CharField(max_length=255)
    testimonial = models.TextField()
    rating = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.person_name} on {self.date}"

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='services/', null=True, blank=True)

    def __str__(self):
        return self.title

class GreenInitiative(models.Model):
    title = models.CharField(max_length=200)
    information = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='initiatives/', null=True, blank=True)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class GreenInitiativeComment(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    green_initiative = models.ForeignKey(GreenInitiative, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    personal_views = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.green_initiative.title}"
