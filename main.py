import tkinter as tk
import webbrowser
from tkinter import filedialog, messagebox, ttk, scrolledtext
import sys
import os
import shutil


class App:
    def __init__(self, master):
        self.master = master
        master.title("Kenshi WorkshopMod Folders Renamer")

        self.folder_path = None
        self.destination_path = None

        self.select_button = tk.Button(master, text="Select Source Folder", command=self.select_folder, padx=10, pady=5)
        self.select_button.place(relx=0.5, rely=0.32, anchor="center")

        self.destination_button = tk.Button(master, text="Select Destination Folder", command=self.select_destination, padx=10, pady=5)
        self.destination_button.place(relx=0.5, rely=0.64, anchor="center")

        self.var1 = tk.IntVar()
        self.c1 = tk.Checkbutton(master, text='Destination same as source',variable=self.var1, onvalue=1, offvalue=0, command=self.on_checkbutton_change)
        self.c1.place(relx=0.5, rely=0.48, anchor="center")

        self.run_button = tk.Button(master, text="Run", command=self.run_script, padx=10, pady=5)
        self.run_button.place(relx=0.4, rely=0.82, anchor="center")

        self.quit_button = tk.Button(master, text="Quit", command=master.quit, padx=10, pady=5)
        self.quit_button.place(relx=0.6, rely=0.82, anchor="center")

        self.link_label = tk.Label(self.master, text="Concept Art by Sergey Musin", fg="blue", cursor="hand2")
        self.link_label.pack(side="bottom", anchor="se", padx=0, pady=0)
        self.link_label.configure(borderwidth=0, highlightthickness=0)
        self.link_label.bind("<Button-1>", lambda e: webbrowser.open_new(
            "https://www.artstation.com/prints/art_poster/RxM8/kenshi-concept-art-newrobot4"))

        # messagebox.showinfo("Warning", "Dont run the Renamer on the steam workshop folder directly!")

    def on_checkbutton_change(self):
        if self.var1.get() == 1:
            self.destination_button.config(state=tk.DISABLED)
        else:
            self.destination_button.config(state=tk.NORMAL)

    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
    
    def select_destination(self):
        self.destination_path = filedialog.askdirectory()

    def run_script(self):
        forbidden = ['system32', '233860']
        skipped_folders = []
        renamed_folders = []
        scroll_box = scrolledtext.ScrolledText(width=30, height=10)
        if self.folder_path is None:
            messagebox.showinfo("Error 404", "No folder selected")
        if (self.destination_path is None) or (self.var1.get() == 1):
            self.destination_path = self.folder_path

        for folder_name in os.listdir(self.folder_path):
            folder_path = os.path.join(self.folder_path, folder_name)

            # Check if the folder is a directory
            if not os.path.isdir(folder_path):
                continue

            # Check if the folder is in the forbidden list
            if any(s in folder_name for s in forbidden):
                continue

            found_mod_files = False
            mod_files = []
            for file_name in os.listdir(folder_path):
                if file_name.endswith('.mod'):
                    found_mod_files = True
                    mod_files.append(file_name)

            if len(mod_files) > 1:
                skipped_folders.append(folder_name + " (multiple .mod files on single folder)")
            elif found_mod_files and len(mod_files) == 1:
                # Create new folder then Move all files to the new folder
                mod_file_name = mod_files[0]
                new_folder_name = mod_file_name.rsplit('.mod', 1)[0]
                ###!!!!!!!!!!!!
                new_folder_path = os.path.join(self.destination_path, new_folder_name)
                if os.path.exists(new_folder_path):
                    skipped_folders.append(folder_name + " (folder exists)")
                    continue
                os.makedirs(new_folder_path, exist_ok=True)
                for file_name in os.listdir(folder_path):
                    old_path = os.path.join(folder_path, file_name)
                    new_path = os.path.join(new_folder_path, file_name)
                    shutil.move(old_path, new_path)
                renamed_folders.append(new_folder_name)
                shutil.rmtree(folder_path)
            else:
                skipped_folders.append(folder_name + " (no .mod file)")
        if len(skipped_folders) == 0:
            messagebox.showinfo("Finished", f"All {len(renamed_folders)} folders renamed!")
        else:
            for folder in skipped_folders:
                scroll_box.insert(tk.END, f"{folder}\n")
            messagebox.showinfo("Finished", f"{len(renamed_folders)} folders renamed!, Skipped {len(skipped_folders)} folders:", icon="info",
                                detail=scroll_box.get("1.0", tk.END))


# Get the path to the directory containing the bundled files
if hasattr(sys, '_MEIPASS'):
    # PyInstaller >= 1.6
    bundle_dir = sys._MEIPASS
else:
    # PyInstaller < 1.6
    bundle_dir = os.path.abspath(os.path.dirname(__file__))


icon_path = os.path.join(bundle_dir, "favicon.ico")
background_image_path = os.path.join(bundle_dir, "kenshiart.png")
roots = tk.Tk()
roots.geometry("400x200")
roots.iconbitmap(icon_path)
background_image = tk.PhotoImage(file=background_image_path)
background_label = tk.Label(roots, image=background_image)
background_label.place(relx=0.5, rely=0.5, anchor="center")
app = App(roots)
roots.mainloop()
