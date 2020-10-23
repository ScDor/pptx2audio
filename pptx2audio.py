#!/usr/bin/env python
# Extracts audio from pptx files saved in the same folder.
# all audio files in foo.pptx will be extracted into a new folder named foo.
__version__ = 1.0

import os
import zipfile
from pathlib import Path

DEFAULT_AUDIO_EXTENSIONS = ['m4a']
PPTX_EXTENSION = ".pptx"


def extract_audio(in_path: Path, audio_extensions: list = None) -> None:
    if audio_extensions is None:
        audio_extensions = DEFAULT_AUDIO_EXTENSIONS

    audio_extensions = [f".{ext}" for ext in audio_extensions]

    audio_count = 0

    zip_paths = [file for file in Path(in_path).iterdir()
                 if Path(file).suffix == PPTX_EXTENSION]

    for zip_path in zip_paths:
        print("searching audio files in", zip_path.name)
        with zipfile.ZipFile(zip_path) as zip_file:
            audio_files = [f for f in zip_file.filelist
                           if Path(f.filename).suffix in audio_extensions]
            dest_folder = Path(zip_path.stem)
            if not Path.exists(dest_folder):
                Path.mkdir(dest_folder)

            for audio_file in audio_files:
                # allows copying directly into dest, rather than into dest/ppt/audio/
                audio_file.filename = os.path.basename(audio_file.filename)

                zip_file.extract(audio_file, path=dest_folder)
                print("\t", "extracting ", dest_folder, audio_file.filename)
                audio_count += 1
    print()
    print("created by ScDor, October 2020\t\tsource: github.com/ScDor/pptx2audio")
    print(f"done extracting {audio_count} audio files\t\tpress enter to close")
    input()


if __name__ == '__main__':
    extract_audio(Path.cwd())
