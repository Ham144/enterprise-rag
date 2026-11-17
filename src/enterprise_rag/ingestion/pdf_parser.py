from io import BytesIO
from pypdf import PdfReader

def extract_pdf(pdf_content: bytes) -> list[dict]:
    
    extracted_pages = []
    reader = PdfReader(BytesIO(pdf_content)) 
    if reader.is_encrypted:
       raise ValueError("file di kunci") 
    
    
    for page_idx, page in enumerate(reader.pages, start=1):
        content = page.extract_text() or ""
        if not content:
            continue
        extracted_pages.append({
            "halaman": page_idx,
            "content": content
        })
    
    return extracted_pages