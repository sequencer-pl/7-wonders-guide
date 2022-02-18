from django.db import models


class Expansion(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=8192)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']


class Symbol(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='symbols/')
    description = models.CharField(max_length=8192)

    def __str__(self) -> str:
        return f"{self.name} - {self.description}"

    class Meta:
        ordering = ['name']


class CardType(models.Model):
    type = models.CharField(max_length=64)
    color = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"{self.type} ({self.color})"

    class Meta:
        ordering = ['type']


class Card(models.Model):
    name = models.CharField(max_length=64)
    type = models.ForeignKey(CardType, on_delete=models.CASCADE)
    symbol = models.ForeignKey(Symbol, on_delete=models.CASCADE)
    origin = models.ForeignKey(Expansion, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.origin} - {self.type} - {self.name}"

    class Meta:
        ordering = ['name', 'origin']


class Wonder(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='wonders/')
    origin = models.ForeignKey(Expansion, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} - {self.origin}"

    class Meta:
        ordering = ['name', 'origin']


class WonderStep(models.Model):
    wonder = models.ForeignKey(Wonder, on_delete=models.CASCADE)
    symbol = models.ForeignKey(Symbol, on_delete=models.CASCADE)
    level = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f"{self.wonder} - level {self.level}"

    class Meta:
        ordering = ['wonder', 'level']