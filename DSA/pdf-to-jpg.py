import fitz  # PyMuPDF
import os

pdf_path = r"C:\Users\lenovo\Documents\mcafile\PMC203_Assign_25020020573_ShaileshLingwal_compressed.pdf"
output_folder = r"C:\Users\lenovo\Documents\mcafile"

os.makedirs(output_folder, exist_ok=True)

doc = fitz.open(pdf_path)

for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    pix = page.get_pixmap(dpi=300)
    # This will save as 1.jpg, 2.jpg, 3.jpg inside mcafile
    pix.save(os.path.join(output_folder, f"{page_num + 1}.jpg"))

doc.close()
print("Sab pages alag ho gaye! Check mcafile folder")
