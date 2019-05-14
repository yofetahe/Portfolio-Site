from django.db import models

class AboutMe(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    udpated_at = models.DateTimeField(auto_now=True)

class Portfolio(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    detail_info = models.TextField(null=True)
    technologies = models.TextField(null=True)
    image_url = models.CharField(max_length=225)
    site_url = models.CharField(max_length=225)
    github_url = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    udpated_at = models.DateTimeField(auto_now=True)

class PortfolioDetail(models.Model):
    description = models.TextField()
    image_url = models.CharField(max_length=225)
    display_order = models.IntegerField()
    portfolio = models.ForeignKey(Portfolio, related_name="portfolio_detail")
    created_at = models.DateTimeField(auto_now_add=True)
    udpated_at = models.DateTimeField(auto_now=True)

class Technology(models.Model):
    name = models.CharField(max_length=225)
    image_url = models.CharField(max_length=225)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    udpated_at = models.DateTimeField(auto_now=True)

class MyNote(models.Model):
    title = models.CharField(max_length=225)
    intro_info = models.TextField()
    categoty = models.CharField(max_length=225)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    udpated_at = models.DateTimeField(auto_now=True)
