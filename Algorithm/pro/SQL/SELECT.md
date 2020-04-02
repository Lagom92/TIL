# SELECT

<br/>

### SELECT

<br/>



테이블 이름 = ANIMAL_INS



- 테이블의 데이터 전부 조회

```
SELECT * FROM ANIMAL_INS;
```



<br/>

### ORDER BY



- NAME과 DATETIME 조회(ID를 역순으로)

```
SELECT NAME, DATETIME FROM ANIMAL_INS ORDER BY ANIMAL_ID DESC;
```



<br/>

### WHERE



- ID와 NAME 조회(조건 INTAKE_CONDITION이 Sick인 것)

```
FROM ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION="Sick";
```





<br/>

- ID와 NAME 조회(조건 INTAKE_CONDITION이 Aged가 아닌 것)

```
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION !="Aged";
```



<br/>

- ID와 NAME을 조회(ANIMAL_ID 순으로)

```
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS ORDER BY ANIMAL_ID;
```





<br/>

- ID, NAME와 DATETIME을 조회(이름 순서로,  이름이 같으면 날짜가 늦은 순서대로)

```
SELECT ANINAL_ID, NAME, DATETIME FROM ANIMAL_INS ORDER BY NAME, DATETIME DESC; 
```





<br/>

### LIMIT



<br/>

- DATETIME가 가장 빠른 NAME 조회

```
SELECT NAME FROM ANIMAL_INS ORDER BY ASC LIMIT 1;
```





















