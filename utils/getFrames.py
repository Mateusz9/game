from PIL import Image, ImageSequence

def loadGIF(filename, pygame):
    pilImage = Image.open(filename)
    frames = []
    for frame in ImageSequence.Iterator(pilImage):
        frame = frame.convert('RGBA')
        pygameImage = pygame.image.fromstring(
            frame.tobytes(), frame.size, frame.mode).convert_alpha()
        pygameImage = pygame.transform.scale(pygameImage, (100, 100))
        frames.append(pygameImage)
    return frames