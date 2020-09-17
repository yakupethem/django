from django.db import models

# Create your models here.

class yazar(models.Model):
    name=models.CharField(max_length=60)
    created=models.DateTimeField("created")
    def __str__(self):
        return self.name


class kitap(models.Model):
    name=models.CharField(max_length=60)
    created=models.DateTimeField("created")
    author=models.ForeignKey(yazar,on_delete=models.CASCADE)
    fiyat=models.DecimalField(decimal_places=2,max_digits=4,null=True   )

    def __str__(self):
        return self.name