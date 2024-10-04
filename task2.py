from PIL import Image
import numpy as np
import os

def encrypt_image(image_path, key):
    # Open the image
    image = Image.open(image_path)
    # Convert the image into a NumPy array for pixel manipulation
    image_array = np.array(image)

    # Encrypt by adding the key to each pixel value
    encrypted_array = (image_array + key) % 256

    # Convert back to an image
    encrypted_image = Image.fromarray(np.uint8(encrypted_array))

    # Generate output filename
    base, ext = os.path.splitext(image_path)
    output_path = f"{base}_encrypted{ext}"

    # Save the encrypted image
    encrypted_image.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(image_path, key):
    # Open the image
    image = Image.open(image_path)
    # Convert the image into a NumPy array for pixel manipulation
    image_array = np.array(image)

    # Decrypt by subtracting the key from each pixel value
    decrypted_array = (image_array - key) % 256

    # Convert back to an image
    decrypted_image = Image.fromarray(np.uint8(decrypted_array))

    # Generate output filename
    base, ext = os.path.splitext(image_path)
    output_path = f"{base}_decrypted{ext}"

    # Save the decrypted image
    decrypted_image.save(output_path)
    print(f"Decrypted image saved as {output_path}")

def main():
    print("Image Encryption/Decryption Tool")
    choice = input("Do you want to encrypt or decrypt an image? (e/d): ").lower()

    if choice not in ['e', 'd']:
        print("Invalid choice!")
        return

    image_path = input("Enter the image file path: ")
    key = int(input("Enter the encryption/decryption key (a number): "))

    if choice == 'e':
        encrypt_image(image_path, key)
    elif choice == 'd':
        decrypt_image(image_path, key)

if __name__ == "__main__":
    main()
