import sys, string

text = sys.argv[1]
key = sys.argv[1].split()[0]
result = list(text)
key_text = []

while len(key_text) < len(text):
    key_text.append(key)
    
key_text = list("".join(key_text))

for i, letter in enumerate(text):
    if letter in string.ascii_lowercase: continue
    key_text.insert(i, letter)

key_text = key_text[:len(text)]

for i, letter in enumerate(key_text):
    if not letter in string.ascii_lowercase: continue
    if not result[i] in string.ascii_lowercase: continue
    a = string.ascii_lowercase.index(result[i])-string.ascii_lowercase.index(letter)-1
    while a >= 26:
        a -= 26
    result[i] = string.ascii_lowercase[a]

print(key + " " + "".join(result[len(key)+1:]))
