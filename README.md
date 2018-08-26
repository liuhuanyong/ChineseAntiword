# ChineseAntiword
ChineseAntiword,针对中文词语的反义词查询接口．在当前的中文信息处理当中，有大量的近义词词典，如同义词词林等，但少有反义词词典，反义词词典在构造对立语义上有很大用途，本项目目的是为提供这一接口


# 使用方式
    from ChineseAntiword import *
    antiwords = handler.get_antiword(word)


# 测试样例
    s = '自然语言处理是皇冠上的一颗明珠'
    handler = ChineseAntiword()
    word = '天才'
    antiwords:['庸才', '庸人', '蠢材']
    word = '快乐'
    antiwords:['悲伤', '伤心', '难过', '痛苦', '烦恼', '苦恼']
    word = '和蔼'
    antiwords:['凶狠', '凶残', '粗暴', '凶横', '凶恶', '严厉', '蛮横']
    word = '批判'
    antiwords:['表扬', '表彰', '赞颂']


# 问题
1) 基于词典的反义词查询，不可取，取无法穷举
2) 要是能够找到像word2vec这样的技术大规模地挖掘反义词，该有多好．



