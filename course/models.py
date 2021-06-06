from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    imgpath = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Course(models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    logo = models.CharField(max_length = 255)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return self.name


class Branch(models.Model):
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete = models.CASCADE, related_name = "branches")

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'
 

class Contact(models.Model):
    CONTACT = [
        (1, 'Phone'),
        (2, 'Email'),
        (3, 'Facebook'),
    ]
    contact_type = models.IntegerField(choices=CONTACT)
    value = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete = models.CASCADE, related_name = "contacts")

    def __str__(self):
        return self.value

