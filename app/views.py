from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def transliterate(request):
    if request.method == 'POST':
        inputText = request.POST['inputText']
        outputText = ""

        transcriptions = {
            "А": "A",
            "Б": "B",
            "В": "V",
            "Г": "G",
            "Д": "D",
            "Е": "YE",
            "Ё": "YO",
            "Ж": "ZH",
            "З": "Z",
            "И": "I",
            "Й": "Y",
            "К": "K",
            "Л": "L",
            "М": "M",
            "Н": "N",
            "О": "O",
            "П": "P",
            "Р": "R",
            "С": "S",
            "Т": "T",
            "У": "U",
            "Ф": "F",
            "Х": "H",
            "Ц": "TS",
            "Ч": "CH",
            "Ш": "SH",
            "Щ": "SHCH",
            "Ъ": "",
            "Ы": "Y",
            "Ь": "\'",
            "Э": "E",
            "Ю": "YU",
            "Я": "YA",
        }

        # for each char in text, convert
        for char in inputText:
            outputText += transcriptions[char]

        # inputText is being used for testing; temporary
        return render(request, 'result.html', {'outputText': outputText})
