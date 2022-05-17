# YoCrypt algorithm written in Python
YoCrypt is a new way to encode and decode text symetrically. It works with a key and is a variation of the [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher). If you want to know more about YoCrypt, check out the [GitHub](https://github.com/PetitPotiron/YoCrypt).

The files located in this directory implement the YoCrypt algorithm in Python. Note that their usage only works with `argv` (command-line passed arguments) as described below.

* [Usage](#usage)
* * [Encoding](#encoding)
* * [Decoding](#decoding)
* [To go further...](#to-go-further)

[![Discord server for help](https://discord.com/api/guilds/800032961525317693/embed.png)](https://discord.gg/t2dxrXMKya)

## Usage
### Encoding
To encode a text using YoCrypt, run the `encode.py` file located in this directory, and pass the text to encode via `argv` :

```
user@computer:~ $ python3 encode.py "hello my name is john doe"
hello ud zmbm ne vdps pat
```

### Decoding
To decode a text using YoCrypt, run the `decode.py` file located in this directory, and pass the text to decode via `argv` :

```
user@computer:~ $ python3 decode.py "hello ud zmbm ne vdps pat"
hello my name is john doe
```

## To go further...
If you want to go further through the uses of the algorithm, take a look at the **library** ([on GitHub](httos://github.com/PetitPotiron/YoCrypt/src/python/library) and [on PyPI](https://pypi.org/project/yocrypt)) and the [documentation](https://yocrypt.readthedocs.io). You can also check out the [GitHub](https://github.com/PetitPotiron/YoCrypt).