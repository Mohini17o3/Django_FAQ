from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
# Create your models here.

translator = Translator()

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = RichTextField()

    
    def get_translated_question(self , language='en'):
        translation = self.translations.filter(language=language).first()
        if translation:
            return {'question':translation.question, 'answer':translation.answer}
        
        else :
             translated_question = translator.translate(self.question , src='en' , dest=language).text
             translated_answer = translator.translate(self.answer , src='en' , dest=language).text

             TranslatedFAQ.objects.create(
                 translatedFaqs = self,
                 language = language, 
                 question = translated_question, 
                 answer = translated_answer 
             )

             return {'question' :translated_question , 'answer':translated_answer}

    def __str__(self):
        return self.question


class TranslatedFAQ(models.Model):
    translatedFaqs = models.ForeignKey(FAQ , on_delete=models.CASCADE , related_name='translations')
    language = models.CharField(max_length=10)
    question = models.CharField(max_length=255)
    answer = RichTextField()


    def __str__(self):
        return f"{self.translatedFaqs.question} ({self.language})"

    

