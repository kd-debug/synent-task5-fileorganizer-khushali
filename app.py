import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from organizer import organize_folder

class FileOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart File Organizer")
        self.root.geometry("600x450")
        self.root.resizable(False, False)
        
        # Color Scheme
        self.bg_color = "#f0f2f5"
        self.primary_color = "#4a90e2"
        self.accent_color = "#ffffff"
        self.text_color = "#333333"
        
        self.root.configure(bg=self.bg_color)
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main Container
        main_frame = tk.Frame(self.root, bg=self.bg_color, padx=30, pady=30)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        header_label = tk.Label(
            main_frame, 
            text="File Organizer", 
            font=("Helvetica", 24, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        )
        header_label.pack(pady=(0, 10))
        
        subtitle_label = tk.Label(
            main_frame,
            text="Select a folder to automatically organize your files by type.",
            font=("Helvetica", 10),
            bg=self.bg_color,
            fg="#666666"
        )
        subtitle_label.pack(pady=(0, 30))
        
        # Folder Selection Area
        selection_frame = tk.Frame(main_frame, bg=self.bg_color)
        selection_frame.pack(fill=tk.X, pady=10)
        
        self.path_var = tk.StringVar()
        self.path_entry = tk.Entry(
            selection_frame, 
            textvariable=self.path_var,
            font=("Helvetica", 11),
            bd=1,
            relief=tk.FLAT,
            highlightthickness=1,
            highlightbackground="#cccccc"
        )
        self.path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10), ipady=5)
        
        browse_btn = tk.Button(
            selection_frame,
            text="Browse",
            command=self.browse_folder,
            font=("Helvetica", 10, "bold"),
            bg=self.primary_color,
            fg="white",
            relief=tk.FLAT,
            padx=20,
            cursor="hand2"
        )
        browse_btn.pack(side=tk.RIGHT)
        
        # Action Button
        self.organize_btn = tk.Button(
            main_frame,
            text="Organize Files",
            command=self.start_organization,
            font=("Helvetica", 12, "bold"),
            bg="#2ecc71",
            fg="white",
            relief=tk.FLAT,
            pady=10,
            cursor="hand2",
            state=tk.DISABLED
        )
        self.organize_btn.pack(fill=tk.X, pady=20)
        
        # Stats/Log Area
        log_frame = tk.LabelFrame(
            main_frame, 
            text="Results", 
            font=("Helvetica", 10, "bold"),
            bg=self.bg_color,
            fg=self.text_color,
            padx=10,
            pady=10
        )
        log_frame.pack(fill=tk.BOTH, expand=True)
        
        self.stats_text = tk.Text(
            log_frame,
            height=8,
            font=("Consolas", 10),
            bg=self.accent_color,
            bd=0,
            padx=10,
            pady=10
        )
        self.stats_text.pack(fill=tk.BOTH, expand=True)
        self.stats_text.config(state=tk.DISABLED)
        
        # Path change listener
        self.path_var.trace_add("write", self.on_path_change)

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.path_var.set(folder_selected)
            
    def on_path_change(self, *args):
        path = self.path_var.get()
        if os.path.isdir(path):
            self.organize_btn.config(state=tk.NORMAL)
        else:
            self.organize_btn.config(state=tk.DISABLED)
            
    def log(self, message):
        self.stats_text.config(state=tk.NORMAL)
        self.stats_text.insert(tk.END, message + "\n")
        self.stats_text.see(tk.END)
        self.stats_text.config(state=tk.DISABLED)
        
    def clear_log(self):
        self.stats_text.config(state=tk.NORMAL)
        self.stats_text.delete(1.0, tk.END)
        self.stats_text.config(state=tk.DISABLED)

    def start_organization(self):
        target_path = self.path_var.get()
        if not target_path:
            return
            
        try:
            self.clear_log()
            self.log(f"Scanning: {target_path}")
            
            results = organize_folder(target_path)
            
            total_files = sum(results.values())
            
            if total_files == 0:
                self.log("No files found to organize.")
                messagebox.showinfo("Done", "No files found to organize.")
            else:
                self.log("-" * 30)
                self.log(f"Success! Organized {total_files} files:")
                for cat, count in results.items():
                    if count > 0:
                        self.log(f"  • {cat}: {count}")
                self.log("-" * 30)
                messagebox.showinfo("Success", f"Successfully organized {total_files} files!")
                
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.log(f"ERROR: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerApp(root)
    root.mainloop()
