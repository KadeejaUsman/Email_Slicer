from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


# Create your views here.
def extract_info(email):
    try:
        validate_email(email)
        username, domain = email.split('@')
        return username, domain
    except ValidationError:
        return None, None

def slice(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        username, domain = extract_info(email)
        if username and domain:
            message = f'Hai! Your Username is  {username} & Your domain is {domain}.'
        else:
            message = 'Invalid email address. Please try again.'
        return render(request, 'slice.html', {'message': message})
    return render(request, 'slice.html', {'message':None})
