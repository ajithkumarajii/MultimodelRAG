import fitz
import os

def extract_images_from_page(pdf_path, page, image_dir, page_num):
    image_paths = []
    img_index = 0

    doc = fitz.open(pdf_path)
    for img_index, img in enumerate(page.get_images(full=True)):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_filename = f"page{page_num+1}_img{img_index+1}.png"
        image_path = os.path.join(image_dir, image_filename)
        with open(image_path, "wb") as image_file:
            image_file.write(image_bytes)
        
        image_paths.append(image_path)
    
    return image_paths

def parse_pdf(pdf_path):
    text_content = ""
    image_list = []
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    image_dir = f"./static/{pdf_name}_images"
    os.makedirs(image_dir, exist_ok=True)
    
    doc = fitz.open(pdf_path)
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        text_content += page.get_text() + "\n"
        image_list.extend(extract_images_from_page(pdf_path, page, image_dir, page_num))
    
    doc.close()
    return text_content, image_list
