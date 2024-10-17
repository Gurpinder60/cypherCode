alphabet = ["a", "b", "c", "d","e","f","g","h", "i", "j", "k", "l", "m","n", "o","p","q","r","s", "t", "u", "v", "w", "x", " y", "z"]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type the message:\n").lower()
shift = int(input("type the shift number:\n"))

def encrypt (original_text, shift_amount):
        cypher_text = ""
        for letter in original_text:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cypher_text += alphabet[shifted_position]
        print(f"Here is the encoded result: {cypher_text}")
encrypt(original_text=text, shift_amount=shift)


def decrypt(original_text, shift_amount):
    decode_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        decode_text += alphabet[shifted_position]
    print(f"Here is the decoded result: {decode_text}")


decrypt(original_text=text, shift_amount=shift)
