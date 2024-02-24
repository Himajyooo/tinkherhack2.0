import streamlit as st
from aes import encrypt_message, decrypt_message
from caeser import encrypt_caeser, decrypt_caeser
from res import encrypt_res, decrypt_res
from Crypto.Random import get_random_bytes

# Main function to run the Streamlit application
def main():
    st.title("Text Encryption and Decryption App")
    
    # Text input box for user input
    text_input = st.text_area("Enter your text:")

    # Dropdown box to select encryption method
    encryption_method = st.selectbox("Select Encryption Method", ["AES", "Caesar", "Res"])

    if st.button("Encrypt"):
        if text_input:
            if encryption_method == "AES":
                # Call AES encryption function
                key_input = get_random_bytes(16)
                encrypted_text,keyaes = encrypt_message(text_input, key_input)
                st.success("Text Encrypted Successfully!")
                st.write("Encrypted Text:", encrypted_text)
                st.write("With key:",keyaes)
            elif encryption_method == "Caesar":
                # Call Caesar encryption function
                shift = st.text_area("Enter the key:")
                encrypted_text = encrypt_caeser(text_input,shift)
                st.success("Text Encrypted Successfully!")
                st.write("Encrypted Text:", encrypted_text)
            # elif encryption_method == "Res":
            #     # Call Res encryption function
            #     encrypted_text = encrypt_res(text_input)
            #     st.success("Text Encrypted Successfully!")
            #     st.write("Encrypted Text:", encrypted_text)
            # else:
            #     st.error("Encryption method not supported yet.")

    # if st.button("Decrypt"):
    #     encrypted_text = st.text_input("Enter the encrypted text:")
    #     if encrypted_text:
    #         if encryption_method == "AES":
    #             # Call AES decryption function
    #             decrypted_text = decrypt_message(encrypted_text)
    #             st.success("Text Decrypted Successfully!")
    #             st.write("Decrypted Text:", decrypted_text)
    #         elif encryption_method == "Caesar":
    #             # Call Caesar decryption function
    #             decrypted_text = decrypt_caeser(encrypted_text)
    #             st.success("Text Decrypted Successfully!")
    #             st.write("Decrypted Text:", decrypted_text)
    #         elif encryption_method == "Res":
    #             # Call Res decryption function
    #             decrypted_text = decrypt_res(encrypted_text)
    #             st.success("Text Decrypted Successfully!")
    #             st.write("Decrypted Text:", decrypted_text)
    #         else:
    #             st.error("Decryption method not supported yet.")

if __name__ == "__main__":
    main()
