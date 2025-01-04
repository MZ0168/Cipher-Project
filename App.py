

import streamlit as st

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]

    return encrypted_text

# Streamlit app layout
st.title("Muhammed's Cipher App")
st.write("Encrypt and Decrypt your text using the Caesar cipher.")
st.write("This app will encrypt/decrypt you words, sentences and even paragraphs using the ceaser cipher program. You can also decrypt a word if you know its value that it was encrypted with by putting it in negative.")

# Input for plain text
text = st.text_input("Enter the text to be encrypted:")

# Input for shift value
shift = st.number_input("Enter the shift value (1-25):", min_value=1, max_value=25, value=5)

# Button to encrypt
if st.button("Secret Message Maker"):
    if text:
        encrypted_text = caesar(text, shift)
        st.write('**Plain text:**', text)
        st.write('**Encrypted text:**', encrypted_text)
    else:
        st.warning("Please enter a text to encrypt.")

# Input for plain text
text = st.text_input("Enter the text to be decrypted:")

# Input for shift value
shift = st.number_input("Enter the shift value (-25--1):", min_value=-25, max_value=-1, value=-5)

# Button to encrypt
if st.button("Secret Message Decrypter"):
    if text:
        encrypted_text = caesar(text, shift)
        st.write('**Plain text:**', text)
        st.write('**Encrypted text:**', encrypted_text)
    else:
        st.warning("Please enter a text to decrypt.")
