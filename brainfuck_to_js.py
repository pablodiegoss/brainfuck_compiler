import argparse
from getch import getche

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Brainfuck filename")
parser.add_argument("-o", help="Filename to be generated")

args = parser.parse_args()

INPUT_FILENAME = args.filename
OUTPUT_FILENAME = args.o


def main():
    arquivobf = open(INPUT_FILENAME, 'r')
    arquivojs = open(OUTPUT_FILENAME, 'w')

    initialize(arquivojs)

    for line in arquivobf:
        for c in line:
            text = convert_to_js(c)
            arquivojs.write(text)

    arquivobf.close()
    arquivojs.close()




def convert_to_js(char):
    text = ''

    if(char == '+'):
        text += 'fita[i]++\n'
    elif(char == "-"):
        text += 'fita[i]--\n'
    elif(char == ">"):
        text += 'i++\nif (isNaN(fita[i])) fita[i]=0\n'
    elif(char == "<"):
        text += 'i--\n'
    elif(char == '.'):
        text = 'window.alert(String.fromCharCode(fita[i]))\n'
    elif(char == ','):
        text = 'fita[i] = window.prompt().charCodeAt(0)\n'

    return text



def initialize(arquivojs):
    arquivojs.write("var fita = [0]\nvar i = 0\n\n")


main()
