# NHXHide
NHXHide is a tool written in Python used to penetrate data into multimedia files and reading from them.

# New Features!

  - Support for reading data or extracting data to external sources (files).
  - Support for Binaries and large external files.
  - Support for most Multimedia sources such as Image files (png, jpg, bmp etc), Video files (mp4, mkv etc) and Audio Files (mp3, avi etc).
  - Support for writing more than one file to the multimedia destination (in the form of writing a whole folder, adding multiple files inside the folder and specifying the folder as external source for data to be written to multimedia destination).

### Installation

NHXHide requires Python 3+ to run.

To install on Linux or OSX, install:

```sh
$ git clone https://github.com/chmuhammadsohaib/NHXHide.git
$ cd NHXHide
$ chmod +x setup.sh 
$ ./setup.sh
```

For Windows, directly download NHXHide .py and use it via python3 shell:

```sh
$ python3 NHXHide.py
```

### Usage

Using this tool is simple. One argument is required, which is the multimedia file to read or write data to, and the second optional argument is the file to read the data from, to be written to multimedia, or the file for writng back the extracted data from the multimedia file.

```sh
$ NHXHide <multimedia file> <optional:data file\folder>
```
