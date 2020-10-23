# pptx2audio
Extracts audio files from pptx presentations.

## Usage
If you have python installed, use [pptx2audio.py](https://github.com/ScDor/pptx2audio/blob/master/pptx2audio.py).

If you don't (or don't know what Python is), download [this file](https://github.com/ScDor/pptx2audio/releases/latest/download/pptx2audio.exe).

Save pptx2audio in a folder where your pptx files are, and run it.
    
    .
    ├── ...
    ├── presentations           # folder
    │   ├── foo.pptx            # some pptx file, preferably including audio files
    │   ├── bar.pptx            
    │   └── pptx2audio.py       # or pptx2audio.exe
    └── ...
    
    
   After running the script, the folder will look like this:
   
    .
    ├── ...
    ├── presentations           
    │   ├── foo.pptx            
    │   ├── foo.pptx            
    │   ├── pptx2audio.py        
    │   | 
    |   ├── foo                 # a newly-created folder
    │   |   ├── audio1.m4a      # some audio file from foo.pptx
    │   |   ├── audio2.m4a      
    │   |   └── ...             
    │   | 
    │   └── bar                 # a separate folder for each pptx file
    │       ├── audio1.m4a      
    │       └── ...
    |   
    └── ...
    
