from PIL import Image

def encode_message(image_path, output_path, message):
    # Bild öffnen
    img = Image.open(image_path).convert("RGB")  # Stelle sicher, dass das Bild im RGB-Format ist
    pixels = img.load()

    # Nachricht in Binär umwandeln und ein Endezeichen hinzufügen
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '00000000'  # Endezeichen (Nullbyte)

    # Überprüfen, ob die Nachricht ins Bild passt
    width, height = img.size
    if len(binary_message) > width * height * 3:
        raise ValueError("Nachricht ist zu lang für das Bild!")

    # Nachricht in die Pixel einbetten
    index = 0
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # R, G, B-Kanäle modifizieren
            if index < len(binary_message):
                r = (r & 0xFE) | int(binary_message[index])
                index += 1
            if index < len(binary_message):
                g = (g & 0xFE) | int(binary_message[index])
                index += 1
            if index < len(binary_message):
                b = (b & 0xFE) | int(binary_message[index])
                index += 1

            # Pixel aktualisieren
            pixels[x, y] = (r, g, b)

    # Bild speichern
    img.save(output_path)
    print(f"Nachricht wurde in {output_path} codiert!")

# Beispiel: Nachricht in ein Bild codieren
encode_message("input.png", "output.png", "Geheime Nachricht!")

# Yt Video: https://www.youtube.com/watch?v=u_luy52v7z4