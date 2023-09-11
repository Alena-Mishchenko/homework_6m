import sys
from pathlib import Path


images = list()
videos = list()
documents = list()
music = list()
folders = list()
archives = list()
others = list()
unknown = set()
extensions = set()

registered_extensions = {
    'JPEG': images,
    'JPG': images,
    'PNG': images,
    'SVG': images,
    'AVI': videos,
    'MP4': videos,
    'MOV': videos,
    'MKV': videos,
    'DOC': documents,
    'DOCX': documents,
    'TXT': documents,
    'PDF': documents,
    'XLSX': documents,
    'PPTX': documents,
    'MP3': music,
    'OGG': music,
    'WAV': music,
    'AMR': music,
    'ZIP': archives,
    'GZ': archives,
    'TAR': archives
}


def get_extensions(file_name):
    return Path(file_name).suffix[1:].upper()


def scan(folder):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('archives', 'music', 'documents', 'videos', 'images'):
                folders.append(item)
                scan(item)
            continue

        extension = get_extensions(file_name=item.name)
        new_name = folder/item.name
        if not extension:
            others.append(new_name)
        else:
            try:
                container = registered_extensions[extension]
                extensions.add(extension)
                container.append(new_name)
            except KeyError:
                unknown.add(extension)
                others.append(new_name)


if __name__ == '__main__':
    path = sys.argv[1]
    print(f"Start in {path}")

    arg = Path(path)
    scan(arg)
    # print(f'images: {images}\n')
    # print(f'documents: {documents}\n')
    # print(f'archives: {archives}\n')
    # print(f'music: {music}\n')
    # print(f'videos: {videos}\n')
    # print(f'unknown: {others}\n')
    # print(f'All extensions: {extensions}\n')
    # print(f'Unknown extensions: {unknown}\n')
