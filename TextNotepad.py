import tkinter as tk
from tkinter import filedialog, messagebox

def format_text(tag):
    try:
        current_tags = text.tag_names("sel.first")
        if tag in current_tags:
            text.tag_remove(tag, "sel.first", "sel.last")
        else:
            text.tag_add(tag, "sel.first", "sel.last")
    except tk.TclError:
        pass

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("HTML files", "*.html;*.htm")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text.delete(1.0, tk.END)
            text.insert(tk.END, content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("HTML files", "*.html;*.htm")])
    if file_path:
        with open(file_path, 'w') as file:
            content = text.get(1.0, tk.END)
            file.write(content)
        messagebox.showinfo("保存成功", f"文件已保存到 {file_path}")

root = tk.Tk()
root.title("简单文档编辑器")

# Toolbar frame
toolbar_frame = tk.Frame(root, bg="#282c34")
toolbar_frame.pack(side=tk.TOP, fill=tk.X)

bold_button = tk.Button(toolbar_frame, text="加粗", command=lambda: format_text('bold'), bg="#61dafb", fg="#282c34")
bold_button.pack(side=tk.LEFT, padx=5, pady=5)

italic_button = tk.Button(toolbar_frame, text="斜体", command=lambda: format_text('italic'), bg="#61dafb", fg="#282c34")
italic_button.pack(side=tk.LEFT, padx=5, pady=5)

underline_button = tk.Button(toolbar_frame, text="下划线", command=lambda: format_text('underline'), bg="#61dafb", fg="#282c34")
underline_button.pack(side=tk.LEFT, padx=5, pady=5)

left_align_button = tk.Button(toolbar_frame, text="左对齐", command=lambda: text.tag_configure('align_left', justify='left'), bg="#61dafb", fg="#282c34")
left_align_button.pack(side=tk.LEFT, padx=5, pady=5)

center_align_button = tk.Button(toolbar_frame, text="居中", command=lambda: text.tag_configure('align_center', justify='center'), bg="#61dafb", fg="#282c34")
center_align_button.pack(side=tk.LEFT, padx=5, pady=5)

right_align_button = tk.Button(toolbar_frame, text="右对齐", command=lambda: text.tag_configure('align_right', justify='right'), bg="#61dafb", fg="#282c34")
right_align_button.pack(side=tk.LEFT, padx=5, pady=5)

open_button = tk.Button(toolbar_frame, text="打开文件", command=open_file, bg="#61dafb", fg="#282c34")
open_button.pack(side=tk.RIGHT, padx=5, pady=5)

save_button = tk.Button(toolbar_frame, text="保存文件", command=save_file, bg="#61dafb", fg="#282c34")
save_button.pack(side=tk.RIGHT, padx=5, pady=5)

# Text editor frame
text = tk.Text(root, wrap=tk.WORD, undo=True, font=("Segoe UI", 16))
text.pack(expand=True, fill=tk.BOTH)

# Tag configurations
text.tag_configure('bold', font=('Segoe UI', 16, 'bold'))
text.tag_configure('italic', font=('Segoe UI', 16, 'italic'))
text.tag_configure('underline', font=('Segoe UI', 16, 'underline'))

root.mainloop()


