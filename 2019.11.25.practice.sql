/*
    2019.11.25 Practice
*/

-- cross join
select *
from emp, dept;

-- equi join
select empno, ename, e.deptno, d.deptno
from emp e, dept d
where e.deptno = d.deptno
and ename = 'SCOTT'
;

-- non equi join
select ename, sal, grade
from emp, salgrade
where sal between losal and hisal
;

select * from salgrade;

-- self join
select e1.empno, e1.ename, e1.mgr, e2.empno, e2.ename
from emp e1, emp e2
where e1.mgr = e2.empno
;

-- outer join
select e1.empno, e1.ename, e1.mgr, e2.empno, e2.ename
from emp e1, emp e2
where e1.mgr = e2.empno(+)
order by e1.ename
;

-- ANSI cross join
select *
from emp cross join dept
;

select * from emp, dept;

-- ANSI inner join
select * from emp inner join dept
on emp.deptno = dept.deptno
where job = 'MANAGER'
;

-- using
select *
from emp inner join dept
using (deptno)
where hiredate like '81%'
;

-- natural join
select * from emp natural join dept;

-- left|right|full outer join
select * from emp e1, emp e2 where e1.mgr = e2.empno(+);
select * from emp e1 inner join emp e2 on e1.mgr = e2.empno;
select * from emp e1 left outer join emp e2 on e1.mgr = e2.empno;
select * from emp e1 right outer join emp e2 on e1.mgr = e2.empno;
select * from emp e1 full outer join emp e2 on e1.mgr = e2.empno;

-- 단일행 서브 쿼리
select * from emp where ename = 'SCOTT';
select dname from dept where deptno = 20;

select dname 
from dept
where deptno=(select deptno from emp where ename='SCOTT')
;

-- 평균 급여를 구하는 쿼리문을 서브 쿼리로 사용, 평균 근여보다 더 많은 급여를 받는 사원을 검색
select *
from emp
where sal>=(select avg(sal) from emp)
;

-- 다중행 서브 쿼리 in/any, some/all/exist
-- in : 메인 쿼리의 비교 조건이 서브 쿼리의 결과 중에서 하나라도 일치하면 참
-- 3000이상 받는 사원이 소속된 부서와 동일한 부서에서 근무하는 사원
select *
from emp
where deptno in (select distinct deptno from emp where sal>=3000)
;

-- all : 메인 쿼리의 비교 조건이 서브 쿼리의 검색 결과와 모든 값이 일치해야 참
-- 30번 소속 사원들 중에서 급여를 가장 많이 받는 사원보다 더 많은 급여를 받는 사람의 이름, 급여 
select ename, sal
from emp
where sal > all(select sal from emp where deptno=30)
;

-- any, some : 메인 쿼리의 비교 조건이 서브 쿼리의 검색 결과와 하나 이상이 일치하면 참
-- 30번 소속 사원들의 급여 중 가장 작은 값보다 많은 급여를 받는 사원의 이름, 급여
select ename, sal
from emp
where sal > any (select sal from emp where deptno = 30)
;

-- rownum
select rownum, ename, deptno
from emp
where rownum <= 2
;

-- 스칼라 부속질의 : select절에서의 부속질의
-- 마당서점의 고객별 판매액. 결과는 고객이름과 고객별 판매액 출력
select (select name from customer c where c.custid=o.custid) 고객이름, sum(saleprice) 판매액
from orders o
group by custid
order by sum(saleprice) desc
;

-- orders 테이블에 각 주문에 맞는 도서이름 입력
select o.bookid, (select bookname from book b where b.bookid = o.bookid) bookname
from orders o
group by o.bookid
;

--update orders
--set bookname = (select bookname from book where book.bookid = orders.bookid)
--;

-- 인라인 뷰 : from절에서의 부속질의
-- 고객번호가 2 이하인 고객의 판매액. 결과는 고객이름과 고객별 판매액 출력
select * from customer;
select * from book;
select * from orders;

select cs.name, sum(saleprice)
from (select custid, name from customer c where c.custid<=2) cs, orders o
where cs.custid = o.custid
group by cs.name
;

-- 중첩질의 : where절에서의 부속질의=술어질의
-- 데이터를 선택하는 조건 또는 술어와 같이 사용됨.
-- 평균 주문금액 이하의 주문에 대해서 주문번호와 금액을 보이시오.
select orderid, saleprice
from orders
where saleprice<(select avg(saleprice) from orders)
;

-- 각 고객의 평균 주문금액보다 큰 금액의 주문 내역에 대해서
-- 주문번호, 고객번호, 금액 출력
select o1.orderid, o1.custid, o1.saleprice
from orders o1
where saleprice>(select avg(saleprice) from orders o2 where o1.custid=o2.custid)
;

select saleprice from orders having saleprice>avg(saleprice);
select avg(saleprice)
from orders;






