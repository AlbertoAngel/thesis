import sys
files = sys.argv[1:]

for afile in files:
    lines = open(afile).read().split("\n")
    startindices = []
    endindices = []
    for i in xrange(len(lines)):
        if "\\beq" in lines[i] or "\\begin{align}" in lines[i]:
            startindices.append(i)
        elif "\\eeq" in lines[i] or "\\end{align}" in lines[i] or "\\end{align*}" in lines[i]:
            endindices.append(i)

    for start,end in zip(startindices,endindices):
        if "\\label" not in " ".join(lines[start:end]):
            if "\\beq" in lines[start]:
                lines[start] = lines[start].replace("\\beq","\\beqnn")
                lines[end] = lines[end].replace("\\eeq","\\eeqnn")
            elif "\\begin{align}" in lines[start]:
                lines[start] = lines[start].replace("\\begin{align}","\\begin{align*}")
                lines[end] = lines[end].replace("\\end{align}","\\end{align*}")

    open(afile,'w').write("\n".join(lines))
