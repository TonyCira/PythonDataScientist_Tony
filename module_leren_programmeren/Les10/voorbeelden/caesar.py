def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    # Als we willen ontcijferen, draaien we de verschuiving om
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        # Versleutel hoofdletters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Versleutel kleine letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Laat leestekens en spaties ongewijzigd
        else:
            result += char

    return result


# --- VOORBEELD GEBRUIK ---
originele_tekst = "Hallo Wereld!"
verschuiving = 3

# 1. Versleutelen
geheime_tekst = caesar_cipher(originele_tekst, verschuiving, mode='encrypt')
print(f"Origineel: {originele_tekst}")
print(f"Versleuteld (geheim): {geheime_tekst}")

# 2. Ontcijferen
ontcijferde_tekst = caesar_cipher(geheime_tekst, verschuiving, mode='decrypt')
print(f"Ontcijferd: {ontcijferde_tekst}")
