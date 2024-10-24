import os
import csv
from tqdm import tqdm
from collections import Counter

# Block the following formats.
IMAGE = ["png", "jpg", "jpeg", "gif"]
VIDEO = ["mp4", "jfif"]
DOC = [
    "key",
    "PDF",
    "pdf",
    "docx",
    "xlsx",
    "pptx",
]
AUDIO = ["flac", "ogg", "mid", "webm", "wav", "mp3"]
ARCHIVE = ["jar", "aar", "gz", "zip", "bz2"]
MODEL = ["onnx", "pickle", "model", "neuron"]
OTHERS = [
    "npy",
    "index",
    "inv",
    "index",
    "DS_Store",
    "rdb",
    "pack",
    "idx",
    "glb",
    "gltf",
    "len",
    "otf",
    "unitypackage",
    "ttf",
    "xz",
    "pcm",
    "opus",
]
ANTI_FORMATS = tuple(IMAGE + VIDEO + DOC + AUDIO + ARCHIVE + OTHERS)

REPO_DIRECTORY="repos"

def get_extensions(directory):
    """Compiles a comma separated list of the file extensions + count"""
    file_paths = []
    file_extensions = []
    print("starting...")
    # Recursively find all files within the directory
    for root, _, files in os.walk(directory):
        path = root.split(os.path.sep)[1:]
        if len(path) > 1:
            root = path[0]
            for file in files:
                file_path = os.path.join(os.path.sep.join(path), file)
                if not file_path.endswith(ANTI_FORMATS) and all(
                    k not in file_path for k in [".git", "__pycache__", "xcodeproj"]
                ):
                    file_paths.append(file_path)
                    
    for _, path in enumerate(tqdm(file_paths)):
        _, file_extension = os.path.splitext(path)
        file_extensions.append(file_extension)

    extensions_dict = dict(Counter(file_extensions))
    return extensions_dict

if __name__ == "__main__":
        extensions_dict = get_extensions(REPO_DIRECTORY)
        print('finished extracting extensions')
        with open('extensions.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            for k, v in extensions_dict.items():
                 writer.writerow([k, v])

