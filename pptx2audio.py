import zipfile
from pathlib import Path


# todo consider filtering input files AND audio files by extension

def parse_file(in_path: str) -> None:
    zip_paths = [file for file in Path(in_path).iterdir() if zipfile.is_zipfile(file)]
    for file in zip_paths:
        with zipfile.ZipFile(file) as zf:
            zip_dir = zf.filelist
            audio_files = [f for f in zip_dir if f.filename.endswith('m4a')]
            for af in audio_files:
                zf.extract(af, 'Audio')
    pass


if __name__ == '__main__':
    parse_file(r'Lectures')
