from django.contrib import admin

# Register your models here.
from test_app.models import Test_model

admin.site.register(Test_model)