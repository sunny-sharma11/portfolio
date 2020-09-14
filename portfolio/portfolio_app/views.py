from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    objs = Home.objects.all()
    tags = Tags.objects.all()
    sliders = Slider.objects.all()

    return render(request, 'index.html', {'objs': objs, 'tags': tags, 'sliders': sliders})


def resume(request):
    res_intro = Resume_intro.objects.all()
    res_ser = Resume_services.objects.all()
    res_exp = Resume_experience.objects.all()
    res_edu = Resume_education.objects.all()
    res_lan = Resume_language_skill.objects.all()
    res_skill = Resume_coding_skill.objects.all()
    res_knw = Resume_knowledge.objects.all()
    res_intr = Resume_interests.objects.all()
    testi = Testimonials.objects.all()
    clients = Client_logos.objects.all()
    custom_text = Custom_text.objects.all()

    return render(request, 'resume.html', {'res_intro': res_intro, 'res_ser': res_ser,
                                           'res_exp': res_exp, 'res_edu': res_edu, 'res_lan': res_lan,
                                           'res_skill': res_skill,
                                           'res_knw': res_knw, 'res_intr': res_intr, 'testi': testi, 'clients': clients,
                                           'custom_text': custom_text})


def work(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'works.html', {'portfolios': portfolios})


def contact(request):
    detail = Contact_detail.objects.all()
    return render(request, 'contacts.html', {'detail': detail})
