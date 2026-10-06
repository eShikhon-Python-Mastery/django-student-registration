from django.db import models


class Student(models.Model):

    COURSE_CHOICES = [
        ('Python', 'Python'),
        ('Django', 'Django'),
        ('Java', 'Java'),
        ('Web Development', 'Web Development'),
    ]

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=20)

    course = models.CharField(
        max_length=50,
        choices=COURSE_CHOICES
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name