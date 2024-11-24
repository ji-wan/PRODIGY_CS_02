from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size
    
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            
            #swapping red and blue channels
            encrypted_pixel = (b, g, r)
            
            pixels[i, j] = encrypted_pixel
            
    img.save(output_path)
    print("image encrypted succesfully")
    
def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size
    
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            
            #swapping red and blue channels back
            decrypted_pixel = (b, g, r)
            
            pixels[i, j] = decrypted_pixel
    
    img.save(output_path)
    print("image decrypted succesfully")
    
#exmaple usage
input_image = r"C:\Users\Dell\OneDrive\Desktop\task02\image.jpg"
encrypted_image = r"C:\Users\Dell\OneDrive\Desktop\task02\eimg.jpg"
decrypted_image = r"C:\Users\Dell\OneDrive\Desktop\task02\dimg.jpeg"

#encrypt the image
encrypt_image(input_image, encrypted_image, key=None)

#decrypt the image
decrypt_image(encrypted_image, decrypted_image, key=None)
    
    