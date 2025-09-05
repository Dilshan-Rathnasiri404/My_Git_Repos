# T9-style bidirectional translator (interactive, with sentences)

mapping = {
    "a": "2",    "b": "22",   "c": "222",
    "d": "3",    "e": "33",   "f": "333",
    "g": "4",    "h": "44",   "i": "444",
    "j": "5",    "k": "55",   "l": "555",
    "m": "6",    "n": "66",   "o": "666",
    "p": "7",    "q": "77",   "r": "777",  "s": "7777",
    "t": "8",    "u": "88",   "v": "888",
    "w": "9",    "x": "99",   "y": "999",  "z": "9999"
}

reverse_mapping = {v: k for k, v in mapping.items()}


def encode(text: str) -> str:
    text = text.lower()
    result = []
    prev_digit = ""
    for ch in text:
        if ch == " ":
            result.append("0")
            prev_digit = ""
        elif ch == ".":
            result.append("00")
            prev_digit = ""
        elif ch in mapping:
            code = mapping[ch]
            if prev_digit and code[0] == prev_digit:
                result.append(".")
            result.append(code)
            prev_digit = code[0]
        else:
            result.append(ch)  # unknown symbols kept
            prev_digit = ""
    return "".join(result)


def decode(code: str) -> str:
    result = []
    i = 0
    while i < len(code):
        if code[i] == ".":
            i += 1  # just a separator, skip
            continue
        if code[i:i+2] == "00":
            result.append(".")
            i += 2
            continue
        if code[i] == "0":
            result.append(" ")
            i += 1
            continue

        # collect a digit run
        j = i
        while j < len(code) and code[j] not in ".0":
            j += 1
        seg = code[i:j]

        pos = 0
        while pos < len(seg):
            matched = False
            for l in range(len(seg) - pos, 0, -1):  # longest match first
                pref = seg[pos:pos + l]
                if pref in reverse_mapping:
                    result.append(reverse_mapping[pref])
                    pos += l
                    matched = True
                    break
            if not matched:
                result.append("?")
                pos += 1
        i = j
    return "".join(result)


def main():
    choice = input("To Inside? Or Outside? (Enter I or O): ").strip().lower()
    if choice == "i":
        plain = input("Enter the plaintext: ")
        cipher = encode(plain)
        print("Cipher:", cipher)
    elif choice == "o":
        cipher = input("Enter the cipher: ")
        plain = decode(cipher)
        print("Plaintext:", plain)
    else:
        print("Invalid choice. Please enter I or O.")


if __name__ == "__main__":
    # demo
    # print(encode("hi bro."))
    # print(decode("44.4440.22777666000"))
    main()
