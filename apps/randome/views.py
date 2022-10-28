from random import choices
from django.shortcuts import render


def random_string(request):
    if request.method == 'POST':
        length = request.POST['length']
        specials = request.POST['specials']
        digits = request.POST['digits']
        string = [chr(letter) for letter in list(range(65, 91)) + list(range(97, 123))]
        string += [chr(sign) for sign in list(range(33, 48))] if int(specials) else ""
        string += [chr(number) for number in list(range(48, 58))] if int(digits) else ""
        result = "".join(choices(string, k=int(length)))
        return render(request, 'randome/random.html', context={'output_randoms': result})
    else:
        return render(request, 'randome/random.html')
