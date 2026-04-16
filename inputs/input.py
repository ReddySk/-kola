from pynput import keyboard, mouse
import time


def on_press(key):
    print(f"Key {key} pressed") 
    
def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at ({x}, {y}) with {button}") 
        
if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press) as keyboard_listener, mouse.Listener(on_click=on_click) as mouse_listener:
        keyboard_listener.join()
        mouse_listener.join()   
        
        