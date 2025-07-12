from PIL import Image

def encrypt_image(image_path, output_path):
    img = Image.open(image_path)
    img = img.convert("RGB")  # Ensure it's in RGB format
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            # Simple encryption: Invert each color component
            pixels[i, j] = (255 - r, 255 - g, 255 - b)

    img.save(output_path)
    print(f"🔐 Encrypted image saved as {output_path}")

def decrypt_image(encrypted_path, output_path):
    # Decryption is same as encryption for this invert method
    encrypt_image(encrypted_path, output_path)

# --- Main Driver Code ---

# ✅ Replace with the actual path to your original image
encrypt_image("C:/Users/rajki/Downloads/original.png", "encrypted.png")
decrypt_image("encrypted.png", "decrypted.png")
