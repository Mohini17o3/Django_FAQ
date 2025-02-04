from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

# Create your models here.


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = RichTextField()
    language = models.CharField(max_length=20 , default = 'en')

  
    
    def get_translated_question(self , language='en'):
        translation = TranslatedFAQ.objects.filter(translatedFaqs=self, language=language).first()
        
        if translation:
               print(f"Using existing translation for {self.question} in {language}")
               return {'question':translation.question, 'answer':translation.answer}
        
        else :
              translator = Translator()

              translated_question = translator.translate(self.question, src='en', dest=language).text
              if self.answer:
                translated_answer = translator.translate(self.answer, src='en', dest=language).text
              else:
                  translated_answer = 'No answer available.'  

              new_translation =TranslatedFAQ.objects.create(
                 translatedFaqs = self,
                 language = language, 
                 question = translated_question, 
                 answer = translated_answer     
             )
              
              print(f"New translation saved: {new_translation.question} ({new_translation.language})")

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

    

