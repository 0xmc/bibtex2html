import argparse
import re


def bib2html(filename):
    """
    Writes output .html file from input .bib filename.

    Args:
        filename (str): .bib file
    """
    try:
        with open(filename) as f:
            bib = f.readlines()
    except IOError:
        print("Cannot open file")
        return

    output = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
<title>bibtex</title>
</head>
<body>
"""

    for line in bib:
        if re.match("^\@", line):
            line = "<pre>\n" + line
        if re.match("^\}$", line):
            line = line + "</pre>\n"
        m = re.search("\{http[a-zA-Z0-9\:\/\-\.]+\}", line)
        if m:
            line = (line[:m.start()] +
                    "{<a href=\"" +
                    m.group(m.pos)[1:-1] +
                    "\">" +
                    m.group(m.pos)[1:-1] +
                    "</a>}" +
                    line[m.end():])
        output += line

    output += "</body>\n</html>"

    try:
        with open(filename + ".html", "w") as f:
            f.write(output)
    except IOError:
        print("Cannot write file")


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description="Turn .bib into .html")
    argparser.add_argument("filename", help=".bib file to html-ify")
    args = argparser.parse_args()

    bib2html(args.filename)
