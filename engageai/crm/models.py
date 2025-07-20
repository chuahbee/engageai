from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    source = models.CharField(max_length=100, help_text="例如：社群、电商网站")
    tag = models.CharField(max_length=100, blank=True, help_text="可打标签如“高潜在客户”")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
