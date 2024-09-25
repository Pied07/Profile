from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def home(request):
    return render(request,'home.html')

def download_resume(request):
    try:
        url = f"https://res.cloudinary.com/dbgvwyhdr/raw/upload/v1727232856/uhyh17rllmgo6z64wiff.pdf"
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="Sandipan_Adhikary_Resume.pdf"'
        response.write(requests.get(url).content)
        return response
    except Exception as e:
        return HttpResponse(f"Error Downloading file: {e}",status=500)
