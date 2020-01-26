from django.db import models
from django.utils import timezone


class Test(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Test'
        verbose_name_plural = 'Tests'

    def __repr__(self):
        return f"Test(name='{self.name}')"

    def __str__(self):
        return self.name
