import imp
from rest_framework import serializers
from .models import Resume

class ResumeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    address = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    desc = serializers.CharField(max_length=1000)
    schoolname = serializers.CharField(max_length=200)
    subjectname = serializers.CharField(max_length=200)
    skills = serializers.CharField(max_length=200)
    project = serializers.CharField(max_length=200)

class ResumeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    address = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    desc = serializers.CharField(max_length=1000)
    schoolname = serializers.CharField(max_length=200)
    subjectname = serializers.CharField(max_length=200)
    skills = serializers.CharField(max_length=200)
    project = serializers.CharField(max_length=200)
    def create(self,validated_data):
        return Resume.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.email = validated_data.get('email',instance.email)
        instance.desc = validated_data.get('desc',instance.desc)
        instance.schoolname = validated_data.get('schoolname',instance.schoolname)
        instance.subjectname = validated_data.get('subjectname',instance.subjectname)
        instance.skills = validated_data.get('skills',instance.skills)
        instance.project = validated_data.get('project',instance.project)
        instance.save()
        return instance

