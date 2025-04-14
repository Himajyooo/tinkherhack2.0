# # import streamlit as st
# # from aes import encrypt_aes,decrypt_aes, get_iv, get_key
# # from caeser import encrypt_caeser,decrypt_caesar
# # from Crypto.Random import get_random_bytes
# # from new import consvow_encrypt,consvow_decrypt

# # # Main function to run the Streamlit application
# # def main():
# #     global key, iv
# #     st.title("Text Encryption App")
    
# #     # Text input box for user input
# #     text_input = st.text_area("Enter your text:")

# #     # Dropdown box to select encryption method
# #     encryption_method = st.selectbox("Select Encryption Method", ["AES", "Caesar","Consvow"])
    
# #     if text_input:
# #         if encryption_method == "AES":
# #             # Generate a random key
# #             key = get_random_bytes(16)
# #             # Call AES encryption function
# #             if st.button("Encrypt"):
# #                 encrypted_text,iv = encrypt_aes(text_input, key)
# #                 st.success("Text Encrypted Successfully!")
# #                 # st.write("Encrypted Text: <b>{}</b>".format(encrypted_text), unsafe_allow_html=True)
# #                 st.write("Encrypted Text :",encrypted_text.hex())
# #                 st.write("Encryption Key:", iv.hex())
# #         elif encryption_method == "Caesar":
# #             # Call Caesar encryption function
# #             shift = st.number_input("Enter the key:",step=1)
# #             if st.button("Encrypt"):
# #                 encrypted_text = encrypt_caeser(text_input, shift)
# #                 st.success("Text Encrypted Successfully!")
# #                 st.write("Encrypted Text:", encrypted_text)

# #         elif encryption_method == "Consvow":
# #             # Call Caesar encryption function
# #             shift1 = st.number_input("Enter the vowel shift:",step=1)
# #             shift2 = st.number_input("Enter the consonant shift:",step=1)
# #             if st.button("Encrypt"):
# #                 encrypted_text = consvow_encrypt(text_input, shift1, shift2)
# #                 st.success("Text Encrypted Successfully!")
# #                 st.write("Encrypted Text:", encrypted_text)
# #         else:
# #             st.error("Encryption method not supported yet.")

# #     st.title("Text Decryption App")
    
# #     # Text input box for user input
# #     text_input2 = st.text_area("Enter your texxt:")

# #     # Dropdown box to select encryption method
# #     decryption_method = st.selectbox("Select Decryption Method", ["AES", "Caesar","Consvow"])
    
# #     if text_input2:
# #         if decryption_method == "AES":
# #             key = get_key()
# #             iv = get_iv()
# #             # Call AES encryption function
# #             if st.button("Decrypt"):
# #                 decrypted_text= decrypt_aes(text_input2,key, iv)
# #                 st.success("Text Decrypted Successfully!")
# #                 st.write("Decrypted Text :",decrypted_text)
                
# #         elif decryption_method == "Caesar":
# #             # Call Caesar encryption function
# #             shift = st.number_input("Enter the keyy:",step=1)
# #             if st.button("Decrypt"):
# #                 decrypted_text = decrypt_caesar(text_input2, shift)
# #                 st.success("Text Decrypted Successfully!")
# #                 st.write("Decrypted Text:", decrypted_text)

# #         elif decryption_method == "Consvow":
# #             # Call Caesar encryption function
# #             shift1 = st.number_input("Enter the vowel shift.:",step=1)
# #             shift2 = st.number_input("Enter the consonant shift.:",step=1)
# #             if st.button("Decrypt"):
# #                 decrypted_text = consvow_decrypt(text_input2, shift1,shift2)
# #                 st.success("Text Decrypted Successfully!")
# #                 st.write("Decrypted Text:", decrypted_text)
# #         else:
# #             st.error("Encryption method not supported yet.")

# # if __name__ == "__main__":
# #     main()

# import streamlit as st
# from aes import encrypt_aes, decrypt_aes
# from caeser import encrypt_caeser, decrypt_caesar
# from new import consvow_encrypt, consvow_decrypt
# from Crypto.Random import get_random_bytes

# # Initialize session state
# if "page" not in st.session_state:
#     st.session_state.page = "home"

# # Function to navigate between pages
# def navigate(page):
#     st.session_state.page = page
#     st.rerun()

# # ---------------- Main Menu ----------------
# if st.session_state.page == "home":
#     st.title("🔐 Secure Encryption App")
#     st.write("Choose an option:")
    
#     col1, col2 = st.columns(2)
#     with col1:
#         if st.button("Encrypt 🔒", use_container_width=True):
#             navigate("encrypt")
    
#     with col2:
#         if st.button("Decrypt 🔓", use_container_width=True):
#             navigate("decrypt")

# # ---------------- Encryption Page ----------------
# elif st.session_state.page == "encrypt":
#     st.title("🔒 Encryption Page")
#     text_input = st.text_area("Enter text to encrypt:", height=100)
#     encryption_method = st.selectbox("Choose an encryption method:", ["AES", "Caesar Cipher", "Consonant-Vowel Encryption"])
    
#     shift_value = 0
#     vowel_shift = 0
#     consonant_shift = 0

#     if encryption_method == "Caesar Cipher":
#         shift_value = st.number_input("Enter shift value:", min_value=1, max_value=25, step=1, value=3)

#     if encryption_method == "Consonant-Vowel Encryption":
#         consonant_shift = st.number_input("Enter consonant shift value:", min_value=1, max_value=25, step=1, value=3)
#         vowel_shift = st.number_input("Enter vowel shift value:", min_value=1, max_value=25, step=1, value=2)

#     if st.button("Encrypt Now"):
#         if text_input.strip():
#             if encryption_method == "AES":
#                 key = get_random_bytes(16)  # Generate a random AES key
#                 encrypted_text, iv = encrypt_aes(text_input, key)  

#                 st.session_state.key = key.hex()  # Convert key to hex before storing
#                 st.session_state.iv = iv  # No need for `.hex()`, iv is already a string

#             elif encryption_method == "Caesar Cipher":
#                 encrypted_text = encrypt_caeser(text_input, shift=shift_value)
#             else:
#                 encrypted_text = consvow_encrypt(text_input, consonant_shift=consonant_shift, vowel_shift=vowel_shift)
            
#             st.success(f"🔒 Encrypted Text: {encrypted_text}")
#         else:
#             st.warning("Please enter text to encrypt.")

#     if st.button("🔙 Back to Home"):
#         navigate("home")

# # ---------------- Decryption Page ----------------
# elif st.session_state.page == "decrypt":
#     st.title("🔓 Decryption Page")
#     text_input = st.text_area("Enter text to decrypt:", height=100)
#     decryption_method = st.selectbox("Choose a decryption method:", ["AES", "Caesar Cipher", "Consonant-Vowel Decryption"])

#     shift_value = 0
#     vowel_shift = 0
#     consonant_shift = 0

#     if decryption_method == "Caesar Cipher":
#         shift_value = st.number_input("Enter shift value:", min_value=1, max_value=25, step=1, value=3)

#     if decryption_method == "Consonant-Vowel Decryption":
#         consonant_shift = st.number_input("Enter consonant shift value:", min_value=1, max_value=25, step=1, value=3)
#         vowel_shift = st.number_input("Enter vowel shift value:", min_value=1, max_value=25, step=1, value=2)

#     if st.button("Decrypt Now"):
#         if text_input.strip():
#             try:
#                 if decryption_method == "AES":
#                     key = bytes.fromhex(st.session_state.key)  # Convert key back to bytes
#                     iv = st.session_state.iv  # IV is already in Base64, no need to decode further

#                     decrypted_text = decrypt_aes(text_input, key, iv)

#                 elif decryption_method == "Caesar Cipher":
#                     decrypted_text = decrypt_caesar(text_input, shift=shift_value)
#                 else:
#                     decrypted_text = consvow_decrypt(text_input, consonant_shift=consonant_shift, vowel_shift=vowel_shift)
                
#                 st.success(f"🔓 Decrypted Text: {decrypted_text}")
#             except Exception:
#                 st.error("Decryption failed. Make sure you are using the correct key and IV.")
#         else:
#             st.warning("Please enter text to decrypt.")

#     if st.button("🔙 Back to Home"):
#         navigate("home")

import streamlit as st
from aes import encrypt_aes, decrypt_aes
from caeser import encrypt_caeser, decrypt_caesar
from new import consvow_encrypt, consvow_decrypt
from Crypto.Random import get_random_bytes
import base64

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "home"

# Function to navigate between pages
def navigate(page):
    st.session_state.page = page
    st.rerun()

# ---------------- Home Page ----------------
if st.session_state.page == "home":
    st.title("🔐 Secure Encryption App")
    st.write("Choose an option:")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Encrypt 🔒", use_container_width=True):
            navigate("encrypt")
    
    with col2:
        if st.button("Decrypt 🔓", use_container_width=True):
            navigate("decrypt")

# ---------------- Encryption Page ----------------
elif st.session_state.page == "encrypt":
    st.title("🔒 Encrypt a File or Text")

    encryption_method = st.selectbox("Choose an encryption method:", ["AES", "Caesar Cipher", "Consonant-Vowel Encryption"])

    # File Upload
    uploaded_file = st.file_uploader("Upload a file for encryption (optional)", type=["txt"])
    text_input = st.text_area("Or enter text to encrypt:", height=100)

    if uploaded_file is not None:
        text_input = uploaded_file.getvalue().decode()

    shift_value = 0
    consonant_shift = 0
    vowel_shift = 0

    if encryption_method == "Caesar Cipher":
        shift_value = st.number_input("Enter shift value:", min_value=1, max_value=25, step=1, value=3)

    if encryption_method == "Consonant-Vowel Encryption":
        consonant_shift = st.number_input("Enter consonant shift value:", min_value=1, max_value=25, step=1, value=3)
        vowel_shift = st.number_input("Enter vowel shift value:", min_value=1, max_value=25, step=1, value=2)

    if text_input:
        if st.button("Encrypt Now"):
            if encryption_method == "AES":
                key = get_random_bytes(16)  # Generate AES key
                encrypted_text, iv = encrypt_aes(text_input, key)
                st.session_state.key = key.hex()
                st.session_state.iv = iv
            elif encryption_method == "Caesar Cipher":
                encrypted_text = encrypt_caeser(text_input, shift=shift_value)
            else:
                encrypted_text = consvow_encrypt(text_input, consonant_shift=consonant_shift, vowel_shift=vowel_shift)

            st.success("🔒 Encryption Successful!")

            if uploaded_file is None:  # If user entered text manually, show output directly
                st.text_area("🔐 Encrypted Text:", encrypted_text, height=150)
            else:  # If user uploaded a file, provide download option
                encrypted_data = encrypted_text.encode()
                st.download_button(label="📥 Download Encrypted File",
                                   data=encrypted_data,
                                   file_name="encrypted.txt",
                                   mime="text/plain")
    
    if st.button("🔙 Back to Home"):
        navigate("home")

# ---------------- Decryption Page ----------------
elif st.session_state.page == "decrypt":
    st.title("🔓 Decrypt a File or Text")

    decryption_method = st.selectbox("Choose a decryption method:", ["AES", "Caesar Cipher", "Consonant-Vowel Decryption"])

    # File Upload
    uploaded_file = st.file_uploader("Upload an encrypted file (optional)", type=["txt"])
    text_input = st.text_area("Or enter encrypted text:", height=100)

    if uploaded_file is not None:
        text_input = uploaded_file.getvalue().decode()

    shift_value = 0
    consonant_shift = 0
    vowel_shift = 0

    if decryption_method == "Caesar Cipher":
        shift_value = st.number_input("Enter shift value:", min_value=1, max_value=25, step=1, value=3)

    if decryption_method == "Consonant-Vowel Decryption":
        consonant_shift = st.number_input("Enter consonant shift value:", min_value=1, max_value=25, step=1, value=3)
        vowel_shift = st.number_input("Enter vowel shift value:", min_value=1, max_value=25, step=1, value=2)

    if text_input:
        if st.button("Decrypt Now"):
            try:
                if decryption_method == "AES":
                    key = bytes.fromhex(st.session_state.key)
                    iv = st.session_state.iv
                    decrypted_text = decrypt_aes(text_input, key, iv)
                elif decryption_method == "Caesar Cipher":
                    decrypted_text = decrypt_caesar(text_input, shift=shift_value)
                else:
                    decrypted_text = consvow_decrypt(text_input, consonant_shift=consonant_shift, vowel_shift=vowel_shift)
                
                st.success("✅ Decryption Successful!")

                if uploaded_file is None:  # If user entered text manually, show output directly
                    st.text_area("🔓 Decrypted Text:", decrypted_text, height=150)
                else:  # If user uploaded a file, provide download option
                    decrypted_data = decrypted_text.encode()
                    st.download_button(label="📥 Download Decrypted File",
                                       data=decrypted_data,
                                       file_name="decrypted.txt",
                                       mime="text/plain")
            except Exception as e:
                st.error(f"Decryption failed: {e}")

    if st.button("🔙 Back to Home"):
        navigate("home")