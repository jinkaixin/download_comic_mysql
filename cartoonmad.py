import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


#注：此文件用于提取动漫狂网站内漫画的真实下载地址，网站的网址为 https://www.cartoonmad.com/
def html_encoding():
    return 'big5'                                                #动漫狂网站的编码格式
                   

def get_image_url_prefixion(comic_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}
    html_return = requests.get(comic_url,headers=headers)
    html_return.encoding = 'big5'
    html = BeautifulSoup(html_return.text,'lxml')
    info_lists = html.find_all(name='fieldset')                    #分析网站发现，需要的信息全放在第二个fieldset的td标签中
    info_lists = info_lists[1].find_all(name='td')
    for num in range(len(info_lists)):
        try:
            part_url = info_lists[num].a.get('href')
        except AttributeError:                                     #不需要的td标签用except来排除
            continue
        else:
            break
    new_url = 'https://www.cartoonmad.com' + part_url
    html_return = requests.get(new_url,headers=headers)
    html_return.encoding = 'big5'
    html = BeautifulSoup(html_return.text,'lxml')
    info_lists = html.find_all(name='img')
    for num in range(len(info_lists)):
        try:
            part_url = info_lists[num].get('src')
            if not 'file=/' in part_url:
                continue
        except AttributeError:                                    
            continue
        else:
            break
    part_url = part_url.replace('amp;','')
    new_url = 'https://www.cartoonmad.com/comic/'+part_url
    opt = webdriver.ChromeOptions()
    opt.set_headless()
    driver = webdriver.Chrome(options=opt)
    driver.get(new_url)
    image_url_prefixion=driver.current_url
    driver.quit()
    image_url_prefixion = re.findall(r'(.+)/[0-9]+/[0-9]+.jpg',image_url_prefixion)[0]+'/'
    return image_url_prefixion
                   
def extract_comic_info(url_return):                                #确定动漫狂网站上该漫画一共更新了多少话，每话有多少页数，并将结果存入一个空字典中,其中使用了BeautifulSoup模块
    info_dict = {}
    choosed_comic_name = ''
    html = BeautifulSoup(url_return.text,'lxml')
    all_info_lists = html.find_all(name='fieldset')                    #分析网站发现，需要的信息全放在第二个fieldset的td标签中，且话的名称在a标签中，页数在font标签中
    info_lists = all_info_lists[1].find_all(name='td') 
    comic_name_info = all_info_lists[0].find_all(name='legend')
    choosed_comic_name = comic_name_info[0].string.strip()[:-2]                
    for num in range(len(info_lists)):
        try:
            chapter_info = info_lists[num].a.string
            pages = info_lists[num].font.string
        except AttributeError:                                     #不需要的td标签用except来排除
            continue
        else:
            pattern = re.compile(r'\d+')
            pages = pattern.findall(pages)[0]
            chapter_info = str(chapter_info)
            info_dict[chapter_info] = pages                        #将话名与相应页数存入字典   
    return info_dict,choosed_comic_name


def form_image_url(info_dict,folder_path,image_url_prefixion):                 #此函数返回的字典存入了每一话名称，每一张图片的页码及真实下载地址，其中值为一个字典，存放着每一张图片的页码及真实下载地址，即字典里套字典
    total_info_dict = {}
    for chapter_info,pages in info_dict.items():                         #构造下载链接
        pattern = re.compile(r'\d+')
        chapter = pattern.findall(chapter_info)[0]         #获取下载地址中的一串数字,等下构建图片的真实下载地址时要用到
        pages = int(pages)+1
        interim_info_dict = {}
        for page in range(1,pages):
            if page < 10:
                image_url = image_url_prefixion+chapter+'/00'+str(page)+'.jpg'
            elif page <100:
                image_url = image_url_prefixion+chapter+'/0'+str(page)+'.jpg'       
            else:
                image_url = image_url_prefixion+chapter+'/'+str(page)+'.jpg'       #确定真实下载地址
            interim_info_dict[page] = image_url
        total_info_dict[chapter_info] = interim_info_dict
    return total_info_dict
