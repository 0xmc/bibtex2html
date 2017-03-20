import re

with open('publications.bib') as f:
    bib = f.readlines()

output = ""
for line in bib:
    if re.match('^\@', line):
        line = "<pre>\n" + line
    if re.match('^\}$', line):
        line = line + "</pre>\n"
    m = re.search('\{http[a-zA-Z0-9\:\/\-\.]+\}', line)
    if m:
        line = (line[:m.start()] +
                "{<a href=\"" +
                m.group(m.pos)[1:-1] +
                "\">" +
                m.group(m.pos)[1:-1] +
                "</a>}" +
                line[m.end():])
    output += line

with open('publications.bib.html', 'w') as f:
    f.write(output)
