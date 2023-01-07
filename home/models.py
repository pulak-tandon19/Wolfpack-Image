from django.db import models
from PIL import Image, ImageOps

# Create your models here.

class ImageEdit(models.Model):
    img = models.ImageField()
    img1 = models.ImageField()
    img2 = models.ImageField()
    img3 = models.ImageField()
    img4 = models.ImageField()

    def save(self, *args, **kwargs):
       
        super().save(*args, **kwargs)
        s1 = (200, 300)
        s2 = (500, 500)
        s3 = (1024, 768)

        im1 = Image.open(self.img.path)
        im1 = im1.resize(s1)
        im1.save(self.img1.path)
        im1.close()

        im2 = Image.open(self.img2.path)
        im2 = im2.resize(s2)
        im2.save(self.img2.path)
        im2.close()

        im3 = Image.open(self.img3.path)
        im3 = im3.resize(s3)
        im3.save(self.img3.path)
        im3.close()

        im4 = Image.open(self.img4.path)
        im = ImageOps.grayscale(im4)
        im.save(self.img4.path)
        im4.close()
            


