import customtkinter as ctk
import tkinter as tk
import locale
from PIL import Image, ImageTk
import os

class DirtyMoneyConverter(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configure the window
        self.title("Apollo Networks - Dirty Money Converter")
        self.geometry("450x650")  # Increased height for the new button
        ctk.set_appearance_mode("dark")
        
        # Set the icon
        self.set_icon()
        
        # Set locale for proper money formatting
        try:
            locale.setlocale(locale.LC_ALL, '')
        except locale.Error:
            print("Warning: Unable to set locale. Using default formatting.")

        # Custom color scheme
        self.bg_color = "#001F3F"  # Dark blue background
        self.fg_color = "#E0E0E0"  # Light text color
        self.accent_color = "#00FF00"  # Bright green accent
        self.button_color = "#003366"  # Darker blue for buttons and frames
        self.coming_soon_color = "#8A2BE2"  # Vibrant purple for Coming Soon button
        self.configure(bg=self.bg_color)

        # Create main frame
        self.main_frame = ctk.CTkFrame(self, fg_color=self.bg_color)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Create and place widgets
        self.create_widgets()

    def set_icon(self):
        try:
            icon_path = os.path.join(os.path.dirname(__file__), "money-bag.png")
            print(f"Attempting to load icon from: {icon_path}")
            if os.path.exists(icon_path):
                icon = Image.open(icon_path)
                photo = ImageTk.PhotoImage(icon)
                self.iconphoto(True, photo)
                print("Icon set successfully")
            else:
                print(f"Icon file not found at {icon_path}")
        except Exception as e:
            print(f"Error loading icon: {e}")

    def create_widgets(self):
        # Title
        title_label = ctk.CTkLabel(self.main_frame, text="Dirty Money Converter", 
                                   font=("Roboto", 28, "bold"), 
                                   text_color=self.accent_color)
        title_label.pack(pady=(0, 30))

        # Input Frame
        input_frame = ctk.CTkFrame(self.main_frame, fg_color=self.button_color)
        input_frame.pack(fill=tk.X, padx=10, pady=10)

        amount_label = ctk.CTkLabel(input_frame, text="Enter dirty money amount:", 
                                    font=("Roboto", 14), text_color=self.fg_color)
        amount_label.pack(pady=(10, 5))

        self.amount_entry = ctk.CTkEntry(input_frame, width=200, fg_color=self.bg_color, 
                                         text_color=self.fg_color)
        self.amount_entry.pack(pady=(0, 10))

        # Convert Button
        convert_button = ctk.CTkButton(self.main_frame, text="Convert", command=self.convert_money, 
                                       fg_color=self.accent_color, hover_color="#00CC00",
                                       text_color=self.bg_color, font=("Roboto", 16, "bold"))
        convert_button.pack(pady=20)

        # Result Frame
        self.result_frame = ctk.CTkFrame(self.main_frame, fg_color=self.button_color)
        self.result_frame.pack(fill=tk.X, padx=10, pady=10)

        result_title = ctk.CTkLabel(self.result_frame, text="Conversion Result", 
                                    font=("Roboto", 18, "bold"), text_color=self.accent_color)
        result_title.pack(pady=(10, 5))

        self.clean_money_label = ctk.CTkLabel(self.result_frame, text="Clean Money: $0.00", 
                                              font=("Roboto", 16), text_color=self.fg_color)
        self.clean_money_label.pack(pady=5)

        self.fee_label = ctk.CTkLabel(self.result_frame, text="Conversion Fee: $0.00", 
                                      font=("Roboto", 14), text_color=self.fg_color)
        self.fee_label.pack(pady=(0, 10))

        # Status Message
        self.status_label = ctk.CTkLabel(self.main_frame, text="", font=("Roboto", 14))
        self.status_label.pack(pady=10)

        # Coming Soon Button
        coming_soon_button = ctk.CTkButton(self.main_frame, text="Coming Soon", 
                                           command=self.show_coming_soon,
                                           fg_color=self.coming_soon_color, 
                                           hover_color="#9F3FFF",
                                           text_color=self.fg_color, 
                                           font=("Roboto", 14, "bold"))
        coming_soon_button.pack(pady=20)

        # Made by xhox label
        made_by_label = ctk.CTkLabel(self.main_frame, text="Made by xhox", 
                                     font=("Roboto", 12), 
                                     text_color=self.fg_color)
        made_by_label.pack(side=tk.BOTTOM, pady=(20, 0))

    def format_money(self, amount):
        try:
            return locale.currency(amount, grouping=True)
        except locale.Error:
            return f"${amount:.2f}"

    def convert_money(self):
        try:
            dirty_money = float(self.amount_entry.get())
            if dirty_money <= 0:
                raise ValueError("Amount must be positive")

            # Calculate conversion fee (fixed 23%)
            fee_percentage = 0.23
            fee = dirty_money * fee_percentage

            # Calculate clean money
            clean_money = dirty_money - fee

            # Update labels with formatted money values
            self.clean_money_label.configure(text=f"Clean Money: {self.format_money(clean_money)}")
            self.fee_label.configure(text=f"Conversion Fee: {self.format_money(fee)}")
            self.status_label.configure(text="Conversion successful!", text_color=self.accent_color)

        except ValueError as e:
            self.status_label.configure(text=str(e), text_color="#FF3366")  # Error in red

    def show_coming_soon(self):
        # Hide main frame
        self.main_frame.pack_forget()

        # Create and show coming soon frame
        coming_soon_frame = ctk.CTkFrame(self, fg_color=self.bg_color)
        coming_soon_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        coming_soon_label = ctk.CTkLabel(coming_soon_frame, text="Coming Soon!", 
                                         font=("Roboto", 36, "bold"), 
                                         text_color=self.accent_color)
        coming_soon_label.pack(pady=(50, 30))

        description_label = ctk.CTkLabel(coming_soon_frame, 
                                         text="Exciting new features are on the way!\nStay tuned for updates.",
                                         font=("Roboto", 18), 
                                         text_color=self.fg_color)
        description_label.pack(pady=20)

        back_button = ctk.CTkButton(coming_soon_frame, text="Back to Converter", 
                                    command=lambda: self.show_main_frame(coming_soon_frame),
                                    fg_color=self.accent_color, hover_color="#00CC00",
                                    text_color=self.bg_color, font=("Roboto", 16, "bold"))
        back_button.pack(pady=30)

    def show_main_frame(self, current_frame):
        # Hide current frame and show main frame
        current_frame.destroy()
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

if __name__ == "__main__":
    app = DirtyMoneyConverter()
    app.mainloop()
