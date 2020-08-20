from rest_framework import serializers
from .models import User
import json
""" Imorting a rest framework serlizaers class for for linking the arguments """
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        """ creating a python list to show the database attributes """
        fields =["id", "real_name", "tz","start_time", "end_time"]
