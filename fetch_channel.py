import requests
import json

# Source URL
URL = "https://hidden-boat-b444.saqlainhaider8198.workers.dev/"
OUTPUT_FILE = "channels.json"

def main():
    try:
        response = requests.get(URL)
        response.raise_for_status()
        data = response.json()

        # Save file
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print("✅ channels.json updated successfully")
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()
