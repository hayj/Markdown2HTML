# coding: utf-8

import sys


import argparse
import os.path
from systemtools.location import *
from systemtools.file import fileToStr, strToFile
import pypandoc

def mdFileNameToHtmlFileName(mdFilePath):
    return absPath(mdFilePath) + ".html"

def convert():
    # Get args:"
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
        htmlBegin = "<!DOCTYPE html><html><head><meta charset=\"UTF-8\"><title>" + title + "</title>" +  style + "</head><body>\n"
        htmlEnd = "\n</body></html>"
        html = htmlBegin + html + htmlEnd
        print(("Writing " + outputPath))
        strToFile(html, outputPath)
        
if __name__ == '__main__':
    convert()
    # Then we convert all files:
    
