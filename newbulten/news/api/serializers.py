from rest_framework import serializers
from news.models import Article
 
# Makale Serializer 
class ArticleSerializer(serializers.Serializer):
    id= serializers.IntegerField(read_only=True)  # Otomatik olarak atanacak, sadece okunabilir bir alan
    author = serializers.CharField()  # Yazar ismini tutan karakter alanı
    title = serializers.CharField()  # Başlığı tutan karakter alanı
    description = serializers.CharField()  # Açıklamayı tutan karakter alanı
    text = serializers.CharField()  # Makale metnini tutan karakter alanı
    city = serializers.CharField()  # Şehir bilgisini tutan karakter alanı
    published_date=serializers.DateField()  # Yayınlanma tarihini tutan tarih alanı
    isActive = serializers.BooleanField()  # Makalenin aktif olup olmadığını tutan boolean alanı
    created_date = serializers.DateTimeField(read_only=True)  # Oluşturulma tarihini tutan ve sadece okunabilir bir alan
    updated_date = serializers.DateTimeField(read_only=True)  # Güncellenme tarihini tutan ve sadece okunabilir bir alan

    def create(self, validated_data):
        # validated_data içindeki verileri kullanarak yeni bir Article nesnesi oluşturur
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Mevcut bir Article nesnesini, validated_data içindeki verilerle günceller
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.text = validated_data.get('text', instance.text)
        instance.city = validated_data.get('city', instance.city)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.isActive = validated_data.get('isActive', instance.isActive)
        instance.save()
        return instance

def validate(self,data):
   
    raise serializers.ValidationError('Title and description can not be same')
    return data

def validate_title(self,value):
    if len(value) < 20:
        raise serializers.ValidationError('Title space must minumum 20 character')

    return value