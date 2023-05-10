from django.shortcuts import render
from .utils import summarize_text  # Asume que tienes una función que resume texto en utils.py

def summarize(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        summary = summarize_text(text)
        return render(request, 'summarizer_app/summary.html', {'summary': summary})
    return render(request, 'summarizer_app/summarize.html')

def summary(request):
    return render(request, 'summarizer_app/summary.html')
