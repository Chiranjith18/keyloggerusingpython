


# Python Keylogger with GUI (Educational)

A simple educational keylogger built in Python using:
- **pynput** for capturing keystrokes  
- **tkinter** for a basic GUI  

Keystrokes are saved to:
- `logs.json` – structured key events (Pressed / Held / Released)
- `logs.txt` – continuous plain-text keystrokes

⚠️ **Ethical Use Only**  
This project is for learning and cybersecurity awareness only.  
Do **not** run this on any system without explicit permission.


## How to Run (VS Code)

### 1. Download & Open
- Download the project ZIP from GitHub  
- Extract it (includes a preconfigured virtual environment: `keylogger-env`)  
- Open **VS Code → File → Open Folder** → select the project folder  


### 2. Activate Virtual Environment

**PowerShell (default):**
```powershell
keylogger-env\Scripts\Activate.ps1
````

If blocked:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
keylogger-env\Scripts\Activate.ps1
```

**Command Prompt (cmd):**

```cmd
keylogger-env\Scripts\activate
```

You should see:

```
(keylogger-env)
```

> Required packages are already installed.

---

### 3. Run the Program

```bash
python keylogger.py
```

* A GUI window **“Keylogger Page”** opens
* Click **“Start Keylogger”** to begin logging
* Logs are written to `logs.json` and `logs.txt`

Stop logging by closing the window or pressing `Ctrl + C`.

---

### 4. Deactivate Environment

```bash
deactivate
```

---

## Notes

* Educational use only
* Demonstrates keyboard event handling, basic GUI, and logging in Python
* Always follow legal and ethical guidelines



