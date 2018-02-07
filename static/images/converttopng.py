import sys
import subprocess
import os

def convert(file):
    filename, ext = os.path.splitext(file)
    if ext == '.pdf':
        print('converting ' + str(file))
        subprocess.call(['pdftoppm', '-singlefile', '-r', '300', '-png', file, filename])
        subprocess.call(['convert', filename + '.png', '-trim', filename + '.png'])

def main():
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            convert(sys.argv[i])
    else:
        for file in os.listdir('./'):
            convert(file)

if __name__ == '__main__':
    main()
