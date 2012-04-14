import sys
files = sys.argv[1:]
matrixtrigger = "mymtx"
endtrigger = "l}"

for afile in files:
    origcontents = open(afile).read()
    startindex = 0
    while(True):
        try:
            startindex = origcontents.index(matrixtrigger, startindex) + len(matrixtrigger) + 1
            endindex = origcontents.index(endtrigger,startindex)
            lines = [i.strip().replace(","," ").replace("  "," ") for i in origcontents[startindex:endindex].split(";")]
            lines = [i.replace(" "," & ") for i in lines]
            rowcount = len(lines)
            columncount = lines[0].count("&") + 1
            origcontents = origcontents[:startindex - len(matrixtrigger) - 2] + "\\left[\\begin{array}{" + "c"*columncount + "}" + "\\\\\n".join(lines) + "\end{array}\\right]" + origcontents[endindex+len(endtrigger):]
        except:
            break
    newfile = afile.replace("orig","")
    open(newfile,'w').write(origcontents)
