
'''
모스부호 판독기

미완
다른 테케를 통과 못함 왜??
'''


def func(mos):
    dic = {
        "*-**": "ㄱ", 	
        "**-*": "ㄴ",	
        "-***": "ㄷ",
        "***-": "ㄹ",
        "--": "ㅁ",
        "*--": "ㅅ",
        "-*-": "ㅇ",
        "*--*": "ㅈ",
        "-*-*": "ㅊ",
        "-**-": "ㅋ",
        "--**": "ㅌ",
        "---": "ㅍ",
        "*---": "ㅎ",
        "*": "ㅏ",
        "**":  "ㅑ",
        "-": "ㅓ",
        "***": "ㅕ",
        "*-": "ㅗ",
        "-*": "ㅛ",
        "****": "ㅜ",
        "*-*": "ㅠ",
        "-**": "ㅡ",
        "**-": "ㅣ",
        "--*-": "ㅐ",
        "-*--": "ㅔ",
        "*****-": "ㅖ",
        "****-": "ㅒ"
    }


    res = []
    for word in list(mos.split()):
        res.append(dic[word])
        res.append(" ")
            


    return ''.join(res).strip()
    
    

data = "-*- *** *-** **- **-* -** **-* -**- *- -*** - ***- --*- **-* -*** -**"
print(func(data))