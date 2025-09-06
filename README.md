# PDF Splitter

This project provides a Python script to split a large PDF (such as a book, article, or exam) into smaller PDFs based on custom page ranges. Each split is stored in its own folder, preventing file clutter and making it easy to organize multiple divided PDFs.

## Features
- Split a PDF into multiple parts according to your defined page ranges.
- Each input PDF has its own output folder inside `data/output_pdfs/`.
- User is prompted whether to **keep or delete** the original PDF after splitting.
- File names are automatically numbered and labeled for clarity.

## Project Structure
```
📂 pdf-splitter
 ┣ 📂 data
 ┃ ┣ 📂 input_pdfs     # Place your original PDFs here
 ┃ ┗ 📂 output_pdfs    # Split PDFs will be saved here, in subfolders named after the original PDF
 ┣ 📂 src
 ┃ ┗ split_pdf.py      # Main script
 ┣ .gitignore
 ┗ README.md
```

## Requirements
- Python 3.8+
- [PyPDF2]

Install dependencies:
```bash
pip install PyPDF2
```

## Usage
1. Place your original PDF file inside `data/input_pdfs/`.
2. Open `src/split_pdf.py` and edit the `ranges` list with the page intervals and names you want:
   ```python
   ranges = [
       (1, 15, "summary"),
       (16, 32, "chapter_1")
   ]
   ```
3. Update the `input_pdf` variable with the file path of your PDF inside `data/input_pdfs`:
   ```python
   input_pdf = os.path.join(input_folder, "my_book.pdf")
   ```
4. Run the script:
   ```bash
   python src/split_pdf.py
   ```
5. When the script finishes, it will ask:
   ```
   Do you want to keep the original PDF '../data/input_pdfs/my_book.pdf'? (y/n):
   ```
   - Type `y` to keep the original file.
   - Type `n` to delete it.

## Example Output
After splitting `my_book.pdf`:
```
📂 data/output_pdfs/my_book
 ┣ 01_summary.pdf
 ┗ 02_chapter_1.pdf
```

## Notes
- Page numbers are **1-based** (first page is page 1).
- Each original PDF has its own folder inside `output_pdfs` to avoid mixing files.
- The script ensures output folders exist before saving.

---
Easily organize and split your PDFs! 🚀
