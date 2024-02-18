import random
import string

def generate_password(length=12):
    """Belirtilen uzunlukta rastgele bir şifre oluşturur."""
    password_characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(password_characters) for i in range(length))
    return password

password = generate_password()
print("Oluşturulan Şifre: ", password)
