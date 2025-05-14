from django.db import models

class BookDemoModel(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    institution = models.CharField(max_length=100, null=True)
    phone = models.IntegerField(null=True)
    subject = models.TextField(default=None, null=True, max_length=150)
    message = models.TextField(default=None, null=True, max_length=750)

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.email)
