# String, Date

## 중성화 여부 파악하기

 https://programmers.co.kr/learn/courses/30/lessons/59409 

<br/>

테이블명: ANIMAL_INS

````mysql
NAME	TYPE	NULLABLE
ANIMAL_ID	VARCHAR(N)	FALSE
ANIMAL_TYPE	VARCHAR(N)	FALSE
DATETIME	DATETIME	FALSE
INTAKE_CONDITION	VARCHAR(N)	FALSE
NAME	VARCHAR(N)	TRUE
SEX_UPON_INTAKE	VARCHAR(N)	FALSE
````

<br/>



<br/>

### 문제

-  동물의 아이디와 이름, 중성화 여부를 아이디 순으로 조회 
- 동물이 중성화 되었는지 파악해야함(`SEX_UPON_INTAKE` 컬럼에 'Neutered' or 'Spayed'라는 단어가 들어가 있음)
- 중성화가 되어 있으면 'O', 아니면 'X'



<br/>

### ANSWER

- IF 사용

```mysql
SELECT ANIMAL_ID, NAME, IF (SEX_UPON_INTAKE LIKE "Neutered%" OR  SEX_UPON_INTAKE LIKE "Spayed%", "O", 'X') AS '중성화'
FROM ANIMAL_INS;
```



<br/>

- 다른 방법(CASE 사용)

```mysql
SELECT ANIMAL_ID, NAME, 
CASE
 WHEN SEX_UPON_INTAKE LIKE '%Neutered%' OR SEX_UPON_INTAKE LIKE '%Spayed%'
 THEN 'O'
 ELSE 'X' END as '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```





<br/>

### IF 문법

```mysql
IF(조건, '참', '거짓')
```



- ex)

```mysql
SELECT IF(required, '필수' '선택') AS '필수여부' FROM subject
```



<br/>

### CASE 문법

```mysql
CASE
WHEN 조건1 THEN '조건1 반환값'
WHEN 조건2 THEN '조건2 반환값'
ELSE '충족되는 조건 없을때 반환값'
END
	
```







<br/>

<br/>

## 오랜 기간 보호한 동물(2)

 https://programmers.co.kr/learn/courses/30/lessons/59411 

<br/>

테이블명: ANIMAL_INS

```mysql
NAME	TYPE	NULLABLE
ANIMAL_ID	VARCHAR(N)	FALSE
ANIMAL_TYPE	VARCHAR(N)	FALSE
DATETIME	DATETIME	FALSE
INTAKE_CONDITION	VARCHAR(N)	FALSE
NAME	VARCHAR(N)	TRUE
SEX_UPON_INTAKE	VARCHAR(N)	FALSE
```

<br/>

테이블명: ANIMAL_OUTS

```
NAME	TYPE	NULLABLE
ANIMAL_ID	VARCHAR(N)	FALSE
ANIMAL_TYPE	VARCHAR(N)	FALSE
DATETIME	DATETIME	FALSE
NAME	VARCHAR(N)	TRUE
SEX_UPON_OUTCOME	VARCHAR(N)	FALSE
```



<br/>

### 문제

-  입양을 간 동물 중, 보호 기간이 가장 길었던 동물 두 마리의 아이디와 이름을 조회 



<br/>

### ANSWER

```
SELECT OUTS.ANIMAL_ID, OUTS.NAME 
FROM ANIMAL_OUTS AS OUTS
JOIN ANIMAL_INS AS INS 
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
ORDER BY (INS.DATETIME - OUTS.DATETIME) ASC
LIMIT 2;
```





<br/>

### JOIN

- 테이블 두개를 연결(결합)하는 것











