import os 
from pdf2image import convert_from_path

pdf_dir = 'C:\\Users\\welog\\OneDrive\\Desktop\\ResearchUCSD\\Tesseract2Ubuntu\\Nupepa_Folder_for_LLM\\ke_au_hou\\july\\pdfs'
output_dir = 'C:\\Users\\welog\\OneDrive\\Desktop\\ResearchUCSD\\Tesseract2Ubuntu\\Nupepa_Folder_for_LLM\\ke_au_hou\\july\\images'

# Loop through all files in the PDF directory
for filename in os.listdir(pdf_dir):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_dir, filename)

        # Convert the PDF to a list of images (one per page)
        images = convert_from_path(pdf_path)

        # Save each page as a JPEG image
        for i, image in enumerate(images):
            # Create the output file path for each page
            output_file = os.path.join(output_dir, f"{filename[:-4]}_page_{i + 1}.jpg")
            
            # Save the image as a JPEG file
            image.save(output_file, "JPEG")
            print(f"Saved: {output_file}")

# if you want to add to windows you need to pip install pdf2images
# after that due to dependency of pdf2image on poppler go to 
# https://github.com/oschwartz10612/poppler-windows/releases
# once here you can extract the release.*.zip and placing the extracted into a folder
# recommedation C:\poppler (note you can rename the release to poppler without breaking anything)
# once this look through the poppler directory to find the path to \bin, copy this path
# with this path you can go to environment varialbles adding this path which should look like
# C:\poppler\*\bin assuming an additonal directory or C:\poppler\bin if none
# save and then run