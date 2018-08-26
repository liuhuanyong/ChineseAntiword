#!/usr/bin/env python3
# coding: utf-8
# File: ChineseAntiWord.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-8-26

import os
class ChineseAntiword:
    def __init__(self):
        cur_dir = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        antifile = os.path.join(cur_dir, 'antisem.txt')
        self.antidict, self.simdict = self.build_antidict(antifile)

    '''构造反义词词典'''
    def build_antidict(self, file):
        antidict = {}
        simdict = {}
        for line in open(file):
            line = line.strip().split(':')
            wd = line[0]
            antis = line[1].strip().split(';')
            if wd not in antidict:
                antidict[wd] = antis
            else:
                antidict[wd] += antis

            for anti in antis:
                if anti not in simdict:
                    simdict[anti] = [i for i in antis if i != anti]
                else:
                    simdict[anti] += [i for i in antis if i != anti]

        return antidict, simdict

    '''根据目标词获取反义词'''
    def get_antiword(self, word):
        return self.antidict.get(word, 'None')

    '''根据目标词获取近义词'''
    def get_simword(self, word):
        return self.simdict.get(word, 'no')


def demo():
    handler = ChineseAntiword()
    word = '批判'
    antiwords = handler.get_antiword(word)
    print(antiwords)

if __name__=="__main__":
    demo()