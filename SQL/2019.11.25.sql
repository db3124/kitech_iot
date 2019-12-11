/*
    2019.11.25
*/

-- CROSS JOIN : 테이블을 단순히 붙여준다.
-- JOIN -> 테이블을 집합으로 보고 집합의 곱 연산의 결과이다. -> N*M(결과 행이다.)
select * 
from emp, dept
;

-- equi join
select * 
from emp, dept
where emp.deptno = dept.deptno
;

-- 이름이 'SCOTT'인 사원의 소속부서의 이름을 사원의 이름과 함께 출력하자
select ename, dname, d.deptno
from emp e, dept d
where e.deptno = d.deptno
and ename = 'SCOTT'
;

-- no-equi join : 특정 범위 내에 있는지 조사
select e.sal, s.losal, s.hisal, s.grade
from emp e, salgrade s
where e.sal between s.losal and s.hisal
order by e.sal
;

-- self join
select mgr
from emp
where ename = 'SMITH'
;

select ename
from emp
where empno = 7902
;

select e1.ename, e2.ename
from emp e1, emp e2
where e1.mgr = e2.empno
;

select e1.ename, e2.ename, d.dname
from emp e1, emp e2, dept d
where e1.mgr = e2.empno and e1.deptno = d.deptno
;

select e1.ename, e2.ename, d.dname
from emp e1, emp e2, dept d
where e1.mgr = e2.empno and e1.deptno = d.deptno
order by e2.ename
;

-- outer join
select n.ename, nvl(m.ename,'없음') manager
from emp n, emp m
where n.mgr = m.empno(+)
;

-- ANSI join
-- cross join
select * from emp, dept;
select * from emp cross join dept;

select * from emp e, dept d where e.deptno = d.deptno;
select * from emp inner join dept on emp.deptno = dept.deptno; 

-- using
select * from emp inner join dept using (deptno);

-- natural join
select emp.ename, dept.deptno from emp natural join dept;

select empno m from emp right outer join emp e on m.mgr = e.empno;

-- left|right|full outer join
select * from emp e, emp m where e.mgar = e.emptno(+);
select * from emp e inner join emp m on e.mgr=m.empno;
select * from emp e  left outer join emp m on e.mgr =e.empno;

-- 부속질의 : 쿼리 안에 쿼리 작성
-- SELECT (부속질의) FROM ( 부속질의) where 컬럼 조건식(부속질의)

-- emp 테이블에서 평균 급여보다 더 많이 버는 사원의 리스트
-- sal>평균급여 <-부속질의
select avg(sal) from emp;
select ename, sal from emp where sal>2073; 

select *
from emp
where sal>(
    -- select sal from emp where sal>3000  
    select avg(sal) from emp
)
;

-- 다중행 조건
-- 3000 이상 받는 사원이 소속된 부서(10번, 20번)와 동일한 부서에서 근무하는 사원출력
-- 3000 이상 받는 사원이 소속된 부서 : 부속질의
-- 동일한 부서에서 근무하는 사원
select distinct deptno from emp where sal>=3000;

select ename, deptno
from emp
where deptno in(select distinct deptno from emp where sal>=3000)
;

select ename, deptno
from emp
where deptno in (
    select deptno from emp where sal>=3000
)
;

-- 30번 소속 사원들 중에서 급여를 가장 많이 받는 사원보다 더 많은 급여를 받는 사람의 이름, 급여 출력
-- 30번 소속 사원들 중에서 급여를 가장 많이 받는 사원
select ename, sal from emp where deptno=30;

select ename, sal 
from emp
where sal > all (select sal from emp where deptno = 30)
;

select sal from emp where deptno=30;

select ename, sal from emp
where sal > (select max(sal) from emp where deptno=30)
order by sal
;

-- 부서번호가 30번인 사원들의 급여 중 가장 작은 값(950)보다 많은 급여를 받는 사원의 이름, 급여
-- 부서번호가 30번인 사원들의 급여 중 가장 작은 값(950)
select sal from emp
where deptno = 30
;

select ename, sal from emp
where sal > any (select sal from emp where deptno = 30)
;

select ename, sal from emp
where sal >( select min(sal) from emp where deptno = 30 )
;

desc emp;

-- rownum
select ename, rownum from emp
;

-- 스칼라 부속질의 : select뒤에 위치하는 부속질의
-- 마당사점의 고객별 판매액(결과는 구객이름과 고객별 판매애글출력
select o.custid, (select name from customer c where c.custid = o.custid) 성명,
       sum(o.saleprice), round(avg(o.saleprice),0), count(*)
from orders o
group by o.custid
;

-- 주문 정보를 출력해보자.(주문번호, 고객 이름, 주문 금액)
select orderid, (select name from customer where orders.orderid=customer.custid), saleprice
from orders;

--join
select c.name, sum(o.saleprice)
from (select custid, name from customer where custid<=2) c,
     orders o
where c.custid = o.orderid
group by c.name
;

select * from (select custid, name from customer where custid<=2)
order by name
;

-- rownum
select ename, rownum from emp order by ename;

select ename, rownum from(select * from emp order by ename);


-- DDL
-- CREATE TABLE : 테이블 생성
-- 사원번호 사원이름, 급여 3개의 칼럼으로 구성된 EMP01 테이블 생성
create table emp01(
    empno number(4), -- 사원 번호
    ename varchar2(20), -- 사원 이름
    sal number(7,2) -- 급여
);

drop table emp01;

desc emp01;

-- 기존 테이블의 스키마 복사(제약조건 제외)해서 테이블 생성
create table emp02
as
select * from emp
;

desc emp;
desc emp02;

create table emp04
as
select ename, deptno from emp
;

desc emp04;

create table emp05
as
select * from emp
where sal>=3500
;

desc emp05;

drop table emp05;

create table emp06
as
select * from emp where 1=0;

desc emp06;

-- 테이블의 수정 : 컬럼의 추가, 수정, 삭제
-- 컬럼 추가
desc emp01;

alter table emp01
add (job varchar2(9))
;

alter table emp01
modify(job varchar2(20))
;

alter table emp01
drop column job
;

create table emp07
as
select * from emp
;
select * from emp07;

-- 테이블 삭제
drop table emp07;

select * from emp02;

truncate table emp02;

-- 테이블 이름 변경
rename test to emp
;
desc test;

-- 제약조건
insert into dept values (10,'test','seoul');

desc dept;

-- not null 제약조건
drop table emp01;

create table emp01(
    empno number(4) not null,
    ename varchar2(20) not null,
    job varchar2(10),
    deptno number(2)
)
;

insert into emp01 values(1002, 'daughter', 'manager', 10);
insert into emp01 values(1001, 'aunt', 'manager', 10);
select * from emp01;

drop table emp03;
create table emp03(
    empno number(4) unique,
    ename varchar2(20) not null,
    job varchar2(10),
    deptno number(2)
);

insert into emp03 values (1001, 'daughter','manager', 10);
insert into emp03 values (1001, 'queen', 'manager', 10);
select * from emp03;

drop table emp04;
create table emp04(
    empno number(4) constraint emp04_empno_uk unique,
    ename varchar2(20) constraint emp04_ename_nn not null,
    job varchar2(10),
    deptno number(2)
);

insert into emp04 values (1001, 'daughter', 'manager', 10);
insert into emp04 values (1001, 'queen', 'manager', 10);
select * from emp04;

drop table emp05;
create table emp05(
    empno number(4) constraint emp05_empno_pk primary key,
    ename varchar2(20) constraint emp05_ename_nn not null,
    job varchar2(10),
    deptno number(2)
);

insert into emp05 values (1001, 'daughter', 'manager', 10);
insert into emp05 values (1001, 'queen', 'manager', 10);

drop table emp06;
create table emp06(
    empno number(4) constraint emp06_empno_pk primary key,
    ename varchar2(20) constraint emp06_ename_nn not null,
    job varchar2(10),
    deptno number(2) constraint emp06_deptno_fk references dept(deptno)
);

insert into emp06 values (1001, 'daughter', 'manager', null);
insert into emp06 values (1002, 'queen', 'manager', 40);
select * from emp06;









