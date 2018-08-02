# #encoding:utf-8
# import re
# import requests
# from lxml import html
# url='https://movie.douban.com/' #需要爬数据的网址
# page=requests.Session().get(url)
# tree=html.fromstring(page.text)
# result=tree.xpath('//td[@class="title"]//a/text()') #获取需要的数据
#
# # result=tree.xpath('//li[@class="title"]//a/text()')
#
# file_name = open('pachong.txt', "wb")
#
# for i in range(len(result)):
#     print(result[i])
#
#     # 将代码写入文件
#     data=(result[i])
#     data=data.encode('utf-8')
#     # print(type(data))
#     file_name.write(data)
#     file_name.write('\n')
#
# # 关闭文件
# file_name.close()
#

#encoding:utf-8
import urllib2
import requests
from lxml import html
import csv
import pandas as pd
import codecs

url='https://home.meishichina.com/recipe-menu.html#hmsr=www&hmpl=index&hmcu=magicside&hmkw=D4&hmci=D4_menu' #需要爬数据的网址
response = urllib2.urlopen(url)
# print response.read()
data=response.read()
# print(type(response.read()))

file_name = open('pachong.txt', "wb")

file_name.write(data)

# 关闭文件
file_name.close()

file_name = open('pachong.txt', 'r')

# for i in range(len(file_name.readlines())):
#     line = file_name.readlines[i]

count = 0
jisuan = -4
count1 = 0
count2 = 0
flag = True
i = 0
list0 = []
a = 'a'
b = 'b'
c = 'c'

def hanshu(f):
    with open(f,'r+') as f:
        content = f.read()
        f.seek(0,0)
        f.truncate()
        f.write(content.decode('utf8').encode('utf-8-sig'))


for line in file_name.readlines()[486:516]:

    lines = line.strip()
    # print (lines)
    # if lines.find('category_box'):
    if 'href' and 'li' in lines:
        temp = line.find('href')
        temp2 = line.find('"',temp)
        temp2 += 1
        temp2 = line.find('"',temp2)

        url2 = line[temp+6:temp2-1]
        # print url2
        response = urllib2.urlopen(url2)

        data = response.read()
        file_name2 = open('pachong.txt', "wb")
        file_name2.write(data)
        file_name2 = open('pachong.txt', 'r')
        for line2 in file_name2.readlines()[69:300]:
            lines2 = line2.strip()
            if 'href' and 'recipe-' in lines2:
                temp3 = line2.find('href')
                temp4 = line2.find('"', temp3)
                temp4 += 1
                temp4 = line2.find('"', temp4)
                url3 = line2[temp3 + 6:temp4]
                # 关闭文件
                try:
                    response = urllib2.urlopen(url3)

                    data = response.read()
                    file_name3 = open('pachong.txt', "wb")
                    file_name3.write(data)
                    file_name3 = open('pachong.txt', 'r')

                    count1 = 0
                    count2 = 0
                    c1 = 0
                    c2 = 0
                    count3 = 0
                    count4 = 0
                    c3 = 0
                    c4 = 0
                    liebiao1 = []
                    liebiao2 = []
                    liebiao3 = []
                    liebiao4 = []
                    liebiao5 = []
                    liebiao6 = []
                    liebiao9 = []

                    for line3 in file_name3.readlines():
                        lines3 = line3.strip()
                        count1 +=1
                        count2 +=1
                        if '主料' in lines3:
                            c1 = count1
                            count1 = 0
                        if '辅料' in lines3:
                            c2 = count2
                            count2 = 0
                    file_name4 = open('pachong.txt', 'r')
                    file_name5 = open('pachong.txt', 'r')

                    shiwuming=(file_name5.readlines()[4])
                    aaah = shiwuming.find('的做法')
                    shiwuming = shiwuming[7:aaah]
                    liebiao1.append(shiwuming)
                    liebiao4 = str(liebiao1).decode('string_escape')

                    a = (",".join(liebiao1))

                    for line4 in file_name4.readlines()[c1:c2]:
                        lines4 = line4.strip()
                        if '</b>' and '<b>' in lines4:
                            temp5 = line4.find('<b>')
                            temp6 = line4.find('</b>', temp5)
                            url4 = line4[temp5 + 3:temp6]
                            liebiao2.append(url4)
                            # liebiao5 = str(liebiao2).decode('string_escape')

                    b = (",".join(liebiao2))

                    file_name9 = open('pachong.txt','r')

                    for line9 in file_name9.readlines()[c1:c2]:
                        lines9 = line9.strip()
                        if 'category_s2' in lines9:
                            temp9 = line9.find('category_s2')
                            temp10 = line9.find('</span>',temp9)
                            url9 = line9[temp9 + 13:temp10]
                            liebiao9.append(url9)
                    x = (",".join(liebiao9))

                    file_name6 = open('pachong.txt','r')
                    for line5 in file_name6.readlines():
                        lines5 = line5.strip()
                        count3 += 1
                        count4 += 1
                        if '辅料' in lines5:
                            c3 = count3
                            count3 = 0
                        if '工艺' in lines5:
                            c4 = count4
                            count4 = 0

                    file_name7 = open('pachong.txt','r')

                    for line6 in file_name7.readlines()[c3:c4]:
                        lines6 = line6.strip()
                        if '</b>' and '<b>' in lines6:
                            list1 = []
                            temp7 = line6.find('<b>')
                            temp8 = line6.find('</b>', temp7)
                            url5 = line6[temp7 + 3:temp8]

                            liebiao3.append(url5)
                            liebiao6 = str(liebiao3).decode('string_escape')

                    c = (",".join(liebiao3))

                    list1.append(a)
                    list1.append(b)
                    list1.append(x)
                    list1.append(c)
                    print list1
                    list0.append(list1)

                    csvFile = codecs.open("jialiang5.csv", "w+")
                    # csvFile= codecs.open("diyigao.csv", "w+", 'gbk')
            #         writer = csv.writer(csvFile, dialect='excel')
            #         writer.writerow(list0)
            #         csvFile.close()
            #         break
            # break
                    try:
                        writer = csv.writer(csvFile, dialect='excel')
                        writer.writerow(["name", "zhuliao", "amount" "fuliao"])
                        writer.writerows(list0)
                        # writer.writerow((liebiao4, liebiao5, liebiao6))

                    finally:
                        csvFile.close()


                    #
                    # hanshu('diyigao.csv')
                    #
                    # list = [shiwuming,url4,url5]
                    # test = pd.DataFrame(columns=name, data=list)
                    # test.to_csv('diyigao.csv')

                except:
                    pass


# file_name2.close()
