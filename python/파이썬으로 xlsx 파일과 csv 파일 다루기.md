# 파이썬으로 xlsx 파일과 csv 파일 다루기



> 엑셀 파일의 내용들 중 필요한 내용들만 추출해서 csv파일을 만들어야 했다.
>
> 파이썬을 이용해서 노가다를 줄이고 반자동으로 파일 처리를 하고 싶어서 했다.
>
> 판다스나 다른 것을 사용해도 되지만 나는 아래의 방법을 이용하였다.



## Openpyxl



- 설치

```
pip install openpyxl
```



- 사용

```python
import openpyxl
import csv
```



- 파일 열기

```
wb = openpyxl.load_workbook(엑셀 파일 이름)
```



- 파일 닫기

```
wb.close()
```



- 엑셀 sheet 열기

```
# index 이용하기
sheet = wb['Sheet1']
```



- cell에 접근하기

```
# index 이용하기
A = sheet['A1']
A.value
```

```
# cell() 함수 이용하기
A = sheet.cell(row=1, column=1)
A.value
```



- 마지막 셀 찾기

```
# row
sheet.max_row

# column
sheet.max_column
```



- cell 범위 찾기

```
# 특정 엑셀 범위
range = sheet['A1':'C2']
range2 = sheet[2:4]

# 특정 row
r = sheet[3]

# 특정 column
c = sheet['A']
```







- AI Hub에서 한국어 대화에 관한 엑셀 파일을 이용해서 csv파일을 만들었다.

- http://www.aihub.or.kr/content/553



- 전체 코드

```
# 엑셀 파일 열기
wb = openpyxl.load_workbook('food.xlsx')

# sheet 열기
sheet = wb['Sheet1']

# 마지막 row 셀 찾기
max_row = sheet.max_row

# csv파일 만들기
f = open('food.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)

for r in range(2, max_row):
    # 질문과 답이 모두 있는것만 csv파일에 넣기
    if sheet.cell(row=r, column=13).value and sheet.cell(row=r+1, column=16).value:
        q = sheet.cell(row=r, column=13).value
        a = sheet.cell(row=r+1, column=16).value

        wr.writerow([q, a])
        
f.close()
wb.close()
```



- food.csv

```csv
지금 배달되나요?,아 네 배달됩니다
짬뽕류는 어떤 게 있나요? 잘 나가는 짬뽕 있나요?,특해물 짬뽕도 있고 전복 새우 짬뽕도 있고 해물 종류도 새우 홍합 전복 없는 게 없습니다
전복 들어가는 거는 특해물 짬뽕 시켜야 돼요?,전복 짬뽕 시키면 전복이 들어가죠
전복 들어가고 여러 가지 또 딴 것도 들어가죠?,네네
마차이 짬뽕밥은 돼지고기 들어가나요?,짬뽕은 돼지고기 약간씩 들어갑니다
여기 칠성동 1가인데 배달되나요?,칠성동 1가는 안됩니다
중국집 명성루죠? 배달 지금 가능한가요?,예 배달 가능합니다
주로 어떤 게 잘 나가요?,탕수육에 짜장이나 짬뽕 세트가 잘 나가죠 
```













------------------------------------

참고



[빈 셀 생략하는 방법](https://stackoverflow.com/questions/7907928/openpyxl-check-for-empty-cell)

[python으로 엑셀 다루기](https://doitnow-man.tistory.com/159)











