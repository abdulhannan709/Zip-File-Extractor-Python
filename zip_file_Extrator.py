from zipfile import ZipFile
filename="Heart.zip"
with ZipFile(filename, 'r') as zip:
    zip.printdir()
    print('Extracting all the files...')
    zip.extractall()
    print('Done')