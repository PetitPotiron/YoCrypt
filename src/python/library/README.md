# YoCrypt algorithm written in Python
YoCrypt is a new way to encode and decode text symetrically. It works with a key and is a variation of the [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher). If you want to know more about YoCrypt, check out the [GitHub](https://github.com/PetitPotiron/YoCrypt).

The files located in this directory implement the YoCrypt algorithm with a Python library.

* [Usage](#usage)
* * [Encoding](#encoding)
* * [Decoding](#decoding)
* [To go further...](#to-go-further)

[![Discord server for help](https://discord.com/api/guilds/800032961525317693/embed.png)](https://discord.gg/t2dxrXMKya)

## Usage
### Encoding
To encode a text using YoCrypt, use the `encode()` method from the library :

```python
>>> import yocrypt
>>> yocrypt.encode('hello my name is john doe')
'hello ud zmbm ne vdps pat'
```

### Decoding
To encode a text using YoCrypt, use the `decode()` method from the library :

```python
>>> import yocrypt
>>> yocrypt.decode('hello ud zmbm ne vdps pat')
'hello my name is john doe'
```

## To go further...
If you want to go further through the uses of the library, take a look at the [documentation](https://yocrypt.readthedocs.io). You can also check out the [GitHub](https://github.com/PetitPotiron/YoCrypt).