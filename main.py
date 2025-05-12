"""
Bad Version SIM - Main Application
A Tkinter-based GUI application for displaying country flags and generating phone numbers.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import logging
from typing import Optional

from config import *
from utils import load_countries, load_area_codes, generate_phone_number

class BadVersionSIM:
    """Main application class for Bad Version SIM."""
    
    def __init__(self):
        """Initialize the application."""
        self.setup_logging()
        self.load_data()
        self.setup_gui()
        
    def setup_logging(self):
        """Configure logging for the application."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        
    def load_data(self):
        """Load application data from files."""
        try:
            self.countries = load_countries()
            self.area_codes = load_area_codes()
        except Exception as e:
            logging.error(f"Error loading data: {str(e)}")
            messagebox.showerror("Error", f"Failed to load data: {str(e)}")
            raise
            
    def setup_gui(self):
        """Set up the main GUI window and components."""
        self.root = tk.Tk()
        self.root.title(APP_TITLE)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.configure(bg=BG_COLOR)
        
        self.create_main_frame()
        self.create_title()
        self.create_country_list()
        self.create_phone_section()
        self.create_footer()
        
    def create_main_frame(self):
        """Create the main frame with padding."""
        self.main_frame = ttk.Frame(self.root, padding=PADDING)
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
    def create_title(self):
        """Create the application title."""
        title = tk.Label(
            self.main_frame,
            text=APP_TITLE,
            font=TITLE_FONT,
            fg=PRIMARY_TEXT_COLOR,
            bg=BG_COLOR
        )
        title.grid(row=0, column=0, pady=(0, PADDING))
        
    def create_country_list(self):
        """Create the scrollable country list."""
        # Create frame for the list
        list_frame = ttk.Frame(self.main_frame)
        list_frame.grid(row=1, column=0, sticky="nsew", pady=PADDING)
        
        # Create scrollbar and listbox
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.country_list = tk.Listbox(
            list_frame,
            yscrollcommand=scrollbar.set,
            font=NORMAL_FONT,
            bg=BG_COLOR,
            fg=SECONDARY_TEXT_COLOR,
            selectmode=tk.SINGLE,
            height=10
        )
        
        # Populate the list
        for country, flag in self.countries.items():
            self.country_list.insert(tk.END, f"{flag} {country}")
            
        self.country_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.country_list.yview)
        
    def create_phone_section(self):
        """Create the phone number generation section."""
        phone_frame = ttk.Frame(self.main_frame)
        phone_frame.grid(row=2, column=0, pady=PADDING)
        
        # Generate button
        self.generate_button = tk.Button(
            phone_frame,
            text="Generate Phone Number",
            command=self.generate_new_number,
            font=BUTTON_FONT,
            bg=BUTTON_BG,
            fg=SECONDARY_TEXT_COLOR,
            activebackground=BUTTON_ACTIVE_BG,
            activeforeground=SECONDARY_TEXT_COLOR
        )
        self.generate_button.pack(pady=PADDING)
        
        # Phone number display
        self.phone_label = tk.Label(
            phone_frame,
            text="Click to generate",
            font=NUMBER_FONT,
            fg=PRIMARY_TEXT_COLOR,
            bg=BG_COLOR
        )
        self.phone_label.pack()
        
        # Add tooltips
        self.create_tooltip(self.generate_button, "Click to generate a new US phone number")
        
    def create_footer(self):
        """Create the application footer."""
        footer = tk.Label(
            self.main_frame,
            text=f"{APP_TITLE} - {APP_VERSION}",
            font=NORMAL_FONT,
            fg=SECONDARY_TEXT_COLOR,
            bg=BG_COLOR
        )
        footer.grid(row=3, column=0, pady=PADDING)
        
    def generate_new_number(self):
        """Generate and display a new phone number."""
        try:
            number = generate_phone_number(self.area_codes)
            self.phone_label.config(text=number)
        except Exception as e:
            logging.error(f"Error generating phone number: {str(e)}")
            messagebox.showerror("Error", "Failed to generate phone number")
            
    def create_tooltip(self, widget: tk.Widget, text: str):
        """Create a tooltip for a widget."""
        def show_tooltip(event):
            tooltip = tk.Toplevel()
            tooltip.wm_overrideredirect(True)
            tooltip.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")
            
            label = tk.Label(
                tooltip,
                text=text,
                font=NORMAL_FONT,
                bg=BG_COLOR,
                fg=SECONDARY_TEXT_COLOR,
                relief="solid",
                borderwidth=1
            )
            label.pack()
            
            def hide_tooltip():
                tooltip.destroy()
                
            widget.tooltip = tooltip
            tooltip.bind("<Leave>", lambda e: hide_tooltip())
            widget.bind("<Leave>", lambda e: hide_tooltip())
            
        widget.bind("<Enter>", show_tooltip)
        
    def run(self):
        """Start the application main loop."""
        try:
            self.root.mainloop()
        except Exception as e:
            logging.error(f"Application error: {str(e)}")
            messagebox.showerror("Error", "An unexpected error occurred")
            raise

if __name__ == "__main__":
    try:
        app = BadVersionSIM()
        app.run()
    except Exception as e:
        logging.critical(f"Failed to start application: {str(e)}")
        messagebox.showerror("Critical Error", "Failed to start application")