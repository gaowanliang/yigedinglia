from pypinyin import lazy_pinyin, pinyin
import json


# print(pinyin("一个顶俩"))
f = open("idioms.txt", 'r', encoding='UTF-8')
f1 = open("7.txt", 'r', encoding='UTF-8')
f2 = open("8.txt", 'r', encoding='UTF-8')
f3 = open("fudu.txt", 'r', encoding='UTF-8')
f4 = open("fudu1.txt", 'r', encoding='UTF-8')
i1 = eval(f1.read())
i2 = eval(f2.read())
fudu = eval(f3.read())
fudu1 = eval(f4.read())
iss = f.readlines()
i3 = ['cou 凑手不及', 'beng 绷巴吊拷', 'shuan 闩门闭户', 'beng 绷爬吊拷',
      'beng 蹦蹦跳跳', 'beng 绷扒吊拷', 'ken 肯堂肯构', 'ken 肯构肯堂', 'seng 僧多粥少', 'nen 嫩妇女子', "nou 耨盌温敦"]
p1 = ['ji', 'rui', 'ri', 'zhuan', 'han', 'xiu', 'ma', 'she', 'zhong', 'guang', 'yun', 'jue', 'cen', 'qing', 'ming', 'zhen', 'shen', 'wen', 'shuo', 'cha', 'hua', 'ku', 'qie', 'fei', 'tie', 'dan', 'shang', 'zan', 'dong', 'ge', 'mao', 'xia', 'ni', 'long', 'tai', 'xu', 'jiu', 'ju', 'biao', 'di', 'lang', 'guan', 'yan', 'chou', 'ren', 'que', 'song', 'cun', 'qun', 'kuai', 'qi', 'sha', 'shuai', 'nan', 'dao', 'shan', 'yu', 'fu', 'ting', 'zhang', 'kuang', 'su', 'fang', 'bo', 'kong', 'die', 'hui', 'zhu', 'bu', 'ci', 'ke', 'mo', 'gu', 'wei', 'cu', 'sheng', 'xuan', 'zao', 'nei', 'chui', 'tian', 'zhi', 'si', 'tui', 'meng', 'hao', 'ze', 'sao', 'yue', 'cang', 'ban', 'diao', 'bi', 'shuang', 'nang', 'zhui', 'sang', 'jiang', 'cao', 'tou', 'zi', 'bei', 'tong', 'you', 'shou', 'kang', 'ou', 'liang', 'chu', 'le', 'diu', 'shu', 'cai', 'xiao', 'bie',
      'zhuang', 'hai', 'dou', 'ding', 'rong', 'zha', 'juan', 'ti', 'heng', 'mai', 'geng', 'neng', 'er', 'lai', 'qiong', 'cheng', 'chun', 'lv', 'shi', 'qian', 'quan', 'jing', 'jun', 'na', 'ba', 'li', 'jie', 'luo', 'ling', 'pao', 'bing', 'lu', 'jian', 'bao', 'chen', 'wai', 'gui', 'ruo', 'sui', 'duo', 'po', 'mi', 'dang', 'lian', 'qiang', 'zu', 'bai', 'fen', 'ping', 'jin', 'mu', 'jiao', 'qiu', 'feng', 'gan', 'wang', 'chong', 'san', 'yuan', 'cong', 'zheng', 'xi', 'gao', 'an', 'yang', 'yin', 'xue', 'miao', 'dai', 'xing', 'chao', 'pin', 'qiao', 'xiang', 'lin', 'ru', 'pan', 'xian', 'shun', 'hong', 'mei', 're', 'fan', 'gua', 'tu', 'dian', 'wan', 'zuo', 'jia', 'huo', 'pang', 'gai', 'xiong', 'rou', 'zun', 'yi', 'xin', 'wu', 'zhan', 'cuo', 'he', 'men', 'shui', 'tan', 'yong', 'min', 'da', 'gong', 'man', 'kai', 'ben', 'kou', 'duan', 'mian']
p2 = ['ding', 'bi', 'dun', 'ku', 'pan', 'lu', 'nao', 'kun', 'za', 'hua', 'zao', 'bin', 'chen', 'duo', 'qiang', 'lian', 'ran', 'liang', 'xiu', 'weng', 'la', 'chou', 'gu', 'cang', 'ren', 'chang', 'gua', 'ce', 'ke', 'zi', 'mang', 'ming', 'zhua', 'nu', 'nie', 'zhu', 'yong', 'pao', 'di', 'yue', 'sen', 'huan', 'you', 'kuai', 'gou', 'shou', 'zuo', 'hui', 'tang', 'pen', 'qian', 'cha', 'xiang', 'dai', 'kuan', 'suo', 'tan', 'jian', 'xian', 'ceng', 'sang', 'xun', 'hun', 'pei', 'tiao', 'qia', 'quan', 'bo', 'pian', 'san', 'qiao', 'ya', 'juan', 'gai', 'tun', 'chai', 'rang', 'ge', 'tuan', 'bao', 'sui', 'mai', 'gun', 'xuan', 'biao', 'shan', 'cen', 'an', 'guang', 'nai', 'ben', 'a', 'chuan', 'zuan', 'ji', 'wen', 'ga', 'ou', 'xue', 'nan', 'ma', 'jun', 'ban', 'yao', 'ning', 'shao', 'mao', 'mie', 'kou', 'chan', 'zeng', 'pang', 'kan', 'qiu', 'zheng', 'shuo', 'fo', 'huo', 'zun', 'tou', 'bian', 'wei', 'huai', 'bing', 'lv', 'fan', 'sha', 'zhou', 'huang', 'mian', 'guo', 'ruo', 'du', 'jue', 'shuang', 'ha', 'chuo', 'se', 'luan', 'men', 'kuang', 'zhun', 'ci', 'xing', 'lin', 'li', 'dao', 'geng', 'lve', 'song', 'ni', 'cuo', 'guai', 'xia', 'qin', 'te', 'nuo', 'nong', 'long', 'xi', 'yu', 'nv', 'lei', 'gang', 'yin', 'zei', 'tian', 'diao', 'fei', 'nuan', 'cu', 'miu', 'zan', 'teng', 'nei', 'jiong', 'sai', 'zen', 'gui', 'qie', 'hang', 'niu', 'shuai', 'nang', 'ye', 'sun', 'ai', 'zhen', 'pin', 'ze', 'duan', 'jiao',
      'diu', 'pu', 'zui', 'zha', 'cheng', 'liao', 'shu', 'wa', 'hou', 'mei', 'er', 'che', 'ping', 'ruan', 'keng', 'lang', 'she', 'piao', 'cong', 'zhan', 'ri', 'shun', 'sao', 'kai', 'su', 'hai', 'shi', 'dou', 'fang', 'jiang', 'luo', 'sheng', 'tao', 'yun', 'fen', 'zhi', 'ling', 'jin', 'niao', 'na', 'qu', 'ne', 'o', 'cui', 'lai', 'pie', 'chao', 'ti', 'shui', 'tuo', 'shua', 'peng', 'can', 'rou', 'zhong', 'yuan', 'ao', 'sa', 'xin', 'chu', 'bang', 'zang', 'run', 'chong', 'qi', 'zhang', 'fou', 'suan', 'ba', 'pa', 'kuo', 'tie', 'dian', 'shai', 'zhuang', 'fu', 'leng', 'chuang', 'zhuo', 'die', 'le', 'ju', 'han', 'wo', 're', 'ying', 'cao', 'feng', 'dong', 'gan', 'fa', 'kong', 'gong', 'kua', 'chuai', 'pi', 'wai', 'guan', 'ta', 'si', 'ca', 'heng', 'da', 'chi', 'qun', 'zhe', 'zong', 'hei', 'mo', 'cun', 'yi', 'nve', 'dang', 'cuan', 'qiong', 'lou', 'lao', 'yan', 'zhui', 'en', 'xiao', 'liu', 'zhuan', 'hao', 'zu', 'de', 'miao', 'tui', 'yang', 'he', 'tu', 'chun', 'ting', 'hong', 'ru', 'zhai', 'tong', 'hen', 'mu', 'zhao', 'pou', 'lie', 'mi', 'wu', 'meng', 'ang', 'jing', 'reng', 'cai', 'pai', 'wang', 'lan', 'chui', 'jia', 'zhuai', 'zou', 'bu', 'xie', 'man', 'dui', 'sou', 'gen', 'jie', 'qing', 'lun', 'zai', 'kang', 'gao', 'min', 'deng', 'e', 'bai', 'tai', 'que', 'shei', 'nian', 'hu', 'bie', 'bei', 'shang', 'dan', 'kui', 'rao', 'rui', 'xu', 'kao', 'po', 'jiu', 'xiong', 'rong', 'wan', 'shen', 'neng', 'mou']
pinyinList = ['a', 'o', 'e', 'ai', 'ao', 'an', 'ang', 'ou', 'ei', 'er', 'en', 'eng', 'ba', 'bo', 'bi', 'bu', 'bai', 'bao', 'ban', 'bang', 'bei', 'ben', 'beng', 'biao', 'bian', 'bie', 'bin', 'bing', 'pa', 'po', 'pi', 'pu', 'pai', 'pao', 'pan', 'pang', 'pou', 'pei', 'pen', 'peng', 'piao', 'pian', 'pie', 'pin', 'ping', 'ma', 'mo', 'me', 'mi', 'mu', 'mai', 'mao', 'man', 'mang', 'mou', 'mei', 'men', 'meng', 'miao', 'mian', 'mie', 'miu', 'min', 'ming', 'fa', 'fo', 'fu', 'fan', 'fang', 'fou', 'fei', 'fen', 'feng', 'da', 'de', 'di', 'du', 'dai', 'dao', 'dan', 'dang', 'dou', 'dong', 'dei', 'den', 'deng', 'dia', 'diao', 'dian', 'die', 'diu', 'ding', 'duan', 'dui', 'dun', 'duo', 'ta', 'te', 'ti', 'tu', 'tai', 'tao', 'tan', 'tang', 'tou', 'tong', 'teng', 'tiao', 'tian', 'tie', 'ting', 'tuan', 'tui', 'tun', 'tuo', 'na', 'ne', 'ni', 'nu', 'nv', 'nai', 'nao', 'nan', 'nang', 'nou', 'nong', 'nei', 'nen', 'neng', 'niao', 'nian', 'nie', 'niu', 'nin', 'ning', 'niang', 'nuan', 'nve', 'nun', 'nuo', 'la', 'lo', 'le', 'li', 'lu', 'lv', 'lai', 'lao', 'lan', 'lang', 'lou', 'long', 'lei', 'leng', 'lia', 'liao', 'lian', 'lie', 'liu', 'lin', 'ling', 'liang', 'luan', 'lve', 'lun', 'luo', 'ga', 'ge', 'gu', 'gai', 'gao', 'gan', 'gang', 'gou', 'gong', 'gei', 'gen', 'geng', 'gua', 'guai', 'guan', 'guang', 'gui', 'gun', 'guo', 'ka', 'ke', 'ku', 'kai', 'kao', 'kan', 'kang', 'kou', 'kong', 'kei', 'ken', 'keng', 'kua', 'kuai', 'kuan', 'kuang', 'kui', 'kun', 'kuo', 'ha', 'he', 'hu', 'hai', 'hao', 'han',
              'hang', 'hou', 'hong', 'hei', 'hen', 'heng', 'hua', 'huai', 'huan', 'huang', 'hui', 'hun', 'huo', 'ji', 'ju', 'jia', 'jiao', 'jian', 'jie', 'jiu', 'jin', 'jing', 'jiang', 'jiong', 'juan', 'jue', 'jun', 'qi', 'qu', 'qia', 'qiao', 'qian', 'qie', 'qiu', 'qin', 'qing', 'qiang', 'qiong', 'quan', 'que', 'qun', 'xi', 'xu', 'xia', 'xiao', 'xian', 'xie', 'xiu', 'xin', 'xing', 'xiang', 'xiong', 'xuan', 'xue', 'xun', 'zha', 'zhe', 'zhi', 'zhu', 'zhai', 'zhao', 'zhan', 'zhang', 'zhou', 'zhong', 'zhei', 'zhen', 'zheng', 'zhua', 'zhuai', 'zhuan', 'zhuang', 'zhui', 'zhun', 'zhuo', 'cha', 'che', 'chi', 'chu', 'chai', 'chao', 'chan', 'chang', 'chou', 'chong', 'chen', 'cheng', 'chuai', 'chuan', 'chuang', 'chui', 'chun', 'chuo', 'sha', 'she', 'shi', 'shu', 'shai', 'shao', 'shan', 'shang', 'shou', 'shei', 'shen', 'sheng', 'shua', 'shuai', 'shuan', 'shuang', 'shui', 'shun', 'shuo', 're', 'ri', 'ru', 'rao', 'ran', 'rang', 'rou', 'rong', 'ren', 'reng', 'ruan', 'rui', 'ru', 'ruo', 'za', 'ze', 'zi', 'zu', 'zai', 'zao', 'zan', 'zang', 'zou', 'zong', 'zei', 'zen', 'zeng', 'zuan', 'zui', 'zun', 'zuo', 'ca', 'ce', 'ci', 'cu', 'cai', 'cao', 'can', 'cang', 'cou', 'cong', 'cen', 'ceng', 'cuan', 'cui', 'cun', 'cuo', 'sa', 'se', 'si', 'su', 'sai', 'sao', 'san', 'sang', 'sou', 'song', 'sen', 'seng', 'suan', 'sui', 'sun', 'suo', 'ya', 'yo', 'yi', 'yu', 'yao', 'yan', 'yang', 'you', 'yong', 'ye', 'yin', 'ying', 'yuan', 'yue', 'yun', 'wa', 'wo', 'wu', 'wai', 'wan', 'wang', 'wei', 'wen', 'weng']
p3 = ['cou', 'beng', 'shuan', 'ken', 'seng', 'nen', 'nou']
p5 = ['jing', 'fang', 'zhao', 'li', 'bai', 'jiu', 'ji', 'yi', 'feng', 'ren', 'qian', 'meng', 'ri', 'nan', 'mei', 'dao', 'lun', 'tian', 'ju', 'yu', 'ying', 'xin', 'gong', 'mang', 'mu', 'dou', 'zhi', 'jiao', 'xing', 'xuan', 'shu', 'jin', 'xiang', 'jiang', 'qi', 'da',
      'jian', 'nian', 'zui', 'yan', 'hua', 'fu', 'sheng', 'shen', 'duan', 'gu', 'chuang', 'wen', 'wei', 'e', 'zhong', 'jie', 'tou', 'qiao', 'wu', 'bu', 'shi', 'yuan', 'zao', 'sun', 'shan', 'zei', 'guan', 'fan', 'gan', 'cuo', 'guo', 'tong', 'xian', 'di', 'qin', 'kui']
q1 = ['sao', 'fei', 'lan', 'kao', 'geng', 'cou', 'chui', 'niu', 'niao', 're', 'zhen', 'hong', 'nai', 'sha', 'na', 'tu', 'jia', 'yao', 'chan', 'dun', 'gao', 'zheng', 'zun', 'tai', 'an', 'zai', 'shou', 'weng', 'mo', 'bie', 'hu', 'rong', 'chao', 'ben', 'hang', 'zha', 'cha', 'za', 'rou', 'en', 'tui', 'mao', 'ming', 'chou', 'pin', 'zuan', 'chen', 'nu', 'shei', 'xun', 'han', 'dian', 'zang', 'pu', 'hun', 'kua', 'fou', 'cang', 'tun', 'ta', 'song', 'ning', 'lang', 'bin', 'leng', 'die', 'ting', 'pian', 'she', 'yue', 'gen', 'ke', 'ou', 'pai', 'yin', 'ge', 'ku', 'fo', 'ai', 'xu', 'hen', 'bi', 'chai', 'tuo', 'long', 'lei', 'rui', 'sang', 'shuang', 'le', 'bian', 'gou', 'zhui', 'ran', 'chong', 'tie', 'juan', 'ban', 'shun', 'si', 'ceng', 'he', 'ze', 'ang', 'te', 'ao', 'guang', 'lve', 'qia', 'gun', 'qie', 'nao', 'ma', 'zeng', 'ba', 'zhou', 'er', 'run', 'teng', 'cong', 'qiang', 'ye', 'gai', 'kan', 'kuang', 'lai', 'po', 'ru', 'shang', 'heng', 'zong', 'ni', 'sou', 'kang', 'cun', 'chuan', 'jiong', 'ruan', 'cuan', 'xie', 'diu', 'sui', 'sai', 'nuan', 'lu', 'luo', 'cheng', 'lou', 'kun', 'cui', 'pao', 'nve', 'pi', 'bang', 'a', 'xiong', 'kai', 'shuai', 'lao', 'wa', 'tao', 'hei', 'wo', 'chang', 'yun', 'se', 'men', 'ya', 'miu', 'zhun', 'min', 'qun', 'nie', 'liu', 'fa', 'dui', 'lie', 'gui', 'biao', 'xue', 'zhan', 'xi', 'ca', 'kuai', 'lv', 'you', 'kou', 'ne', 'zhu', 'bing', 'hou', 'xia', 'qing', 'cao', 'can', 'dai', 'zi', 'zhuo', 'kong', 'huai', 'nei', 'chuai', 'zuo', 'jun', 'dong', 'su', 'hao', 'liao', 'zhuai', 'pou', 'deng', 'peng', 'ci', 'man', 'bei', 'luan', 'nong', 'mi', 'hui', 'huan', 'cai', 'mian', 'nuo', 'zhua', 'duo', 'pei', 'zhai', 'neng', 'ce', 'cu', 'mou', 'zou', 'tiao', 'pa', 'mai', 'liang', 'qu', 'tuan', 'bao', 'dan', 'guai', 'zan', 'suo', 'wai', 'quan', 'ti',
      'ling', 'chun', 'shai', 'diao', 'bo', 'chu', 'qiong', 'rao', 'zu', 'kuo', 'qiu', 'lian', 'zhuan', 'nv', 'miao', 'fen', 'chi', 'ding', 'shuo', 'jue', 'zhuang', 'tan', 'tang', 'hai', 'sen', 'shao', 'que', 'ping', 'san', 'gang', 'keng', 'cen', 'pan', 'wang', 'shui', 'mie', 'zhe', 'sa', 'xiao', 'chuo', 'kuan', 'yong', 'suan', 'piao', 'xiu', 'de', 'zhang',
      'lin', 'dang', 'nang', 'huang', 'wan', 'pen', 'huo', 'rang', 'che', 'reng', 'gua', 'du', 'pang', 'yang', 'ruo']
# print(list(set(pinyinList).difference(set(p5+q1))))


def jw(lis):
    return eval('['+str(lis).replace(' ', '').replace('[', '').replace(']', '')+']')


def cyfd(text):
    if text+"\n" in iss or text in pinyinList:
        if text in pinyinList:
            zy = text
            uu = []
        else:
            zy = lazy_pinyin(text)[3]
            uu = jw(pinyin(text))
        if zy in p5:
            ts = []
            py = []
            for i in fudu:
                if i.split(" ")[0] == zy:
                    if i.split(" ")[1] == text:
                        return {'title': "这个已经是复读成语了", "step": 0}
                    ts.append([text, i.split(" ")[1]])
                    py.append([uu,
                               jw(pinyin(i.split(" ")[1]))])
                if len(ts) >= 6:
                    break
            res = {
                'title': "已为你显示相关的 "+str(len(ts))+" 条结果",
                "step": 2,
                "num": len(ts),
                'ls': ts,
                'tk': py
            }
            return res
        elif zy in q1:
            ts = []
            py = []
            for i in fudu1:
                if i.split(" ")[0] == zy:
                    ky = lazy_pinyin(i.split(" ")[1])[3]
                    for j in fudu:
                        if j.split(" ")[0] == ky and len(ts) < 6:
                            ts.append([text, i.split(" ")[1], j.split(" ")[1]])
                            py.append([uu, jw(
                                pinyin(i.split(" ")[1])), jw(pinyin(j.split(" ")[1]))])

                if len(ts) >= 6:
                    break
            res = {
                'title': "已为你显示相关的 "+str(len(ts))+" 条结果",
                "step": 3,
                "num": len(ts),
                'ls': ts,
                'tk': py
            }
            return res
        else:
            return {'title': "很遗憾，没找到", "step": 0}
    else:
        return {'title': "这个不是成语/拼音", "step": 0}


def yigedinglia(text):

    if (text+"\n" not in iss) and (text not in pinyinList):
        print(text)
        return {'title': "这个不是成语/拼音", "step": 0}
    else:

        if text == "志在必得":
            text = "志在必的"
        if text == "一个顶俩":
            res = {'title': "你在逗我？", "step": 0}
            return res
        if text in pinyinList:
            rt = text
            uu = ['']
        else:
            rt = lazy_pinyin(text)[3]
            uu = jw(pinyin(text))
        if rt == "yi":
            res = {
                'title': "一步直达",
                "step": 2,
                "num": 1,
                'ls': [[text, '一个顶俩']],
                'tk': [[uu, ['yí', 'gè', 'dǐng', 'liǎ']]]
            }
            return res
        elif rt in p1:
            ts = []
            py = []
            for i in i1:
                if i.split(" ")[0] == rt:
                    ts.append([text, i.split(" ")[1], "一个顶俩"])
                    py.append([uu, jw(pinyin(
                        i.split(" ")[1])), ['yí', 'gè', 'dǐng', 'liǎ']])
                if len(ts) >= 6:
                    break
            res = {
                'title': "已为你显示相关的 "+str(len(ts))+" 条结果",
                "step": 3,
                "num": len(ts),
                'ls': ts,
                'tk': py
            }
            return res
        elif rt in p2:
            ts = []
            py = []
            for i in i2:
                if i.split(" ")[0] == rt:
                    ky = lazy_pinyin(i.split(" ")[1])[3]
                    for j in i1:
                        if j.split(" ")[0] == ky:
                            if text == "志在必的":
                                text = "志在必得"
                            ts.append([text, i.split(" ")[1],
                                       j.split(" ")[1], "一个顶俩"])
                            py.append([uu, jw(pinyin(
                                i.split(" ")[1])), jw(pinyin(
                                    j.split(" ")[1])), ['yí', 'gè', 'dǐng', 'liǎ']])
                            break
                if len(ts) >= 6:
                    break
            res = {
                'title': "已为你显示相关的 "+str(len(ts))+" 条结果",
                "step": 4,
                "num": len(ts),
                'ls': ts,
                'tk': py
            }

            return res
        elif rt in p3:
            ts = []
            py = []
            for q in i3:
                if q.split(" ")[0] == rt:
                    qq = lazy_pinyin(q.split(" ")[1])[3]
                    for i in i2:
                        if i.split(" ")[0] == qq:
                            ky = lazy_pinyin(i.split(" ")[1])[3]
                            for j in i1:
                                if j.split(" ")[0] == ky:
                                    ts.append([text, q.split(" ")[1],
                                               i.split(" ")[1], j.split(" ")[1], "一个顶俩"])
                                    py.append([uu, jw(pinyin(q.split(" ")[1])), jw(pinyin(
                                        i.split(" ")[1])), jw(pinyin(
                                            j.split(" ")[1])), ['yí', 'gè', 'dǐng', 'liǎ']])
                                    break
                        if len(ts) >= 6:
                            break
            res = {
                'title': "已为你显示相关的 "+str(len(ts))+" 条结果",
                "step": 5,
                "num": len(ts),
                'ls': ts,
                'tk': py
            }
            return res
        else:
            res = {
                'title': "没有，别试了",
                "step": 0,
            }
            return res


if __name__ == '__main__':
    print(yigedinglia("为所欲为"))
    exit()