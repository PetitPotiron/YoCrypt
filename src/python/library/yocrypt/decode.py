import string


def decode(text, **kwargs):
    text = text
    key = text.split()[0]
    for identifier, value in kwargs.items():
        if identifier == "key":
            key = value
            text = value + " " + text

    result = list(text)
    key_text = []

    while len(key_text) < len(text):
        key_text.append(key)

    key_text = list("".join(key_text))

    for i, letter in enumerate(text):
        if letter in string.ascii_lowercase:
            continue
        key_text.insert(i, letter)

    key_text = key_text[:len(text)]

    for i, letter in enumerate(key_text):
        if not letter in string.ascii_lowercase:
            continue
        if not result[i] in string.ascii_lowercase:
            continue
        a = string.ascii_lowercase.index(
            result[i])-string.ascii_lowercase.index(letter)-1
        while a >= 26:
            a -= 26
        result[i] = string.ascii_lowercase[a]

    return key + " " + "".join(result[len(key)+1:])
