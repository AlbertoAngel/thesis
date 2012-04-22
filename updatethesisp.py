lines = open("thesis.tex").read().split("\n")

for i in range(len(lines)):
    if "%\\documentclass[12pt,lot, lof, singlespace]{puthesis}" in lines[i]:
        lines[i] = "\\documentclass[12pt,lot, lof, singlespace]{puthesis}"
    elif "%\\newcommand{\\printmode}{}" in lines[i]:
        lines[i] = "\\newcommand{\\printmode}{}"   
    elif "\\documentclass[12pt,lot, lof]{puthesis}" in lines[i]:
        lines[i] = "%\\documentclass[12pt,lot, lof]{puthesis}"
    elif "\\newcommand{\\proquestmode}{}" in lines[i]:
        lines[i] = "%\\newcommand{\\proquestmode}{}"

open("thesisp.tex",'w').write("\n".join(lines))
