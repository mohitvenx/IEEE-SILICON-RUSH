import pandas as pd
a = pd.read_csv("./test_10.docx")
a.to_html("./table10.html")
html_file = a.to_html()