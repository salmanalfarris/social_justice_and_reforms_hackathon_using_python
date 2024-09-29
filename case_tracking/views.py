from django.shortcuts import render
from .models import CourtCase
# Create your views here.

def case_list(request):
    cases = CourtCase.objects.filter(user=request.user)
    return render(request, 'case_tracking/case_list.html', {'cases': cases})

def case_detail(request, case_id):
    case = CourtCase.objects.get(id=case_id)
    return render(request, 'case_tracking/case_detail.html', {'case': case})