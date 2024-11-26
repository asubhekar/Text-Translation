from rest_framework import serializers

class TranslationRequestS(serializers.Serializer):
    text = serializers.CharField(max_length = 500)
    target = serializers.CharField(max_length = 10)

class TranslationResponseS(serializers.Serializer):
    translated_text = serializers.CharField(max_length = 500)