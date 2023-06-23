# from bs4 import BeautifulSoup
# import urllib.request
# from urllib import request
# from urllib.request import Request, urlopen

# import pandas as pd
# import os

# url = "https://www.acmicpc.net/step"
# request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
# html = urlopen(request_site).read()
# df = pd.read_html(html, encoding='utf-8')
# current_path = os.getcwd()

# for i in range(9, len(df[0])):
#     step = str(df[0]["단계"][i])
#     title = str(df[0]["제목"][i])
#     if ":" in title:
#         title = title.replace(":", "_")
#     os.makedirs(step + '. ' + title)

# for folIdx in range(1, len(df[0])):
#     question = int(df[0]["총 문제"][folIdx])
#     step = str(df[0]["단계"][folIdx])
#     title = str(df[0]["제목"][folIdx])
#     if ":" in title:
#         title = title.replace(":", "_")
#         title = title.replace(" ", "")

#     for num in range(question):
#         folder = step + '. ' + title
        
#         filename = f"{folder}/step{num+1}.py"
#         deleteFileName = f"{folder}/step{0}.py"
#         if os.path.exists(deleteFileName):
#             os.remove(deleteFileName)
#         with open(filename, 'w') as file:
#             # You can optionally write content to the file here
#             pass