from pdfreader import PDFDocument

fd = open("./azure-devops-get-started-azure-devops-2022.pdf", "rb")
doc = PDFDocument(fd)
page = next(doc.pages())
sorted(page.Resources.Font.keys())
font = page.Resources.Font['F15']
font_info = font.Subtype, font.BaseFont, font.Encoding
font_file = font.FontDescriptor.FontFile

data = font_file.filtered
with open("sample-font.type1", "wb") as f:
    f.write(data)
