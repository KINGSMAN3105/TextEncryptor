# Creative Text Encryptor

A simple and secure Python-based tool with a **graphical interface** (Tkinter) that allows you to **encrypt and decrypt text files** using the `cryptography` library (`Fernet` encryption).

---

## 🚀 Features
- Encrypt any text using AES-based Fernet encryption.
- Decrypt previously encrypted text.
- Save encrypted text to a `.txt` file.
- Load an encrypted file and decrypt it.
- User-friendly **Tkinter GUI** with styled buttons.

---

## 🛠 Requirements
- Python 3.8+
- `cryptography` library

Install dependencies with:
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage
1. Run the program:
   ```bash
   python main.py
   ```

2. Enter your text in the input box and click **Encrypt**.  
3. Save the encrypted text as a file, or copy it directly.  
4. Load an encrypted file and click **Decrypt** to reveal the original text.  

---

## 📂 Project Structure
```
.
├── main.py          # Main program with GUI
├── requirements.txt # Dependencies
├── README.md        # Project documentation
└── secret.key       # Auto-generated encryption key
```

---

## 🔒 Security Notes
- A secret key (`secret.key`) is generated automatically and reused for encryption/decryption.
- Do not share your `secret.key` with others unless you want them to decrypt your files.

---

## 📸 Screenshot
(*Add a screenshot of the GUI here for better presentation.*)

---

## 📜 License
This project is open-source and available under the MIT License.
