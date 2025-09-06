import os
import shutil
from PyPDF2 import PdfReader, PdfWriter

# ==============================
# Function to split the PDF
# ==============================
def split_pdf(input_pdf, ranges, output_root):
    # Extract base name (without extension) for folder organization
    base_name = os.path.splitext(os.path.basename(input_pdf))[0]
    output_folder = os.path.join(output_root, base_name)

    # Create a specific folder for this PDF
    os.makedirs(output_folder, exist_ok=True)

    # Load the PDF
    reader = PdfReader(input_pdf)

    for idx, (start, end, name) in enumerate(ranges, start=1):
        writer = PdfWriter()

        # Add pages from the range
        for page in range(start - 1, end):  # -1 because PyPDF2 uses 0-based index
            writer.add_page(reader.pages[page])

        # Output file name
        file_name = f"{idx:02d}_{name}.pdf"
        output_path = os.path.join(output_folder, file_name)

        # Save the PDF
        with open(output_path, "wb") as f:
            writer.write(f)

        print(f"File saved: {output_path}")

    return output_folder


# ==============================
# Example usage
# ==============================
if __name__ == "__main__":
    # Project folder structure
    input_folder = os.path.join("..", "data", "input_pdfs")
    output_root = os.path.join("..", "data", "output_pdfs")

    # PDF file inside input_pdfs
    input_pdf = os.path.join(input_folder, "prova-2dia.pdf")

    # Define the ranges (start_page, end_page, name)
    ranges = [
        (1, 15, "nature_science"),
        (16, 32, "math")
    ]

    # Split PDF
    output_folder = split_pdf(input_pdf, ranges, output_root)

    # Ask user if original PDF should be deleted
    choice = input(f"Do you want to keep the original PDF '{input_pdf}'? (y/n): ").strip().lower()
    if choice == "n":
        os.remove(input_pdf)
        print(f"Original PDF deleted: {input_pdf}")
    else:
        print("Original PDF kept.")