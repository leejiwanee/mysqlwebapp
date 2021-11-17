from django.db import models


class Parameter(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    values = models.CharField(max_length=45, blank=True, null=True)
    allowed_values = models.CharField(max_length=200,null=True)
    modifiable = models.IntegerField()
    source = models.CharField(max_length=45)
    apply_type = models.CharField(max_length=45)
    data_type = models.CharField(max_length=45)
    description = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'parameters'  #db_table can be changed