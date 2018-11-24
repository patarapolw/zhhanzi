from zhlib import zh
import regex

for hanzi in regex.findall(r'\p{IsHan}', '''
休
到
刻
差
床
息
报
晚
玩
睡
约
纸
觉
起
钟
饭
'''):
    db_hanzi = zh.Hanzi.get_or_none(hanzi=hanzi)
    print(''.join(db_hanzi.pinyin))
