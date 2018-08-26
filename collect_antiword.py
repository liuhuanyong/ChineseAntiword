#!/usr/bin/env python3
# coding: utf-8
# File: spider.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-8-26


from urllib import request
from lxml import etree

def get_html(url):
    return request.urlopen(url).read().decode('GBK', 'ignore')

def main():
    f = open('antisem_fyc.txt', 'w+')
    links = ['http://fyc.5156edu.com/html2/%s.html'%i for i in range(1, 75)]
    for link in links:
        html = get_html(link)
        selector = etree.HTML(html)
        words = [i for i in selector.xpath('//td/a/text()')]
        links = ['http://fyc.5156edu.com' + i for i in selector.xpath('//td/a/@href')]
        print(len(words), len(links))
        word_dict = list(zip(words, links))
        for i in word_dict:
            wd = i[0]
            link = i[1]
            html = get_html(link)
            selector = etree.HTML(html)
            antis = [i.replace('(','') for i in selector.xpath('//tr[2]/td[2]/text()') if '(' in i and  '。' not in i and '，' not in i]
            print(wd, link, antis)
            f.write(wd + ':' + ';'.join(antis) + '\n')
    f.close()

def main2():
    f = open('antisem_kxue.txt', 'w+')
    links = ['http://fyc.kxue.com/list/index_%s.html'%i for i in range(1, 120)]
    for link in links:
        print(link)
        html = get_html(link)
        selector = etree.HTML(html)
        wds = [i for i in selector.xpath('//span[@class="hz"]/a/text()')]
        antis = [i for i in selector.xpath('//span[@class="hz"]/span[@class="js"]/text()')]
        print(len(wds))
        print(len(antis))
        for i in zip(wds, antis):
            f.write(i[0] + ':' + i[1] + '\n')
    f.close()

def merge():
    f = open('antisem_full.txt', 'w+')
    wd_dict = {}
    for line in open('antisem2.txt'):
        line = line.strip().split(':')
        if len(line) < 2:
            continue
        if not line:
            continue
        wd = line[0]
        antis = [i for i in line[1].split(';')]
        if wd not in wd_dict:
            wd_dict[wd] = antis
        else:
            wd_dict[wd] += antis

    for wd, anti in wd_dict.items():
        f.write(wd+':' + ';'.join(list(set(anti))) + '\n')
    f.close()

#
# if __name__=='__main__':
#     merge()