# coding: utf-8

# cd /home/hayj/Workspace/Python/Organization/Markdown2HTML/md2html/ && pew in markdown2html-venv python convert.py -s truc.css toto.md *.md
# cd /home/hayj/Workspace/Python/Organization/Markdown2HTML/md2html/ && pew in markdown2html-venv python convert.py ../README.md

from __future__ import division, print_function, absolute_import


import sys
reload(sys)  
sys.setdefaultencoding('utf8')


import argparse
import os.path
from systemtools.location import *
from systemtools.file import fileToStr, strToFile
import pypandoc


# from md2html.utils import *

def mdFileNameToHtmlFileName(mdFilePath):
    return absPath(mdFilePath) + ".html"

def convert():
    # Get args:
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='+', help='Files you want to convert')
    parser.add_argument("-v", "--verbose", help="Display infos", action="store_true")
    parser.add_argument("-k", "--keep", help="Keep an existing output file (overwrites by default)", action="store_true")
    parser.add_argument("-s", "--style", help="Give a css file to be embedded in the html output")
    args = parser.parse_args()

    # Convert all relative paths to absolute paths:
    newFileList = []
    for filePath in args.files:
        newFileList.append(absPath(filePath))
    args.files = newFileList
    # For each file, we check if it exists and 
    newFileList = []
    for filePath in args.files:
        if isFile(filePath):
            newFileList.append(filePath)
    args.files = newFileList
    
    # If we are not allowed to override and the output exists, skip this file:
    if args.keep:
        newFileList = []
        for filePath in args.files:
            if not isFile(mdFileNameToHtmlFileName(filePath)):
                newFileList.append(filePath)
        args.files = newFileList
        
    # if there are no css style given, we set the default style in the lib:
    styleTemplatePath = getExecDirectory(__file__) + "/style-templates/style.css"
    if args.style is not None and isFile(args.style):
        styleTemplatePath = args.style
    
    # We get the css:
    css = fileToStr(styleTemplatePath)
        
    # Convert to html:
    for filePath in args.files:
        outputPath = mdFileNameToHtmlFileName(filePath)
        html = pypandoc.convert(filePath, 'html')
        title = filePath.split("/")[-1]
        style = "<style>" + css + "</style>"
        htmlBegin = u"<!DOCTYPE html><html><head><meta charset=\"UTF-8\"><title>" + title + u"</title>" +  style + u"</head><body>\n"
        htmlEnd = u"\n</body></html>"
        html = htmlBegin + html + htmlEnd
        print("Writing " + outputPath)
        strToFile(html, outputPath)
        # print(html)
        
    # TODO OOOOOO tester ça

if __name__ == '__main__':
    convert()
    # Then we convert all files:
    