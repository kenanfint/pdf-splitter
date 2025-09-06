import os
from PyPDF2 import PdfReader, PdfWriter

# ==============================
# Function to split the PDF
# ==============================
def split_pdf(input_pdf, ranges, output_folder):
    # Create output folder if it does not exist
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


# ==============================
# Example usage
# ==============================
if __name__ == "__main__":
    input_pdf = "my_book.pdf"  # Replace with your PDF file
    output_folder = "output_pdfs"

    # Define the ranges (start_page, end_page, name)
    ranges = [
        (1, 10, "Summary"),
        (11, 20, "Chapter_1"),
        (21, 35, "Chapter_2"),
    ]

    split_pdf(input_pdf, ranges, output_folder)
