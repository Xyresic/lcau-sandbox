import os
import pypdfium2 as pdfium
import geograpy

dir_path = 'LCAU_data'
directory = os.fsencode(dir_path)

cities = set()
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    file_path = os.path.join(dir_path, filename)
    text = ''

    if filename.endswith('.txt'):
        with open(file_path, encoding='utf-8') as f:
            text = f.read()
    elif filename.endswith('.pdf'):
        pdf = pdfium.PdfDocument(file_path)
        for page in pdf:
            text_page = page.get_textpage()
            text += text_page.get_text_range() + '\n'

    places = geograpy.get_geoPlace_context(text=text)
    cities |= set(places.address_strings)
    print(filename)

with open('cities_raw.txt', 'w') as f:
    for city in cities:
        f.write(city + '\n')
