from django.contrib import admin
from .models import Project, Task, Tag   # ← ESTA línea es la que falta o está mal

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Tag)