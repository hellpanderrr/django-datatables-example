from django.db import models
import random
# Create your models here.
class Test_model(models.Model):
    test_field_1 = models.BooleanField(default=False)
    a_test_field_2 = models.TextField(default='')
    b_test_field_3 = models.CharField(max_length=8)

#populate fields for this example
# for i in range(20):
#     field_1 = bool(random.randint(0,1))
#     field_2 = random.choice(['Django','Peter','Version','Something','Else'])
#     field_3 = random.choice(['A','B','C','D','E'])

#     j = Test_model(test_field_1=field_1,a_test_field_2=field_2,b_test_field_3=field_3)
#     j.save()
