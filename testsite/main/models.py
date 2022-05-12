from django.db import models

class Processes(models.Model):
    processData = models.CharField(default='test', max_length=5000)
    
    def __str__(self):
        return self.processData

    # removing extra s
    class Meta:
        verbose_name_plural = "Processes"







