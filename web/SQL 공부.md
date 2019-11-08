# SQL 공부







## REGEXP

- 글자 시작이 (a, e, i, o, u) 인 city를 출력(중복 x)

```
SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[aeiou]';
```



- 글자의 마지막이(a, e, i, o, u)인 city를 출력(중복 x)

```
SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '[aeiou]$';
```



- 글자의 시작과 끝이 (a, e, i, o, u)인 city를 출력(중복 x)

```
SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[aeiou]' AND CITY REGEXP '[aeiou]$';
```



- 글자의 시작이 (a, ,e, i, o, u)가 아닌 city를 출력(중복 x)

```
SELECT DISTINCT CITY FROM STATION WHERE CITY NOT REGEXP '^[aeiou]';
```



- 글자의 마지막이(a, e, i, o, u)가 아닌 city를 출력(중복 x)

```
SELECT DISTINCT CITY FROM STATION WHERE CITY NOT REGEXP '[aeiou]$';
```



- ** either do not start with vowels or do not end with vowels

```
SELECT DISTINCT CITY 
    FROM STATION 
    WHERE CITY REGEXP '^[^aeiou]' 
    OR CITY REGEXP '[^aeiou]$'; 
```



- CITY의 시작과 마지막이 (a, e, i, o, u)가 아닌 city를 출력(중복 x)

```
SELECT DISTINCT CITY FROM STATION WHERE CITY NOT REGEXP '^[aeiou]' AND CITY NOT REGEXP '[aeiou]$';
```





## SELECT

- NAME을 알파벳 순서(alphabetical order)로 정렬해서 출력

```
SELECT NAME FROM EMPLOYEE ORDER BY NAME;
```



- SALARY 가 2000보다 크고, MONTHS가 10보다 작은 EMPLOYEE의 NAME을 출력

```
SELECT NAME FROM EMPLOYEE WHERE SALARY>2000 AND MONTHS<10;
```





## Repeat

- Draw The Triangle 1

```
SET @number = 21;
SELECT REPEAT('* ', @number := @number - 1) FROM information_schema.tables LIMIT 20;
```



- Draw The Triangle 2

```
SET @NUM = 0;
SELECT REPEAT('* ', @NUM := @NUM + 1) FROM information_schema.tables LIMIT 20;
```









## Join

![](C:\Users\multicampus\Lagom\TIL\web PJT md\img\SQL_Joins.png)



- 

```
SELECT 결과로 출력될 테이블 설정
FROM 기준 테이블명
JOIN 조인할 테이블명 ON 조인할 조건
WHERE 검색 조건;
```



- CITY 테이블과 COUNTRY테이블이 있다. CONTINENT가 Asia인 도시들의 POPULATION의 합을 출력

```
SELECT SUM(CITY.POPULATION)
FROM COUNTRY
JOIN CITY
ON COUNTRY.CODE = CITY.COUNTRYCODE
WHERE COUNTRY.CONTINENT = "Asia";
```

혹은

```
SELECT SUM(CITY.POPULATION) 
FROM CITY, COUNTRY 
WHERE CITY.COUNTRYCODE = COUNTRY.CODE 
AND COUNTRY.CONTINENT ='Asia';
```

둘다 된다.



- African Cities

```
SELECT CITY.NAME 
FROM CITY, COUNTRY 
WHERE CITY.COUNTRYCODE = COUNTRY.CODE 
AND COUNTRY.CONTINENT = 'Africa';
```













----

...ING