from django.db import models
import os
from django.conf import settings
User = settings.AUTH_USER_MODEL

class SavedRecord(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    voice_record = models.FileField(upload_to="uploades/records/")
    title = models.CharField(max_length=50, null=True)
    original_response = models.TextField(default=None, null=True)
    saved_response = models.TextField(default=None, null=True)
    recorded = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "SavedRecord"
        verbose_name_plural = "SavedRecords"

    def __str__(self):
        return str(self.user.email)

    def deleteObjWithFile(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.voice_record.name))
        super(SavedRecord,self).delete(*args,**kwargs)


class TempRecord(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    voice_record = models.FileField(upload_to="uploades/records/")
    original_response = models.TextField(default=None, null=True)
    recorded = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "TempRecord"
        verbose_name_plural = "TempRecords"

    def __str__(self):
        return str(self.user.email)

    def deleteObjWithFile(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.voice_record.name))
        super(TempRecord,self).delete(*args,**kwargs)
