from django.shortcuts import render
from django.http import JsonResponse
from login.models import Member
from login.forms import MemberForm
from django.utils import timezone


def save(request): 
    try:
        memberForm= MemberForm(request.POST)
        member=memberForm.save(commit=False)
        member.wdate=timezone.now()
        member.save()
        result = {'result':'success'}
    except Exception as ex:
        print('실패했습니다',ex)
        result= {'result':'fail'}
    
    return JsonResponse(result)

# Create your views here.
