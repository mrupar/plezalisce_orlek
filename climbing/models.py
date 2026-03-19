from django.db import models

class Sector(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Route(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name='routes')
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    length = models.IntegerField()
    type = models.CharField(max_length=50, default="sport")
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/routes/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.grade})"