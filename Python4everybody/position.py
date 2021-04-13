str = "X-DSPAM-Confidence: 0.8475"

ipos = str.find(':')
print(f"Position is {ipos+2}")
piece = str[ipos+2:]
fvalue = float(piece)
print(fvalue)