# import requests
# import re
# URL = 'https://en.wikipedia.org/wiki/Akbar'
# page = requests.get(URL)
# text=page.text
# with open("text.html",'w') as f:
#     f.write(text)

#header
    # pattern=r'<h\d>.*</h\d>'
    # header=re.findall(pattern,text)
    # with open("header.html",'w') as f:
    #     f.write("\n".join(header))
    #
    #
    # #paragraph
    # par_pattern=r'<p>.*</p>'
    # header=re.findall(par_pattern,text)
    # with open("par.html",'w') as f:
    #     f.write("\n".join(header))
