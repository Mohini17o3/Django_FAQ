import pytest
from faqs.models import FAQ , TranslatedFAQ
from django.core.exceptions import ValidationError


# TESTS TO BE DONE
# - test faq model for creation on an entry 
# - test TranslatedFAQ model for creation of an entry
# - check get_translated_question method if it return translation
# - check get_translated_question if it returns original question if no translation
# -  test cascading , if FAQ field deletion causes deletion in Translated_FAQ


@pytest.mark.django_db
def test_create_faq():
    faq = FAQ.objects.create(question = "What is pytest ?" , language = "en")
    assert faq.question == "What is pytest ?"
    assert faq.language == "en"

@pytest.mark.django_db
def test_create_translated_faq():
    faq = FAQ.objects.create(question="What is pytest?", language="en")
    translated_faq = TranslatedFAQ.objects.create(
        translatedFaqs=faq, question="¿Qué es pytest?", language="es"
    )
    assert translated_faq.translatedFaqs == faq
    assert translated_faq.question == "¿Qué es pytest?"
    assert translated_faq.language == "es"

@pytest.mark.django_db
def test_translation_method():

    faq = FAQ.objects.create(question="What is pytest?", language="en")
    TranslatedFAQ.objects.create(
        translatedFaqs=faq, question="¿Qué es pytest?", language="es"
    )

    translated_question = faq.get_translated_question("es")
    assert translated_question == {'question': '¿Qué es pytest?', 'answer': ''}

@pytest.mark.django_db
def test_translation_not_found():

    faq = FAQ.objects.create(question="What is pytest?", language="en")
    
    translated_question = faq.get_translated_question("fr")  
    assert translated_question == {'question': "Qu'est-ce que Pytest?", 'answer': 'No answer available.'}


@pytest.mark.django_db
def test_faq_deletion_cascades():
  
    faq = FAQ.objects.create(question="What is pytest?", language="en")
    TranslatedFAQ.objects.create(
        translatedFaqs=faq, question="¿Qué es pytest?", language="es"
    )

    faq.delete()
    
    assert TranslatedFAQ.objects.count() == 0 



@pytest.mark.django_db
def test_cache_works(mocker):
    mock_cache_get = mocker.patch("django.core.cache.cache.get")
    mock_cache_set = mocker.patch("django.core.cache.cache.set")

    faq = FAQ.objects.create(question="What is Django?", language="en")

    mock_cache_get.return_value = None  
    faq.get_translated_question("es") 

    assert mock_cache_set.called

    mock_cache_get.return_value = {"question": "¿Qué es Django?", "answer": "Descripción de Django"}
    translated_question = faq.get_translated_question("es")

    assert mock_cache_get.called

    assert translated_question["question"] == "¿Qué es Django?"
    assert translated_question["answer"] == "Descripción de Django"







