# Memory Logger 

A simple command-line tool to log, view, and delete daily memories for AI training purposes. The program categorizes memories into "general" and "personal" and saves them as JSON files.

## Features

- ✅ Log memories under "general" or "personal" categories.
- ✅ View logged memories for the current day.
- ✅ Delete specific or all memories in a category.
- ✅ Stores data in JSON format for easy retrieval.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/memory-logger.git
   cd memory-logger
   ```
2. Run the script using Python:
   ```bash
   python memory_logger.py --log "Your memory here" --c g  # Logs a general memory
   python memory_logger.py --view  # View today's logs
   ```

## Usage

### Log a memory
```bash
python memory_logger.py --log "Had coffee with a friend" --c p
```

### View memories
```bash
python memory_logger.py --view
```

### Delete a specific memory (e.g., entry 2 in general category)
```bash
python memory_logger.py --delete 2 --c g
```

### Delete all personal memories
```bash
python memory_logger.py --delete --c p
```

---

Feel free to contribute and improve the project! 🚀

