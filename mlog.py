import json
import os
import datetime
import argparse

# Directory to store memory logs
LOG_DIR = "memories"
os.makedirs(LOG_DIR, exist_ok=True)

def get_log_file():
    """Returns the JSON file path for today's log."""
    today = datetime.date.today().strftime("%Y-%m-%d")
    return os.path.join(LOG_DIR, f"{today}.json")

def load_logs():
    """Loads today's logs from the JSON file."""
    log_file = get_log_file()
    if os.path.exists(log_file):
        try:
            with open(log_file, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("⚠️ Error: Log file is corrupted. Starting a new log.")
    return {"general": [], "personal": [], "restricted": True}

def save_logs(logs):
    """Saves logs back to the JSON file."""
    log_file = get_log_file()
    try:
        with open(log_file, "w") as f:
            json.dump(logs, f, indent=4)
    except IOError as e:
        print(f"⚠️ Error: Unable to save logs. {e}")

def log_memory(text, category):
    """Logs a memory under the specified category."""
    if not text.strip():
        print("⚠️ Error: Memory text cannot be empty.")
        return
    logs = load_logs()
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    logs[category].append({"time": timestamp, "text": text})
    save_logs(logs)
    print(f"✅ Memory logged under '{category}': {text}")

def view_logs():
    """Displays today's logs."""
    logs = load_logs()
    print("\nToday's Memories:")
    for category, entries in logs.items():
        if category == "restricted":
            continue
        print(f"\n[{category.upper()}]")
        for idx, entry in enumerate(entries, start=1):
            print(f"{idx}. [{entry['time']}] {entry['text']}")

def delete_memory(category, index=None):
    """Deletes a memory from the specified category."""
    logs = load_logs()
    if index is None:
        # Delete all memories in the category
        logs[category] = []
        save_logs(logs)
        print(f"✅ All memories deleted from '{category}'.")
    else:
        # Delete a specific memory by index
        if 1 <= index <= len(logs[category]):
            deleted_memory = logs[category].pop(index - 1)
            save_logs(logs)
            print(f"✅ Memory deleted from '{category}': {deleted_memory['text']}")
        else:
            print(f"⚠️ Error: Invalid index for '{category}'.")

def main():
    parser = argparse.ArgumentParser(description="Memory Logger")
    parser.add_argument("--log", type=str, help="Log a new memory")
    parser.add_argument("--c", type=str, choices=["g", "p"], default="g", help="Category of memory (g for general, p for personal)")
    parser.add_argument("--view", action="store_true", help="View today's memories")
    parser.add_argument("--delete", type=int, nargs="?", const=-1, help="Delete a memory by index (or all memories if no index is provided)")
    args = parser.parse_args()

    if args.log:
        # Map 'g' to 'general' and 'p' to 'personal'
        category_map = {"g": "general", "p": "personal"}
        category = category_map[args.c]
        log_memory(args.log, category)
    elif args.view:
        view_logs()
    elif args.delete is not None:
        category_map = {"g": "general", "p": "personal"}
        category = category_map[args.c]
        if args.delete == -1:
            # Delete all memories in the category
            delete_memory(category)
        else:
            # Delete a specific memory by index
            delete_memory(category, args.delete)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
