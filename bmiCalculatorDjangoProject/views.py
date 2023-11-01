from django.shortcuts import render


def home(request):
    if request.method == 'POST':
        name = request.POST.get('jina')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        result = int(weight) / (float(height) * float(height))
        context = {
            'name': name,
            'result': result
        }
        return render(request, 'index.html', context)

    return render(request, 'index.html')
