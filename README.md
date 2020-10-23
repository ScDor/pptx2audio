# pptx2audio
Extracts audio files from pptx presentations.

## Usage
If you have python installed, use [pptx2audio.py](https://github.com/ScDor/pptx2audio/blob/master/pptx2audio.py).
Otherwise, download [pptx2audio.exe](https://github.com/ScDor/pptx2audio/releases/latest/download/pptx2audio.exe).

Save pptx2audio in a folder where your pptx files are, and run it.
    
    .
    ├── ...
    ├── presentations           # working directory
    │   ├── foo.pptx            # some pptx file, preferably including audio files
    │   ├── bar.pptx            # another pptx file
    │   └── pptx2audio.py       
    └── ...
    
    
   After running the script, you'll have
   
    .
    ├── ...
    ├── presentations           # working directory
    │   ├── foo.pptx            # some pptx file, preferably including audio files
    │   ├── bar.pptx            
    |   ├── foo                 # a folder
    │   |   ├── audio1.m4a      # some audio file from that foo.pptx
    │   |   ├── audio2.m4a      
    │   |   └── ...
    │   └── bar
    │       ├── audio1.m4a
    │       └── ...
    |   
    └── ...
    
