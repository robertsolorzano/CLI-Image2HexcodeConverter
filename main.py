from tkinter import Tk, filedialog
from PIL import Image

def process_image(file_path):
    try:
        img = Image.open(file_path)
        img_rgb = img.convert("RGB")
        pixel_color = img_rgb.getpixel((1, 1))
        hex_color = '#{:02x}{:02x}{:02x}'.format(*pixel_color)
        print(f"Hex color of the first pixel: {hex_color}")
    except Exception as e:
        print(f"Error processing image: {e}")

def main():
    #initialize Tkinter and hide the root window
    root = Tk()
    root.withdraw()

    while True:
        #wait for the user input
        key_pressed = input("Press 'O' to open the file explorer, 'P' to paste the file path from the clipboard then press Enter, or 'Q' to quit: ").lower()

        if key_pressed == 'o':
            file_path = filedialog.askopenfilename()
            if file_path:
                process_image(file_path)
            else:
                print("No file selected.")
        elif key_pressed == 'p':
            #user prompt to paste
            file_path = input("Paste the file path here and press Enter: ").strip()

            #strip the surrounding quotes
            if file_path.startswith(("'", '"')) and file_path.endswith(("'", '"')):
                file_path = file_path[1:-1]

            if file_path:
                process_image(file_path)
            else:
                print("No file path provided.")
        elif key_pressed == 'q':
            print("Exiting...")
            break  #exit the loop
        else:
            print("Invalid input.")

        #ask if the user wants to process another img
        continue_choice = input("Do you want to process another image? (Y/N): ").lower()
        if continue_choice != 'y':
            print("Exiting...")
            break  #exit the loop if the user is finished

if __name__ == "__main__":
    main()
