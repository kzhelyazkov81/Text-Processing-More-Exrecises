def html_format(content):
    for i in range(len(content)):
        if i == 0:
            print(f'<h1>\n{    content[0]}\n</h1>')
        elif i == 1:
            print(f'<article>\n{    content[1]}\n</article>')
        else:
            print(f'<div>\n{    content[i]}\n</div>')


content = []
while True:
    line = input()
    if line == 'end of comments':
        break
    content.append(line)
html_format(content)
