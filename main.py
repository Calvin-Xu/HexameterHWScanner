from cltk.prosody.latin.hexameter_scanner import HexameterScanner
from cltk.tokenize.line import LineTokenizer
from cltk.prosody.latin.scansion_formatter import ScansionFormatter
from cltk.prosody.latin.scansion_constants import ScansionConstants

constants = ScansionConstants(unstressed="˘",stressed= "-", optional_terminal_ending="X")
scanner = HexameterScanner(constants)
tokenizer = LineTokenizer('latin')
formatter = ScansionFormatter(constants)

def returnFeet(scansion, last=""):
    scansion = list(scansion)
    try:
        if len(scansion) == 0:
            return last
        if scansion[1] == "-":
            last += "S"
            next = scansion[2:len(scansion)+1]
            return returnFeet(next, last)
        elif scansion[1] == "˘":
            last += "D"
            next = scansion[3:len(scansion)+1]
            return returnFeet(next, last)
    except:
        return("ERROR")

with open("test.txt", "r") as f:
    text = tokenizer.tokenize(f.read())
    for line in text:
        result = scanner.scan(line)
        scansion = ''.join(str(e) for e in list(result.scansion.replace(" ", ""))[0:-5])
        feet = returnFeet(scansion) + "DS" if len(returnFeet(scansion)) == 4 else "ERROR"
        print(result.scansion + "    " + feet)
        print(result.original)
        print("\n")
