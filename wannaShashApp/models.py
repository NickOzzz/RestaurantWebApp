from django.db import models

class ShashlikNaUgliach(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    Price = models.IntegerField()
    image = models.ImageField(upload_to='images')
    itemId = models.IntegerField()

class Assorti(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    Price = models.IntegerField()
    image = models.ImageField(upload_to='images')
    itemId = models.IntegerField()

class MiasnoiAssorti(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    Price = models.IntegerField()
    image = models.ImageField(upload_to='images')
    itemId = models.IntegerField()

class Shawerma(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    Price = models.IntegerField()
    image = models.ImageField(upload_to='images')
    itemId = models.IntegerField()

class Emails(models.Model):
    Sender = models.CharField(max_length=100)
    Receiver = models.CharField(max_length=100)

class SpacingMainPage(models.Model):
    SpacingBox2 = models.IntegerField()
    SpacingBox3 = models.IntegerField()
    SpacingBox4 = models.IntegerField()

class Costs(models.Model):
    DeliveryCost = models.IntegerField()