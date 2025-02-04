import pytest
from django.urls import reverse
from faqs.models import FAQ
from django.test import Client
import json



#- test get endpoint in get_faqs views o check if we are getting faqs in json
#- similarly test post faq  , check count for creation of new faq
#- test if empty faq post causes error , for it being invalid
#- test if cache is working for getting the faqs 



@pytest.mark.django_db
def test_get_faqs():

    FAQ.objects.create(question="What is Django?", language="en")
    
    client =  Client()
    response = client.get(reverse("get_faqs"), HTTP_ACCEPT='application/json')

    assert response.status_code == 200
    assert "dataset" in response.json()

@pytest.mark.django_db
def test_post_faq():
    client = Client()
    data = {"question": "What is Django?", "language": "en"}
    response = client.post(reverse("post_faqs"), data=data , HTTP_ACCEPT="application/json")

    assert response.status_code == 200
    assert FAQ.objects.count() == 1






