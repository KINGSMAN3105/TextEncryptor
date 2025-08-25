import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import os

# ------------------ KEY HANDLING ------------------ #
KEY_FILE = "secret.key"

def load_key():
    """Load or generate encryption key"""
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        return key

key = load_key()
cipher = Fernet(key)

# ------------------ ENCRYPT FUNCTION ------------------ #
def encrypt_text():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter some text to encrypt.")
        return

    encrypted = cipher.encrypt(text.encode()).decode()
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted)

def save_encrypted():
    encrypted = output_text.get("1.0", tk.END).strip()
    if not encrypted:
        messagebox.showwarning("Warning", "No encrypted text to save.")
        return

    file = filedialog.asksaveasfilename(defaultextension=".txt",
                                        filetypes=[("Text files", "*.txt")],
                                        title="Save Encrypted File")
    if file:
        with open(file, "w") as f:
            f.write(encrypted)
        messagebox.showinfo("Saved", f"Encrypted file saved as {file}")

# ------------------ DECRYPT FUNCTION ------------------ #
def choose_encrypted_file():
    file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")],
                                      title="Choose Encrypted File")
    if file:
        with open(file, "r") as f:
            encrypted_content = f.read().strip()
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, encrypted_content)
        messagebox.showinfo("File Loaded", f"Loaded encrypted file: {file}")

def decrypt_text():
    encrypted = output_text.get("1.0", tk.END).strip()
    if not encrypted:
        messagebox.showwarning("Warning", "No encrypted text to decrypt.")
        return
    try:
        decrypted = cipher.decrypt(encrypted.encode()).decode()
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, decrypted)
    except Exception:
        messagebox.showerror("Error", "Invalid or corrupted encrypted text.")

# ------------------ GUI SETUP ------------------ #
root = tk.Tk()
root.title("Creative Text Encryptor")
root.geometry("700x500")
root.config(bg="#1e1e2e")

# Input Text
tk.Label(root, text="Enter Text to Encrypt:", bg="#1e1e2e", fg="white", font=("Arial", 12)).pack(pady=5)
input_text = tk.Text(root, height=5, width=70, wrap="word", font=("Arial", 11))
input_text.pack(pady=5)

# Buttons (Encrypt + Save)
frame1 = tk.Frame(root, bg="#1e1e2e")
frame1.pack(pady=10)
tk.Button(frame1, text="Encrypt", command=encrypt_text, bg="#4CAF50", fg="white", font=("Arial", 11), width=12).grid(row=0, column=0, padx=5)
tk.Button(frame1, text="Save Encrypted File", command=save_encrypted, bg="#2196F3", fg="white", font=("Arial", 11), width=20).grid(row=0, column=1, padx=5)

# Buttons (Choose File + Decrypt)
frame2 = tk.Frame(root, bg="#1e1e2e")
frame2.pack(pady=10)
tk.Button(frame2, text="Choose Encrypted File", command=choose_encrypted_file, bg="#FF9800", fg="white", font=("Arial", 11), width=20).grid(row=0, column=0, padx=5)
tk.Button(frame2, text="Decrypt", command=decrypt_text, bg="#F44336", fg="white", font=("Arial", 11), width=12).grid(row=0, column=1, padx=5)

# Output Text
tk.Label(root, text="Output (Encrypted/Decrypted):", bg="#1e1e2e", fg="white", font=("Arial", 12)).pack(pady=5)
output_text = tk.Text(root, height=10, width=70, wrap="word", font=("Arial", 11))
output_text.pack(pady=5)

root.mainloop()
