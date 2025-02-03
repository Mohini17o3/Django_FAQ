from django.shortcuts import render
from django.http import JsonResponse
from .models import FAQ
# Create your views here.



def getFaqs(request):
    lang = request.GET.get('lang' , None)

    if not lang:
         other_lang = request.GET.get('other_lang' , '').lower()
         lang = other_lang if other_lang else 'en'

    if not lang :
         lang = 'en'     
    
    faqs= FAQ.objects.all()

    faq_data = []

    for faq in faqs :
            translated_question = faq.get_translated_question(language = lang)
            faq_data.append({
                'question': translated_question['question'] ,
                'answer': translated_question['answer'] ,
            })

    if request.headers.get('Accept') == 'application/json' :
        return JsonResponse({'dataset' : faq_data })    
        
    else :
         return render(request , "faq_view.html" ,{'dataset':faq_data})  


# def postFaqs(request):

#     if request.method == "POST":
#        FAQ.objects.create(question = request.question , answer = request.answer)



