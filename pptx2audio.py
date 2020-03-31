import zipfile
from pathlib import Path

DEFAULT_AUDIO_EXTENSIONS = ['m4a']
DEFAULT_ARCHIVE_EXTENSIONS = ['pptx']


def parse_file(in_path: str, archive_extensions: list = None,
               audio_extensions: list = None) -> None:
    if not archive_extensions:
        archive_extensions = DEFAULT_ARCHIVE_EXTENSIONS
    if not audio_extensions:
        audio_extensions = DEFAULT_AUDIO_EXTENSIONS

    audio_extensions = [f".{ext}" for ext in audio_extensions]
    archive_extensions = [f".{ext}" for ext in archive_extensions]

    zip_paths = [file for file in Path(in_path).iterdir()
                 if Path(file).suffix in archive_extensions]

    for zip_path in zip_paths:
        with zipfile.ZipFile(zip_path) as zip_file:
            audio_files = [f for f in zip_file.filelist
                           if Path(f.filename).suffix in audio_extensions]

            for audio_file in audio_files:
                # zip_file.extract(audio_file)
                print(audio_file)


if __name__ == '__main__':
    parse_file(r'Lectures')
