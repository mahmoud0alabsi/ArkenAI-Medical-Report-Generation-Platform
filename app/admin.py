from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models.users.models import CustomUser, ProfileInfo
from .models.records.models import SavedRecord, TempRecord
from .models.book.book_model import BookDemoModel

from .models.users.form import *
from .models.records.forms import *

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ProfileInfo, ProfileInfoAdmin)

admin.site.register(SavedRecord, SavedRecordAdmin)
admin.site.register(TempRecord, TempRecordAdmin)

admin.site.register(BookDemoModel)

