

```
SyntaxError: Non-ASCII character '\xec' in file Finding the percentage.py on line 5, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
```



### SyntaxError: Non-ASCII Character 관련 에러

code내에 한글을 파이썬이 읽지 못해서 발생하는 에러



해결방법

```
# -*- coding: utf-8 -*- 
```

파일 첫번째 또는 두번째 줄에 입력

(공백이나 대소문자에 주의해야한다.)



> 알고보니 이 문제는 Python 버전이 2.7이라서 발생했다.
>
> 버전 3에서는 발생하지 않는다고 하니 버전을 업그레이드 해야겠다.