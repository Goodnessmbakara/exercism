def rotate_character(char, key):
    # Check if the character is a letter
    if char.isalpha():
        # Determine whether it's uppercase or lowercase
        offset = ord('A') if char.isupper() else ord('a')
        # Apply the rotation and wrap around if necessary
        return chr((ord(char) - offset + key) % 26 + offset)
    else:
        # If the character is not a letter, leave it unchanged
        return char

def rotate_string(input_str, key):
    # Rotate each character in the string
    rotated_str = ''.join(rotate_character(char, key) for char in input_str)
    return rotated_str

# Example usage with ROT13
plaintext = "abcdefghijklmnopqrstuvwxyz"
key = 13
ciphertext = rotate_string(plaintext, key)
