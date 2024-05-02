from django.core.exceptions import ValidationError

def validate_login(data):
    login = data['login'].strip()

    if not login:
        raise ValidationError('choose another username')
    
    return True

def validate_password(data):
    password = data['password'].strip()

    if not password:
        raise ValidationError('a password is needed')
    
    return True