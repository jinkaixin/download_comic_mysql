import requests
import re
import os
from bs4 import BeautifulSoup


def get_html_resource(url,headers):
    return requests.get(url,headers=headers,timeout=10)

def save_image(image_path,image):
    with open(image_path,'wb') as f:
        f.write(image.content)                                  #将二进制数据写入文件



                    

