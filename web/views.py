# notes/views.py
from .utils import get_website_info
from django.shortcuts import render
from .models import PerformanceAnalysis

def analysis_results(request):
    analyses = PerformanceAnalysis.objects.all()
    return render(request, 'analysis_results.html', {'analyses': analyses})




# web/views.py

from django.shortcuts import render, redirect
from .forms import AnalysisForm
from .models import PerformanceAnalysis
from .utils import get_website_info
from .utils import extract_meta_info

def analyze_performance(request):
    if request.method == 'POST':
        form = AnalysisForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            
            
            # Utilizează funcția definită într-un modul separat pentru a obține informații despre site
            analysis_result = get_website_info(url)
            meta_info = extract_meta_info(url)
            if meta_info:
                title = meta_info['title']
                description = meta_info['description']
                image_url = meta_info.get('image_url', None)
            else:
                title = description = image_url = None

            # Verifică dacă cheia 'error' există în dicționarul analysis_result
            if 'error' in analysis_result:
                # Gestionarea cazului în care apare o eroare
                error_message = analysis_result['error']
                return render(request, 'error_page.html', {'error_message': error_message})

            # Creează un obiect PerformanceAnalysis
            analysis = PerformanceAnalysis.objects.create(
                url=url,
                bytes_received=analysis_result.get('bytes_received', 0),
                content_displayed=analysis_result.get('content_displayed', ''),
                server_response_time=analysis_result.get('server_response_time', 0),
                ip_address=analysis_result.get('ip_address', ''),title=title,
                description=description,image_url=image_url,  # Adaugă adresa IP
                # Alte câmpuri
            )

            return redirect('analysis_results')
    else:
        form = AnalysisForm()

    return render(request, 'analyze_performance.html', {'form': form})
