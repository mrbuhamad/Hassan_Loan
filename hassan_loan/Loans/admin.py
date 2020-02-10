from django.contrib import admin
from .models import Loan, Pyments, Participants


admin.site.register(Loan)
admin.site.register(Pyments)
admin.site.register(Participants)