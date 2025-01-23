from PIL import Image

def decode_message(image_path):
    # Bild öffnen
    img = Image.open(image_path).convert("RGB")  # Stelle sicher, dass das Bild im RGB-Format ist
    pixels = img.load()

    # Binäre Nachricht extrahieren
    binary_message = ""
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # LSBs der R, G, B-Kanäle extrahieren
            binary_message += str(r & 1)
            binary_message += str(g & 1)
            binary_message += str(b & 1)

    # Binäre Nachricht in Zeichen umwandeln
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if byte == '00000000':  # Endezeichen gefunden
            break
        if byte:  # Vermeide leere Bytes am Ende
            message += chr(int(byte, 2))

    return message

# Beispiel: Nachricht aus einem Bild decodieren
decoded_message = decode_message("output.png")
print(f"Decodierte Nachricht: {decoded_message}")