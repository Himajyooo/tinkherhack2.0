import streamlit as st
from aes import encrypt_aes,decrypt_aes, get_iv, get_key
from caeser import encrypt_caeser,decrypt_caesar
from Crypto.Random import get_random_bytes
from new import consvow_encrypt,consvow_decrypt

# Main function to run the Streamlit application
def main():
    global key, iv
    st.title("Text Encryption App")
    
    # Text input box for user input
    text_input = st.text_area("Enter your text:")

    # Dropdown box to select encryption method
    encryption_method = st.selectbox("Select Encryption Method", ["AES", "Caesar","Consvow"])
    
    if text_input:
        if encryption_method == "AES":
            # Generate a random key
            key = get_random_bytes(16)
            # Call AES encryption function
            if st.button("Encrypt"):
                encrypted_text,iv = encrypt_aes(text_input, key)
                st.success("Text Encrypted Successfully!")
                # st.write("Encrypted Text: <b>{}</b>".format(encrypted_text), unsafe_allow_html=True)
                st.write("Encrypted Text :",encrypted_text.hex())
                st.write("Encryption Key:", iv.hex())
        elif encryption_method == "Caesar":
            # Call Caesar encryption function
            shift = st.number_input("Enter the key:",step=1)
            if st.button("Encrypt"):
                encrypted_text = encrypt_caeser(text_input, shift)
                st.success("Text Encrypted Successfully!")
                st.write("Encrypted Text:", encrypted_text)

        elif encryption_method == "Consvow":
            # Call Caesar encryption function
            shift1 = st.number_input("Enter the vowel shift:",step=1)
            shift2 = st.number_input("Enter the consonant shift:",step=1)
            if st.button("Encrypt"):
                encrypted_text = consvow_encrypt(text_input, shift1, shift2)
                st.success("Text Encrypted Successfully!")
                st.write("Encrypted Text:", encrypted_text)
        else:
            st.error("Encryption method not supported yet.")

    st.title("Text Decryption App")
    
    # Text input box for user input
    text_input2 = st.text_area("Enter your texxt:")

    # Dropdown box to select encryption method
    decryption_method = st.selectbox("Select Decryption Method", ["AES", "Caesar","Consvow"])
    
    if text_input2:
        if decryption_method == "AES":
            key = get_key()
            iv = get_iv()
            # Call AES encryption function
            if st.button("Decrypt"):
                decrypted_text= decrypt_aes(text_input2,key, iv)
                st.success("Text Decrypted Successfully!")
                st.write("Decrypted Text :",decrypted_text)
                
        elif decryption_method == "Caesar":
            # Call Caesar encryption function
            shift = st.number_input("Enter the keyy:",step=1)
            if st.button("Decrypt"):
                decrypted_text = decrypt_caesar(text_input2, shift)
                st.success("Text Decrypted Successfully!")
                st.write("Decrypted Text:", decrypted_text)

        elif decryption_method == "Consvow":
            # Call Caesar encryption function
            shift1 = st.number_input("Enter the vowel shift.:",step=1)
            shift2 = st.number_input("Enter the consonant shift.:",step=1)
            if st.button("Decrypt"):
                decrypted_text = consvow_decrypt(text_input2, shift1,shift2)
                st.success("Text Decrypted Successfully!")
                st.write("Decrypted Text:", decrypted_text)
        else:
            st.error("Encryption method not supported yet.")

if __name__ == "__main__":
    main()
