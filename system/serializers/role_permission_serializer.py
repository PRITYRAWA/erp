from ..models.entity import *
from rest_framework import serializers
from system.models.roles_permissions import *

class PermissionSerializer(serializers.ModelSerializer):
    roles = serializers.SerializerMethodField()

    def get_roles(self, obj):
        queryset = RolePermissions.objects.filter(permissions=obj.id)
        serializer = RolePermissionSerializer(queryset, many=True)
        result=[]
        for i in range(len(serializer.data)):
            result.append(serializer.data[i]['role']) if serializer.data else None
        return result

    class Meta:
        model = Permission
        fields = ("__all__")
        read_only_fields = ("created_time", "modified_time")
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}} 

    # To return forign key values in detail
    def to_representation(self, instance):
        response = super().to_representation(instance)
        
        return response 

class RoleSerializer(serializers.ModelSerializer):
    permissions = serializers.SerializerMethodField()

    def get_permissions(self, obj):
        queryset = RolePermissions.objects.filter(role=obj.id)
        serializer = RolePermissionSerializer(queryset, many=True)
        result=[]
        for i in range(len(serializer.data)):
            result.append(serializer.data[i]['permissions']) if serializer.data else None
        return result

    class Meta:
        model = Role
        fields = ("__all__")
        read_only_fields = ("created_time", "modified_time")
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}} 
    
    # To return forign key values in detail
    def to_representation(self, instance):
        response = super().to_representation(instance)

        return response 

class RolePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolePermissions
        fields = ("__all__")
        depth = 1

class RoleCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleCategories
        fields = ("__all__")

class RoleTerritoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleTerritories
        fields = ("__all__")