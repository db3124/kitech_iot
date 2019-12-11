/*
    2019.11.20
*/

-- 사용자의 소유 테이블 정보
select * from tab;

-- 테이블 구조 확인
desc emp;

-- 테이블의 데이터 조회(검색, 질의)
select *
from emp;

select *
from dept;

-- 사원의 이름, 직급, 급여
select empno, ename, job, sal
from emp;

-- 사칙연산 : +, -, *, /
select ename, sal, sal*12 
from emp;

-- NULL : 아직 정해지지 않는 데이터. 연산 불가능->결과도 null
select ename, sal, sal*12, comm, sal*12+comm
from emp;

-- NULL값을 치환하는 함수 : nvl(컬럼명/데이터, 기본값)
select ename, sal, sal*12, nvl(comm,0) comm, sal*12+nvl(comm,0) total
from emp;

-- 문자열의 연산(+)->||
select ENAME||' is a '||JOB
from emp;

select 'Your commision is ', nvl(comm,0) as comm
from emp;

-- DISTINCT : 중복 데이터를 출력하지 않는다.
SELECT DEPTNO FROM EMP;
SELECT DISTINCT DEPTNO FROM EMP;
SELECT DISTINCT JOB FROM EMP;

-- 특정 행 선택 : WHERE절
SELECT ENAME, SAL, COMM
FROM EMP
WHERE SAL>=2000;

-- 조건식 : =
SELECT *
FROM EMP
WHERE DEPTNO = 10;

-- 문자열 비교 : 문자열은 작은 따옴표 안에. 대소문자 구별함
SELECT * FROM EMP WHERE ENAME='BLAKE';
SELECT * FROM EMP WHERE ENAME='blake';

-- 날짜 비교 : 작은 따옴표 안에. 대소문자 구별하지 않음
select * from emp where hiredate='81/09/08';
select * from emp where hiredate>'81/1/1';
select * from emp where hiredate between '81/1/1' and '83/1/1';

select ename, deptno, job from emp where deptno=10 and job='MANAGER';
select ename, deptno, job from emp where deptno=10 or job='MANAGER';

-- BETWEEN A AND B
select *
from emp
where sal between 2000 and 3000;

select * 
from emp 
where hiredate between '81/1/1' and '81/12/31';

select *
from emp
where hiredate>='81/1/1' and hiredate<='81/12/31';

-- IN(a,b,c) : a이거나 b이거나 c
SELECT ENAME FROM EMP WHERE COMM=300 OR COMM=500 OR COMM=1400;

SELECT EMPNO, ENAME FROM EMP WHERE COMM IN(300,500,1400);

-- 패턴 검색 : 컬럼 이름 LIKE 패턴식
select ename from emp where ename like '%T%';
select ename from emp where ename like 'T%';

-- 자리수 고정 패턴: _
select * from emp where ename like '_A%';
SELECT * FROM EMP WHERE ENAME LIKE '__A%';
SELECT * FROM EMP WHERE ENAME NOT LIKE '%E_';

-- NULL 연산자 : IS NULL, IS NOT NULL
select ename, comm from emp where comm is null;
select ename, comm from emp where comm is not null;

-- 결과 데이터 행의 정렬 : ORDER BY 컬럼명 DESC/ASC
select ename, sal from emp order by sal;
select ename, sal from emp order by sal desc;

-- 날짜
select ename, hiredate from emp order by hiredate;
select ename, hiredate from emp order by hiredate desc;

-- 문자열
select ename from emp order by ename;
select ename from emp order by ename desc;

-- 중복의 정렬조건
select ename, sal from emp order by sal desc;
select ename, sal, hiredate from emp order by sal desc, hiredate desc;

-- 함수
-- 변환함수 : 날짜->문자열, to_char(날짜, '패턴')
select SYSDATE, to_char(sysdate, 'YYYY.MM.DD (DY) HH24:MI:SS') 변환날짜
from dual;

select ename, hiredate, to_char(hiredate, 'YYYY.MM.DD DAY') hiredata
from emp
order by hiredate;

-- 변환함수 : 숫자->문자열, to_char(숫자, '패턴')
select to_char(800, 'L0,000,000'), to_char(12345, 'L9,999,999'), to_char(12345.67, '00,000.00')
from dual;

select ename, sal, to_char(sal, 'L9,999,999'), to_char(sal*1000*12+nvl(comm, 0)*1000, 'L999,999,999')
from emp
order by sal desc;

-- 변환 함수 : to_date(문자열/숫자, '패턴')
select trunc(sysdate-to_date('2019/01/01', 'YYYY/MM/DD'))
from dual;

-- 변환 함수 : to_number(문자열, '패턴')
select to_number('20,000', '999,999')-to_number('10,000', '999,999')
from dual;

-- 8. 직급에 따라 급여를 인상하도록 하자.
-- 직급이 'ANALYST'인 사원은 5%,
-- 'SALESMAN'인 사원은 10%,
-- 'MANAGER'인 사원은 15%
-- 'CLERK'인 사원은 20% 인상한다.
select empno, ename, job, sal,
    decode(job, 'ANALYST', sal+sal*0.05,
                'SALESMAN', sal+sal*0.1,
                'MANAGER', sal+sal*0.15,
                'CLERK', sal+sal*0.2
    ) upsal
from emp
order by job;

-- 집합함수
select sum(sal) as "월급의 합",
       trunc(avg(sal)) as "월 평균 급여",
       count(*) as "총 사원의 수",
       max(sal) as "최고 급여",
       min(sal) as "최저 급여",
       sum(comm) as "총 상여금",
       avg(comm) as "총 상여금 평균",
       count(comm) as "상여금 책정 인원"
from emp
where deptno=10;

select * from emp order by deptno asc;

-- group by : 그룹핑->그룹별 집합 함수 표현
-- having : 그룹의 결과 제한ㄴ
select deptno, count(*), sum(sal), trunc(avg(sal))
from emp
group by deptno
having avg(sal)>2000
;



