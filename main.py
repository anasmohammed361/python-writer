import customtkinter
import pyautogui
import tkinter as tk
import time

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Skill Rack Copy Paster")
        self.geometry("700x500")
        
        # Create a Textbox for the top section
        self.text_box = customtkinter.CTkTextbox(self, 400, 400, 20)
        self.text_box.pack(fill=tk.BOTH, expand=True)
        
        # Create a Frame for the bottom section
        self.bottom_frame = customtkinter.CTkFrame(self)
        self.bottom_frame.pack(fill=tk.X)
        
        # Create a "Start Typing" button
        self.type_btn = customtkinter.CTkButton(self.bottom_frame, text="Start Typing", command=self.start_typing,width=300,border_spacing=6)
        self.type_btn.pack(side=tk.LEFT ,padx=10 ,pady=10)
        
        # Create a "Clear" button
        self.clear_btn = customtkinter.CTkButton(self.bottom_frame, text="Clear", command=self.clear_text,width=300,border_spacing=6)
        self.clear_btn.pack(side=tk.RIGHT,padx=10,pady=10)

    def start_typing(self):
        # Get the text from the Textbox
        input_text = self.text_box.get("1.0", tk.END)
        time.sleep(4)
        
        pyautogui.typewrite(input_text,1.0/40)
        # You can replace this with your desired typing logic
        # Here, we simulate typing the text using pyautogui
        # pyautogui.typewrite(input_text)

    def clear_text(self):
        # Clear the Textbox
        self.text_box.delete("1.0",tk.END)


if __name__ == "__main__":
    app = App()
    app.mainloop()
