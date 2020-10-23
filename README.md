# pptx2audio
Extracts m4a from pptx files

## Usage
download pptx2audio.py, put it in some folder with the pptx file(s), and run it.
    
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
    
