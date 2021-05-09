import base64
import os


def split(word):
    return [char for char in word]

def gen_str(instr):
    while True:
        if len(instr) == 10000:
            break
        else:
            instr += b"#"

    return(instr)


def placeholder():
    out = ""
    while True:
        out += "#"
        if len(out) == 10000:
            break
        else:
            pass
    return(out.encode())


def main():

    base = open("base.dll",'rb').read()
    infile = base64.b64encode(open(input("infile: "),'rb').read())
    dat = gen_str(infile)
    sect1 = base.split(placeholder())[0]
    sect2 = base.split(placeholder())[1]
    out = sect1 + dat + sect2
    outfile = input("outfile: ")
    open(outfile,'wb').write(out)

main()
