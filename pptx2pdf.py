import aspose.slides as slides

def convert(pptx_path, pdf_path):
    with slides.Presentation(pptx_path) as presentation:
        presentation.save(pdf_path, slides.export.SaveFormat.PDF)

