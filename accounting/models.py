from django.db import models
from records.models import Visit


# Create your models here.
class Invoice(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    generated_at = models.DateTimeField(auto_now_add=True)
    content = models.BinaryField()
