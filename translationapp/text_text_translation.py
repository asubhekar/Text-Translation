# -*- coding: utf-8 -*-
"""text-text-translation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p5qGxS58S7hpr-aHC1jGiquXHcMFNR9y
"""



import torch
#from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline, AutoProcessor
from langdetect import detect

class App:
  def __init__(self, text, lang2: str = "es"):
    # Initializing application with translation model
    self.lang1 = detect(text)
    self.text = text
    self.lang2 = lang2

    self.translated_text = self.text_to_text(self.text, self.lang1, self.lang2)

  def text_to_text(self, text, lang1, lang2):
    # Initializing the model
    translation_model = f'Helsinki-NLP/opus-mt-{lang1}-{lang2}'

    translation_pipeline = pipeline("translation", model = translation_model, clean_up_tokenization_spaces = True, device=0 if torch.cuda.is_available() else -1)

    return translation_pipeline(text)[0]["translation_text"]

  def translate(self):
    return self.translated_text


