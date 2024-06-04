from django.shortcuts import render
from .models import Lead

from django.http import HttpResponse

from .forms import LeadForm


def lead_list(request):
    leads = Lead.objects.all()

    context = {
        'leads':leads
    }
    return render(request, "leads/lead-list.html", context)


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead":lead
    }    
    return render(request, "leads/lead-detail.html", context)


def lead_create(request):
    print(request.POST)
    context = {
        "form": LeadForm()
    }
    return render(request, "leads/lead-create.html", context) 