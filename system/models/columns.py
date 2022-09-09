from django.db import models
from .common import BaseContent
from system.utils import ColumnTypeChoice, StatusChoice


class App(BaseContent):
    name = models.CharField(max_length=255, null=True)    
    def __str__(self):
        return self.name
    
    
class Columns(BaseContent):
    app = models.ForeignKey('App', on_delete=models.CASCADE, null=True, blank=True)
    list = models.ForeignKey('List', on_delete=models.SET_NULL, null=True)
    position = models.IntegerField(null=True, blank=True)
    default = models.BooleanField(default=False)
    required = models.BooleanField(default = False)
    optional = models.BooleanField(default = False)
    
    
    def __str__(self):
        return self.label
    
