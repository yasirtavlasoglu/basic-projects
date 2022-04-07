import pynput.keyboard

def emir(harfler):
    print(harfler)

dinleme = pynput.keyboard.Listener(on_press=emir)

with dinleme:
    dinleme.join()
