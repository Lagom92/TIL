# GROUP BY

<br/>

- 특정 컬럼을 그룹화 하는 GROUP BY
- 특정 컬럼을 그룹화한 결과에 조건을 거는 HAVING

```
SELECT 컬럼 FROM 테이블 GROUP BY 그룹화할-컬럼;
```

```
SELECT 컬럼 FROM 테이블 GROUP BY 그룹화할-컬럼 HAVING 조건식;
```



<br/>

- WHERE는 그룹화 하기 전이고, HAVING는 그룹화 후에 조건을 건다.



<br/>

- 고양이와 개가 각각 몇 마리인지 조회

```
SELECT ANIMAL_TYPE, COUNT(*) AS count FROM ANIMAL_INS GROUP BY ANIMAL_TYPE;
```





-  동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회 

```
SELECT NAME, COUNT(NAME) AS COUNT FROM ANIMAL_INS GROUP BY NAME HAVING COUNT > 1 ORDER BY NAME;
```





### GROUP BY HOUR(DATETIME)



-  9시부터 19시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회 
- DATETIME을 시간별로 가공해야함

```
SELECT HOUR(DATETIME) AS HOUR, COUNT(*) AS COUNT 
FROM ANIMAL_OUTS 
WHERE HOUR(DATETIME) >= 9 AND HOUR(DATETIME) <= 19 
GROUP BY HOUR(DATETIME);
```



-  0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회 

