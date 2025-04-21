from django.shortcuts import render
from django.shortcuts import HttpResponse
from .serializers import TranslationRequestS, TranslationResponseS
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .text_text_translation import App
from langdetect import detect


class translation(APIView):
    def post(self, request):
        
        req = TranslationRequestS(data = request.data)
        print(req)
        if req.is_valid():
            input = req.data['text']
            selected_lang = req.data['target']
    
            model = App(input,lang2 = selected_lang)
            print(input)
            translated_text = model.translate()
            print(translated_text)
            response_serializer = TranslationResponseS({'translated_text': translated_text})
        return Response(response_serializer.data, status = status.HTTP_200_OK)
        
# Create your views here.
def home(request):
    return render(request, 'translationapp/index.html')