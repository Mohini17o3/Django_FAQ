from django.forms import model_to_dict
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


def postFaqs(request):
    
    if request.method == "POST":
         question = request.POST.get('question')
         language = request.POST.get('language' , 'en')

         if not question :
             return JsonResponse({"error": "Question and answer are required"}, status=400)

         newFAQ =FAQ.objects.create(
          question = question , 
          language = language)
     

         if request.headers.get('Accept') == 'application/json' :
            return JsonResponse({'dataset' : {
               'question' : newFAQ.question , 
               'language' : newFAQ.language
          } })

         return render(request, "post_faq_view.html", {"success": "FAQ successfully added!"})

    return render(request, "post_faq_view.html")






