from sys import argv, stdin

def extract_cites(text:str):
    extracted = []
    offset = 0
    while text != "" and not offset < 0:
        offset = text.find("\\cite{")
        print(offset)
        if (offset > 0):
            text = text[offset+6:]
            offset = text.find("}")
            current = text[:offset]
            text = text[offset+1:]
            extracted.append(current)
    extracted = ",".join(extracted).split(",")
    extracted = map(str.strip, extracted)
    extracted = list(set(extracted))
    
    extracted.sort()
    return ",".join(extracted)

if __name__ == '__main__':
    if len(argv) > 1:
        print(extract_cites(argv[1]))
    else:
        input = ""
        for line in stdin:
            input += line
        print(extract_cites(input))
            
