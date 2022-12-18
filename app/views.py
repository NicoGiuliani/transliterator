from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def transliterate(request):
    if request.method == 'POST':
        inputText = request.POST['inputText']

        # inputText is being used for testing; temporary
        return render(request, 'result.html', {'outputText': inputText})
