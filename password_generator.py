#password generator
import random
import string

def generate_password(length=12):
    """Génère un mot de passe sécurisé avec lettres, chiffres et caractères spéciaux."""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    try:
        length = int(input("Entrez la longueur du mot de passe : "))
        print("🔑 Mot de passe généré :", generate_password(length))
    except ValueError:
        print("❌ Veuillez entrer un nombre valide.")
