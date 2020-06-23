# NHXHide
NHXHide is a tool written in Python used to penetrate data into image files and reading from them.

# New Features!

  - Support for reading data or extracting data to external sources (files).
  - Support for Binaries and large external files.

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

Using this tool is simple. One argument is required, which is the image file to read or write data to, and the second optional argument is the file to read the data from, to be written to image, or the file for writng back the extracted data from the image file.

```sh
$ NHXHide <image file> <optional:data file>
```
