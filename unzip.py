import os
import fnmatch
import zipfile

def unzip(file:str, destination:str):
    try:
        with zipfile.ZipFile(file, 'r') as zip_ref:
            zip_ref.extractall(destination)
    except zipfile.BadZipFile:
        print("Error: Invalid zipfile format.")
    except FileNotFoundError:
        print(f"Error: File not found - {file}.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    origin = os.path.abspath('./prezipped') #input('origin dir :')
    result = os.path.abspath('./unzipped') #input('result dir :')
    archive_type = 'zip' #input('archive type :')
    zip_files = []
    for root, dirs, files in os.walk(origin):
        for file in fnmatch.filter(files, f'*.{archive_type}'):
            zip_files.append(os.path.join(root, file))
    
    for file in zip_files:
        destination = str(file).replace(origin, result).replace(f'.{archive_type}', '')
        if archive_type == 'zip':
            unzip(file=file, destination=destination)
            print(destination)