# YoCrypt
YoCrypt is a new way to encode and decode text symetrically. It works with a key and is a variation of the [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher).

* [How it works](#how-it-works)
* * [Encoding](#encoding)
* * [Decoding](#decoding)
* [Implementations](#implementations)
* * [Python](#python)
* * [JavaScript](#javascript)
* * [Rust](#rust)
* * [Documentation](https://yocrypt.readthedocs.io)
* [Your rights](#your-rights)

## How it works
The text is encoded/decoded in relation to the key, which is the first word of the text. Thus, the security of your encoded text depends on the length of the first word. If the first word is a single letter, the algorithm is directly the [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher). This algorithm simply applies this method on all the letters of the text, one-by-one.

### Encoding
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

## Implementations
This algorithm has initially been written in Python, but it is now available in JavaScript and Rust too. These programs use `argv` (command-line passed arguments), however, some libraries has been published to use it in a real program, without knowing what will be encoded/decoded.

### Python
#### Source code
The source code to encode/decode a text with this method is located in `/src/python`. There are two files there : `encode.py` (which encodes a text) and `decode.py` (which decodes a text).

#### Library
The library has been published on [PyPI](https://pypi.org/project/yocrypt), which means it can be downloaded through `pip`. Just run the following command : `python3 -m pip install yocrypt -U` or `python -m pip install yocrypt -U`. Here is how you can use it, quickly.

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

The complete documentation can be found [here](https://yocrypt.readthedocs.io/python/)

### JavaScript
#### Source code
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum rhoncus metus urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Suspendisse bibendum odio tellus, et consectetur neque accumsan sed. Ut fringilla ipsum justo, sit amet lacinia enim posuere eget. Fusce consequat eleifend laoreet. Nulla vitae nunc egestas nisi interdum feugiat. Mauris venenatis eros in facilisis tristique. Suspendisse tincidunt molestie nisl sed dignissim. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Donec posuere maximus orci quis interdum. Proin congue mauris suscipit metus sodales ultricies. Nam ut fringilla orci. Vivamus ac augue vitae dolor venenatis feugiat. 

#### Library
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ultrices nibh ac porttitor aliquam. Etiam vel porta enim, nec sollicitudin est. Morbi nec sem erat. Vestibulum at elit ut enim vestibulum aliquam. Phasellus dictum pharetra mauris non porttitor. Aenean tempor eros vitae sem vehicula, ut sollicitudin lacus gravida. Etiam libero urna, lobortis id tortor et, rutrum convallis eros. Aenean purus tellus, sodales id pellentesque a, aliquet non tortor. Integer nulla est, dapibus eu iaculis nec, eleifend at quam. Aliquam ut elit lectus. Nam placerat magna nec mauris venenatis tempor. Ut aliquam lorem id ipsum pretium, in scelerisque sem sollicitudin. Suspendisse in risus sed velit mattis euismod ut efficitur tellus. Nam diam sem, porttitor quis rhoncus fringilla, tempus non lacus. 

The complete documentation can be found [here](https://yocrypt.readthedocs.io/javascript/)

### Rust
#### Source code
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam blandit, nibh in ultrices porttitor, magna justo porta enim, id cursus nisi nisi scelerisque urna. Aliquam congue nibh sed facilisis fermentum. In mattis ullamcorper erat, commodo ultricies leo eleifend dignissim. Praesent diam odio, porttitor nec eros ac, tincidunt efficitur ex. Nam ac elementum elit. Duis posuere leo in tortor tincidunt euismod. Fusce turpis neque, pulvinar finibus feugiat sit amet, aliquam sit amet nisl. Curabitur condimentum erat tempus ipsum ultricies, ac vulputate ipsum blandit. Curabitur bibendum lectus sit amet odio blandit, ut aliquam purus iaculis. Vivamus vel aliquam mi.

#### Library
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque pretium lorem risus, nec gravida dui iaculis id. Nunc orci sem, malesuada ultrices blandit a, molestie id eros. Integer ultricies vitae turpis sed maximus. Vivamus malesuada auctor aliquet. Praesent consequat, ligula et consequat volutpat, lectus felis sodales nisi, id porttitor ante nisi eu leo. Nullam vestibulum justo nisl, eu lacinia diam varius quis. Cras vel viverra tortor, sed volutpat justo. Donec quis est turpis. Fusce eleifend semper urna a fermentum. 

The complete documentation can be found [here](https://yocrypt.readthedocs.io/rust/)

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
*

For more information, read the `LICENSE` file located in the root of this repository. Don't worry, it's very fast.
