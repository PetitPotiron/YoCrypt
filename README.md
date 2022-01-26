# YoCrypt
YoCrypt is a new way to encode and decode text symetrically. It works with a key and is a variation of the [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher).

[How it works](#)
[Implementations](#)

## How it works
### Encoding
The text is encoded/decoded in relation to the key, the first word of the text. 

For each letter of the first word, the algorithm takes its alphabet position.

| h | e | l | l | o |
| - | - | - | -| - |
| 8 | 5 | 12 | 12 | 15 |


Then the algorithm overlays the key on the other words, as below.

```
hello my name is john doe | etc.

hello he lloh el lohe llo | etc.
```

And then it replaces each letter of each word (except the first word which is the key) by the letter located `n` positions **further** in the alphabet (`n` is the position of the superimposed letter).

Below is an example :

```
hello my name is john doe | initial text
hello he lloh el lohe llo | overlayed the key on the text
hello ud zmbm ne vdps pat | moved the letters - this is the encoded text
```

### Decoding
To decode and encoded text, the process is the same. Simply, the letters are moved `n` positions **before** the letter (`n` is the position of the superimposed letter).


```
hello ud zmbm ne vdps pat | this is the encoded and initial text
hello he lloh el lohe llo | overlayed the key on the text
hello my name is john doe | moved the letters - this is the decoded text
```

