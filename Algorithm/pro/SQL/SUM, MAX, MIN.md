# SUM, MAX, MIN

<br/>

TABLE NAME = ANIMAL_INS



<br/>

### MAX



<br/>

-  가장 최근에 들어온 동물은 언제 들어왔는지 조회 

```
SELECT MAX(DATETIME) FROM ANIMAL_INS;
```



<br/>

### MIN



<br/>

-  동물 보호소에 가장 먼저 들어온 동물은 언제 들어왔는지 조회 

```
SELECT MIN(DATETIME) FROM ANIMAL_INS;
```



<br/>

### COUNT



<br/>

-  동물 보호소에 동물이 몇 마리 들어왔는지 조회 

```
SELECT COUNT(ANIMAL_ID) FROM ANIMAL_INS
```



<br/>

### WHERE [Column] IS NOT NULL

NULL 제외



<br/>

### DISTINCT

중복을 제거





<br/>

-  동물 보호소에 들어온 동물의 이름은 몇 개인지 조회 (NAME이 NULL이면 제외, 중복은 하나로 처리)

```
SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS WHERE NAME IS NOT NULL;
```





<br/>



