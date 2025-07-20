from django.db import models
from crm.models import Customer

class InteractionRecord(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='interactions')
    channel = models.CharField(max_length=50, choices=[('email', 'Email'), ('message', 'Message'), ('voice', 'Voice')])
    content = models.TextField()
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"对话记录 - {self.customer.name} - {self.channel}"
    
class KMPInteraction(models.Model):
    input_text = models.TextField()
    matched_keyword = models.CharField(max_length=100, blank=True, null=True)
    response_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.input_text[:20]}... → {self.matched_keyword or '无匹配'}"
