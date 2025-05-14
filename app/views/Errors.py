from django.shortcuts import render

# custom 404 view
def custom_404(request, exception):
    return render(request, 'errors/404.html', status=404)


# custom 500 view
def custom_500(request):
    return render(request, 'errors/500.html', status=500)