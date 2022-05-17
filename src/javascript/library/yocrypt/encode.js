module.exports = function (text, key = null) {
    const letters = "abcdefghijklmnopqrstuvwxyz";
    if (key == null) {
        key = text.split(' ')[0];
    }
    let result = text.split('');
    let key_text = [];

    while (key_text.length < result.length) {
        key_text.push(key);
    }

    key_text = key_text.join("").split('');
    for (const [i, letter] of text.split('').entries()) {
        if (letters.includes(letter)) {
            continue;
        }
        key_text.splice(i, 0, letter);
    }

    key_text = key_text.slice(0, text.length);

    for (const [i, letter] of key_text.entries()) {
        if (!letters.includes(letter)) {
            continue;
        }
        if (!letters.includes(result[i])) {
            continue;
        }
        let a = letters.indexOf(result[i]) + letters.indexOf(letter) + 1;
        while (a >= 26) {
            a -= 26;
        }
        result[i] = letters[a]
    }

    return key + " " + result.slice(key.length + 1).join("");
}