import string

alphabet = list(string.ascii_lowercase)

def adjusted_modulo(n, m):
    return ((n % m) + m) % m

def transform_text(text, pad):
    return ''.join(transform_letter(letter, pad) for letter in text)

def transform_letter(letter, pad):
    index = alphabet.index(letter) if letter in alphabet else -1

    if index != -1:
        new_index = adjusted_modulo(index + pad, len(alphabet))
        return alphabet[new_index]

    return letter

def is_token_valid(token):
    return transform_text(token, 5) == 'zxj dtzw ijgzlljw ;)'
