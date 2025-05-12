from colorama import init, Fore
import time
import os
import tkinter as tk
from tkinter import messagebox

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

main_text = """
░█████╗░██╗░░░░░███╗░░░███╗░█████╗░██╗░░░██╗██╗██╗░░░██╗░█████╗░
██╔══██╗██║░░░░░████╗░████║██╔══██╗██║░░░██║██║██║░░░██║██╔══██╗
███████║██║░░░░░██╔████╔██║███████║╚██╗░██╔╝██║╚██╗░██╔╝███████║
██╔══██║██║░░░░░██║╚██╔╝██║██╔══██║░╚████╔╝░██║░╚████╔╝░██╔══██║
██║░░██║███████╗██║░╚═╝░██║██║░░██║░░╚██╔╝░░██║░░╚██╔╝░░██║░░██║
╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝

Dev By: ENG: Ahmed Samir +201029107547
"""

menu1 = Fore.RED + """
[Spain]      █ ▀█▀ ▄▀█ █░░ █▄█
[Croatia]    █ ░█░ █▀█ █▄▄ ░█░

1: Let Bot Sign
2: Upload Photo's
3: Api
"""

menu2 = Fore.RED + """
[Family Reunion]  █▀ █▀▀ █░█ █▀▀ █▄░█ █▀▀ █▀▀ █▄░█   █░█ █ █▀ ▄▀█
                  ▄█ █▄▄ █▀█ ██▄ █░▀█ █▄█ ██▄ █░▀█   ▀▄▀ █ ▄█ █▀█

4: Replaced VFS
5: Replaced TLS Contact
6: BLS Connected
"""

sub_options = {
    "1": ["Check Session", "Run Automation", "Exit Bot"],
    "2": ["Select Directory", "Optimize Images", "Upload Now"],
    "3": ["Check Token", "Get Data", "Send Request"],
    "4": ["Backup Files", "Replace Files", "Verify Change"],
    "5": ["Clear Cache", "Replace Config", "Restart System"],
    "6": ["Connect to BLS", "Validate Docs", "Exit"]
}

clear()
print(main_text)
print(menu1)
print(menu2)

choice = input(Fore.CYAN + "\nSelect an option (1-6): ").strip()

if choice in sub_options:
    clear()
    print(Fore.GREEN + f"\nSub-options for choice {choice}:\n")
    for idx, opt in enumerate(sub_options[choice], 1):
        print(f"{idx}: {opt}")
    
    sub_choice = input(Fore.CYAN + "\nSelect sub-option (1-3): ").strip()

    if sub_choice in ["1", "2", "3"]:
        print(Fore.YELLOW + "\nLoading...")
        time.sleep(1.5)
        print(Fore.GREEN + f"Done: {sub_options[choice][int(sub_choice)-1]}")

        # Show external pop-up only for Run Automation
        if choice == "1" and sub_choice == "2":
            root = tk.Tk()
            root.withdraw()  # Hide the main tkinter window
            messagebox.showinfo("Appointment Booked", "Appointment booked for Mohamed Ali Khamis\nCall: +201029107547")
            root.destroy()
            print(Fore.GREEN + "✔️ Appointment booked successfully")
    else:
        print(Fore.RED + "Invalid sub-option.")
else:
    print(Fore.RED + "Invalid main option.")
