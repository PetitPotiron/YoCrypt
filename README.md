# YoCrypt
YoCrypt is a new way to encode and decode text symetrically. It works with a key and is a variation of the [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher).

* [How it works](#how-it-works)
* * [Encoding](#encoding)
* * [Decoding](#decoding)
* [Implementations](#implementations)
* * [Python](#python)
* * [JavaScript](#javascript)
* * [Rust](#rust)
* [Documentation](https://yocrypt.readthedocs.io)
* [Your rights](#your-rights)

[![Discord server for help](https://discord.com/api/guilds/800032961525317693/embed.png)](https://discord.gg/t2dxrXMKya)

## How it works
The text is encoded and decoded in relation to the key, which is the first word of the text. Thus, the security of your encoded text depends on the length of the first word. If the first word is a single letter, the algorithm is directly the [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher). This algorithm simply applies this method on all the letters of the text, one-by-one.

⚠️ This encoding method does NOT support :
* Uppercase letters
* Non-ASCII letters (These characters will be skipped)

### Encoding
For each letter of the first word, the algorithm takes its alphabet position.

| letter | h | e | l | l | o |
| - | - | - | - | -| - |
| position in the alphabet | 8 | 5 | 12 | 12 | 15 |


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

## Implementations
This algorithm has initially been written in Python, but it is now available in JavaScript and Rust too. These programs use `argv` (command-line passed arguments). However, some libraries has been published to use it in a real program, without knowing what will be encoded/decoded.

### Python
#### Source code
The source code to encode/decode a text with this method is located in [`/src/python/algorithm`](https://github.com/PetitPotiron/YoCrypt/blob/main/src/python/algorithm). There are two files there :  [`encode.py`](https://github.com/PetitPotiron/YoCrypt/blob/main/src/python/algorithm/encode.py)(which encodes a text) and [`decode.py`](https://github.com/PetitPotiron/YoCrypt/blob/main/src/python/algorithm/decode.py) (which decodes a text).

#### Library
The library has been published on [PyPI](https://pypi.org/project/yocrypt), which means it can be downloaded through `pip`. Just run the following command to install it : `python3 -m pip install yocrypt -U` or `python -m pip install yocrypt -U`. Moreover, its source code is available in [`/src/python/library`](https://github.com/PetitPotiron/YoCrypt/blob/main/src/python/library). Here is how you can use it, quickly.

```python
>>> import yocrypt
>>> yocrypt.encode("hello my name is john doe")
'hello ud zmbm ne vdps pat'
>>> yocrypt.decode("hello ud zmbm ne vdps pat")
'hello my name is john doe'
```

You can also specify a key and a text by using keywords arguments :

```python
>>> import yocrypt
>>> yocrypt.encode(key="hello", text="my name is john doe")
'hello ud zmbm ne vdps pat'
>>> yocrypt.decode(key="hello", text="ud zmbm ne vdps pat")
'hello my name is john doe'
```

The complete documentation can be found [here](https://yocrypt.readthedocs.io/python/).

### JavaScript
#### Source code
The source code to encode/decode a text with this method is located in [`/src/javascript/algorithm`](https://github.com/PetitPotiron/YoCrypt/blob/main/src/javascript/algorithm). There are two files there :  [`encode.js`](https://github.com/PetitPotiron/YoCrypt/blob/main/src/javascript/algorithm/encode.js)(which encodes a text) and [`decode.js`](https://github.com/PetitPotiron/YoCrypt/blob/main/src/javascript/algorithm/decode.js) (which decodes a text).

#### Library
The library has been published on [NPMjs](https://pypi.org/project/yocrypt), which means it can be downloaded through `npm`. Just run the following command to install it : `python3 -m pip install yocrypt -U` or `npm i yocrypt`. Moreover, its source code is available in [`/src/javascript/library`](https://github.com/PetitPotiron/YoCrypt/blob/main/src/python/library). Here is how you can use it, quickly.


```javascript
node> let yocrypt = require('yocrypt');
node> yocrypt.encode('hello my name is john doe');
'hello ud zmbm ne vdps pat'
```

```javascript
node> let yocrypt = require('yocrypt')
node> yocrypt.encode("hello my name is john doe")
'hello ud zmbm ne vdps pat'
node> yocrypt.decode("hello ud zmbm ne vdps pat")
'hello my name is john doe'
```

You can also specify a key and a text by using keywords arguments :

```javascript
node> let yocrypt = require('yocrypt');
node> yocrypt.encode(key="hello", text="my name is john doe")
'hello ud zmbm ne vdps pat'
node> yocrypt.decode(key="hello", text="ud zmbm ne vdps pat")
'hello my name is john doe'
```

The complete documentation can be found [here](https://yocrypt.readthedocs.io/javascript/).

### Rust
#### Source code
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam blandit, nibh in ultrices porttitor, magna justo porta enim, id cursus nisi nisi scelerisque urna. Aliquam congue nibh sed facilisis fermentum. In mattis ullamcorper erat, commodo ultricies leo eleifend dignissim. Praesent diam odio, porttitor nec eros ac, tincidunt efficitur ex. Nam ac elementum elit. Duis posuere leo in tortor tincidunt euismod. Fusce turpis neque, pulvinar finibus feugiat sit amet, aliquam sit amet nisl. Curabitur condimentum erat tempus ipsum ultricies, ac vulputate ipsum blandit. Curabitur bibendum lectus sit amet odio blandit, ut aliquam purus iaculis. Vivamus vel aliquam mi.

#### Library
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque pretium lorem risus, nec gravida dui iaculis id. Nunc orci sem, malesuada ultrices blandit a, molestie id eros. Integer ultricies vitae turpis sed maximus. Vivamus malesuada auctor aliquet. Praesent consequat, ligula et consequat volutpat, lectus felis sodales nisi, id porttitor ante nisi eu leo. Nullam vestibulum justo nisl, eu lacinia diam varius quis. Cras vel viverra tortor, sed volutpat justo. Donec quis est turpis. Fusce eleifend semper urna a fermentum. 

The complete documentation can be found [here](https://yocrypt.readthedocs.io/rust/).

## Your rights
This project is licensed under the MIT License. It means you have some permissions, but there are some conditions and limitations too.

### Permissions
* Commercial use
* Modification
* Distribution
* Private use

### Conditions
* Liability
* Warranty

### Limitations
* License and copyright notice

For more information, read the `LICENSE` file located in the root of this repository. Don't worry, it's very fast.
