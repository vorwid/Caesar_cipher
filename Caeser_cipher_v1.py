alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar_cipher(direction, text, shift):
  if direction == "encode":
    cipher_text = ""
    for letter in text:
      position = alphabet.index(letter)
      new_position = position + shift
      cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")
  elif direction == "decode":
    decoded_text = ""
    for letter in text:
      position = alphabet.index(letter)
      new_position = position - shift
      decoded_text += alphabet[new_position]
    print(f"The decoded text is {decoded_text}")

caesar_cipher(direction, text, shift)





