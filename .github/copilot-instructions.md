## Quick orientation for AI coding agents

This is a small, single-developer desktop project that uses CSV files as the primary datastore and Tkinter for a simple GUI. The goal of this file is to provide the minimal, concrete context an AI agent needs to make safe, useful edits without guessing project conventions.

### Big picture
- App type: local desktop inventory viewer/editor (not a web service). UI is built with `tkinter` and images are loaded with `tk.PhotoImage`.
- Data store: CSV files in the repository root are the single source of truth. Key files: `JJInventoryDatabase.csv`, `JJItemImages.csv`, `JJUserDatabase.csv`.
- Main components:
  - `InventoryDatabase.py` — reads `JJInventoryDatabase.csv` and exposes two common shapes: `csv_w_label` (list of dicts via `csv.DictReader`) and `data_values_2D` (list of rows via `csv.reader`). Example use: `InvData.csv_w_label[2]` returns a dict for the 3rd item.
  - `ItemImages.py` — loads `JJItemImages.csv` into `image_data` and exposes `item_image_paths(item_ID)` which returns a list of image file paths (strings) for that item ID.
  - `InventoryDatabaseDisplay.py` — example UI file that builds Tk windows, writes `Inv_Data.csv_w_label` into a `tk.Text`, and demonstrates both a side-by-side image display and a slideshow using `item_image_paths(1001)`.
  - `Main.py` — small test script that imports `InventoryDatabase` and prints some values; useful for quick, headless checks.

### Project-specific conventions & patterns
- CSV-as-DB: code assumes CSV files are present in the repository root and opens them with relative paths (e.g., `open('JJInventoryDatabase.csv')`). Always run code from the project root or adjust paths.
- Two data shapes from CSVs:
  - `csv_w_label` (list of dicts): helpful for keyed access by column name. Created by `InventoryDatabase.read_item_dicts`.
  - `data_values_2D` (list of lists): raw rows including header row in index 0.
- Image lookup: `ItemImages.item_image_paths(item_ID)` expects the first column of `JJItemImages.csv` to be the item ID. Returned paths are used directly with `tk.PhotoImage(file=path)`.
- UI instantiation: the repo sometimes creates multiple `tk.Tk()` instances (e.g., `InventoryDatabaseDisplay.py` creates `tk` and later `root = tk.Tk()`). Be careful when refactoring GUI code — prefer a single root window when combining components.
- Python version hint: compiled files in `__pycache__` indicate CPython 3.13 (`cpython-313`), so target a modern Python 3.x interpreter (3.11+ recommended). No third-party packages are required; all imports are from the standard library (`csv`, `tkinter`).

### How to run / developer workflows
- Quick print-only smoke test (no GUI):
  - Run `python Main.py` from repository root to exercise `InventoryDatabase` parsing.
- Run the GUI example(s):
  - `python InventoryDatabaseDisplay.py` — opens a simple text view of CSV rows and separate windows that show image slideshow/side-by-side displays.
- Debugging notes:
  - If images fail to load, ensure file paths in `JJItemImages.csv` are correct and that `tk.PhotoImage` supports the format. Run from repo root so relative paths resolve.

### Example patterns for small edits
- To add a new field to the in-memory inventory model, update `JJInventoryDatabase.csv` header, then rely on `InventoryDatabase.read_item_dicts` — new columns appear as keys in `csv_w_label` dicts.
- To add images for an item, append a row to `JJItemImages.csv` where column 0 is the item ID and subsequent columns are file paths. `item_image_paths(item_ID)` will return them automatically.
- When changing UI code, check for multiple `Tk()` usages in `InventoryDatabaseDisplay.py` and `ItemImages.py` and consolidate to a single root when integrating features.

### Files to inspect first for context
- `InventoryDatabase.py` — CSV reading and the canonical data shapes.
- `ItemImages.py` — CSV parsing for images and `item_image_paths`.
- `InventoryDatabaseDisplay.py` — how returned data is used in the UI (Text widget, PhotoImage, slideshow).
- `Main.py` — quick smoke test usage.
- CSV files: `JJInventoryDatabase.csv`, `JJItemImages.csv`, `JJUserDatabase.csv` — examine headers and sample rows to understand field names and ordering.

If anything in this doc is incomplete or you want extra examples (for example, the exact CSV header names or a small unit-test harness), tell me which area to expand and I'll update this file.
