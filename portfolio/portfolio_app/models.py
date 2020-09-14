from django.db import models
from django.utils.html import mark_safe


# Create your models here.

# models for homepage start
class Tags(models.Model):
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag


class Home(models.Model):
    name = models.CharField(max_length=20)
    title = models.TextField(max_length=500)
    email = models.EmailField(max_length=50, default='sunnydecent11@gmail.com')
    phone = models.CharField(max_length=12, default='8383966836')
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.name


class Slider(models.Model):
    slider_img = models.ImageField(upload_to='images/')

    @property
    def thumbnail_preview(self):
        if self.slider_img:
            return mark_safe('<img src="{}" width="250" height="250" />'.format(self.slider_img.url))
        return ""

    def __str__(self):
        return self.slider_img.url


# models for homepage ends


# models for Resume page starts


class Resume_intro(models.Model):
    profile_img = models.ImageField(upload_to='images/')
    desc = models.TextField(max_length=500)
    age = models.IntegerField()
    residence = models.CharField(max_length=500)
    choices_for_freelance = [
        ('Available', 'Available'),
        ('Not Available', 'Not Available'),
    ]
    freelance = models.CharField(max_length=30, choices=choices_for_freelance, default='Available', )
    address = models.CharField(max_length=500)
    email = models.EmailField(max_length=50, default='sunnydecent11@gmail.com')
    phone = models.CharField(max_length=12, default='8383966836')
    resume = models.FileField(upload_to='file/')

    @property
    def thumbnail_preview(self):
        if self.profile_img:
            return mark_safe('<img src="{}" width="250" height="250" />'.format(self.profile_img.url))
        return ""

    def __str__(self):
        return self.desc


class Resume_services(models.Model):
    icon = models.CharField(max_length=20)
    heading = models.CharField(max_length=150)
    desc = models.CharField(max_length=300)

    def __str__(self):
        return self.heading


class Resume_experience(models.Model):
    from_date = models.DateField()
    to_date = models.DateField()
    present = models.BooleanField()
    designation = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    role_and_responsibility = models.TextField(max_length=500)

    def __str__(self):
        return self.company


class Resume_education(models.Model):
    from_date = models.DateField()
    to_date = models.DateField()
    institute = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
    score = models.FloatField()

    def __str__(self):
        return self.institute


class Resume_language_skill(models.Model):
    language = models.CharField(max_length=30)
    skill_rating = models.IntegerField()

    def __str__(self):
        return self.language


class Resume_coding_skill(models.Model):
    skill = models.CharField(max_length=100)
    skill_rating = models.IntegerField()

    def __str__(self):
        return self.skill


class Resume_knowledge(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Resume_interests(models.Model):
    icon = models.CharField(max_length=20)
    heading = models.CharField(max_length=150)
    desc = models.CharField(max_length=300)

    def __str__(self):
        return self.heading


class Testimonials(models.Model):
    profile_img = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=20)
    designation = models.CharField(max_length=150)
    desc = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Client_logos(models.Model):
    logos = models.ImageField(upload_to='images/')


class Custom_text(models.Model):
    desc = models.TextField(max_length=500)

    def __str__(self):
        return self.desc


# models for Resume page ends

# models for Portfolio page starts

class Portfolio(models.Model):
    portfolio_img = models.ImageField(upload_to='images/')
    link = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# models for Portfolio page ends

# models for Contact page starts

class Contact_detail(models.Model):
    icon = models.CharField(max_length=20)
    heading = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)

    def __str__(self):
        return self.heading
