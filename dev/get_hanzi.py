import regex

all_hanzi = set(regex.findall(r'\p{IsHan}', '''
刻
差
到
起床
约会
分钟
休息
晚饭
报纸
玩
睡觉
'''))

print('\n'.join(sorted(all_hanzi)))
