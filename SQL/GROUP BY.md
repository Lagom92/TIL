# GROUP BY



- 그룹화 시키는것



- 특정 컬럼을 그룹화 할때 - GROUP BY



- 특정 컬럼을 그룹화한 결과에 조건을 거는것 - HAVING



> WHERE
>
> 그룹화 하기전에 조건을 줄 때 사용
>
> 
>
> HAVING
>
> 그룹화 한 후에 조건을 줄 때 사용



### 컬럼 그룹화

```
SELECT 컬럼 FROM 테이블 GROUP BY 그룹화할 컬럼;
```



### 조건 처리 후에 컬럼을 그룹화

```
SELECT 컬럼 FROM 테이블 WHERE 조건식 GROUP BY 그룹화할 컬럼;
```



### 컬럼 그룹화 후에 조건 처리

```
SELECT 컬럼 FROM 테이블 GROUP BY 그룹화할 컬럼 HAVING 조건식;
```





### 예시

TABLE: ANIMALS



- ANIMALS 테이블에서 NAME과 NAME의 수를 출력하기

```
SELECT NAME, COUNT(NAME) AS COUNT FROM ANIMALS GROUP BY NAME;
```

GROUP BY를 이용해서 NAME끼리 묶어서 NAME의 수를 COUNT했다.



- ANIMALS 테이블에서 NAME과 NAME의 수를 출력하기 단, NAME의 수가 2이상인 것만 출력하기

```
SELECT NAME, COUNT(NAME) AS COUNT FROM ANIMALS GROUP BY NAME HAVING COUNT >= 2;
```









-----





참고

https://extbrain.tistory.com/56

