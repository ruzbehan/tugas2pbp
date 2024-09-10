from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Sate Pacil',
        'price': 15000,
        'description': 'SATE PALING ENAK SE UI?!!!',
        'quantity' : 5
    }

    return render(request, "main.html", context)