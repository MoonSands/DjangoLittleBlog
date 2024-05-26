from rest_framework import serializers
from .models import *
from django.conf import settings

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = postCategory
        fields = '__all__'

#class PostContentSerializer(serializers.ModelSerializer):
 #   class Meta:
 #       model = postContent
 #       fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(many=False, queryset=postCategory.objects.all())

    class Meta:
        model = post
        fields = ['id', 'title', 'preview_image', 'category', 'content', 'time_create', 'slug']

        
class DocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = docs
        fields = '__all__'

class ReportGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = reportsGroup
        fields = '__all__'
    
class ReportsSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(many=False, queryset=reportsGroup.objects.all())
    class Meta:
        model = reports
        fields = ['id', 'name', 'date', 'file', 'group']

        def get_group(self, obj):
            group = obj.group
            if group:
                serializer = ReportGroupSerializer(group)
                return serializer.data
            return None
        
        
class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = faq
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = '__all__'

class FormsSerializer(serializers.ModelSerializer):
    class Meta:
        model = dataFromForms
        fields = '__all__'