from rest_framework import serializers
from .models import *

class PostContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = postContent
        fields = ['id','type_of_content','content','order_num']

class PostSerializer(serializers.ModelSerializer):
    content = PostContentSerializer(many=True)
    class Meta:
        model = post
        fields = [
            'id',
            'title',
            'preview_image',
            'category',
            'time_create',
            'slug',
            'content'
            ]
        
class DocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = docs
        fields = (
            'id',
            'name',
            'path',
            'date',
            'type',
            )
        
class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = faq
        fields = (
            'id',
            'question',
            'answer',
            )
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = (
            'id',
            'name',
            'preview_image',
            )

class FormsSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = (
            'id',
            'name',
            'phone',
            'email',
            'message',
            )