from django.contrib import admin
from quora_api.models import (
    Question,
    Answer
)

admin.site.register(Question)
admin.site.register(Answer)