from django.db import models


class Subject(models.Model):

    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "과목 관리"
    
    def __str__(self):
        return self.name