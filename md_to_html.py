import markdown


def convert(filename):
    with open(filename, 'r') as f:
        text = f.read()
        html = markdown.markdown(text)
    with open(filename[:-3] + ".html", 'w') as f:
        f.write(html)


if __name__ == '__main__':
    convert("Exemple1.md")