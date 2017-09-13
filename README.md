## Requirements

	sudo apt-get install pandoc

## Install

    sudo pip install markdown2html

## Usage

    usage: md2html [-h] [-v] [-k] [-s STYLE] files [files ...]

    positional arguments:
    files                 Files you want to convert

    optional arguments:
    -h, --help            show this help message and exit
    -v, --verbose         Display infos
    -k, --keep            Keep an existing output file (overwrites by default)
    -s STYLE, --style STYLE
                            Give a css file to be embedded in the html output

## Details

You can find the default css file used in `md2html/style-templates/style.css`.
