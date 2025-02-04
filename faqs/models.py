from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache
# Create your models here.


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = RichTextField()
    language = models.CharField(max_length=20 , default = 'en')

  
    
    def get_translated_question(self , language='en'):
        cache_key = f"faq_translation_{self.id}_{language}" 
        cache_translation = cache.get(cache_key)

        if cache_translation : 
            print(f"cache hit ! , using cached translation for {self.question} in {language}")
            return cache_translation

        print("cache miss ")
        translation = TranslatedFAQ.objects.filter(translatedFaqs=self, language=language).first()
        
        if translation:
               print(f"Using existing translation for {self.question} in {language}")
               cache_translation = {'question':translation.question , 'answer' :translation.answer}
               cache.set(cache_key , cache_translation , timeout= 864000)
               return cache_translation
        
        
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
              

              cache_translation = {'question' : translated_question , 'answer' : translated_answer }

              cache.set(cache_key ,cache_translation ,timeout=86400)              
              
              print(f"New translation saved: {new_translation.question} ({new_translation.language})")

              return cache_translation

    def __str__(self):
        return self.question


class TranslatedFAQ(models.Model):
    translatedFaqs = models.ForeignKey(FAQ , on_delete=models.CASCADE , related_name='translations')
    question = models.CharField(max_length=255)
    language = models.CharField(max_length=10)
    answer = RichTextField()


    class Meta :
        unique_together = ('translatedFaqs' , 'language')


    def __str__(self):
        return f"{self.translatedFaqs.question} ({self.language})"

    

