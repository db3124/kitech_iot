/*
    2019.11.25 Practice2
*/

-- 32. EQUI 조인을 사용하여 SCOTT 사원의 부서번호와 부서 이름을 출력하시오.
select e.deptno, d.dname
from emp e, dept d
where e.deptno = d.deptno
and ename = 'SCOTT'
;

-- 33. INNER JOIN과 ON 연산자를 사용하여 사원 이름과 함께 그 사원이 소속된 부서이름과 지역명을 출력하시오.
select ename, dname, loc
from emp e inner join dept d
on e.deptno = d.deptno
;

-- 36. 조인과 WildCARD를 사용하여 이름에 ‘A’가 포함된 모든 사원의 이름과 부서명을 출력하시오.
select ename, dname
from emp inner join dept
using (deptno)
where ename like '%A%'
;

-- 37. JOIN을 이용하여 NEW YORK에 근무하는 모든 사원의 이름, 업무, 부서번호 및 부서명을 출력하시오.
select e.ename, e.job, d.deptno, d.dname
from emp e inner join dept d
on e.deptno = d.deptno
where d.loc = 'NEW YORK'
;

-- 38. SELF JOIN을 사용하여 사원의 이름 및 사원번호, 관리자 이름을 출력하시오.
select e1.ename, e1.empno, e2.ename 관리자
from emp e1, emp e2
where e1.mgr = e2.empno
;

-- 39. OUTER JOIN, SELF JOIN을 사용하여 관리자가 없는 사원을 포함하여 사원번호를 기준으로 내림차순 정렬하여 출력하시오.
select e1.empno, e1.ename, e2.ename 관리자
from emp e1 left outer join emp e2
on e1.mgr = e2.empno
order by e1.empno
;

-- 40. SELF JOIN을 사용하여 지정한 사원의 이름, 부서번호, 지정한 사원과 동일한 부서에서 근무하는 사원을 출력하시오. ( SCOTT )
select e1.ename, e1.deptno
from emp e1
where e1.deptno = (select deptno from emp e2 where ename = 'SCOTT')
;

-- 41. SELF JOIN을 사용하여 WARD 사원보다 늦게 입사한 사원의 이름과 입사일을 출력하시오.
select e1.ename, e1.hiredate
from emp e1
where e1.hiredate > (select hiredate from emp e2 where e2.ename = 'WARD') 
order by e1.hiredate
; 

-- 42. SELF JOIN을 사용하여 관리자보다 먼저 입사한 모든 사원의 이름 및 입사일을 관리자의 이름 및 입사일과 함께 출력하시오.
select me.ename, me.hiredate, manager.ename 관리자, manager.hiredate 관리자입사일
from emp me, emp manager
where me.mgr=manager.empno and me.hiredate < manager.hiredate
;

-- 43. 사원 번호가 7788인 사원과 담당 업무가 같은 사원을 표시(사원 이름과 담당업무)하시오.
select e1.ename, e1.job
from emp e1
where e1.job = (select job from emp e2 where empno = 7788)
;

-- 44. 사원번호가 7499인 사원보다 급여가 많은 사원을 표시하시오. 사원이름과 감당 업무
select e1.ename, e1.job
from emp e1
where sal > (select sal from emp e2 where empno = 7499)
;

select sal from emp  where empno = 7499;

-- 45. 최소급여를 받는 사원의 이름, 담당업무 및 급여를 표시하시오. (그룹함수 사용)

-- 46. 평균급여가 가장 적은 직급의 직급 이름과 직급의 평균을 구하시오.


-- 47. 각 부서의 최소 급여를 받는 사원의 이름, 급여, 부서번호를 표시하시오.



-- 48. 담당업무가 ANALYST 인 사원보다 급여가 적으면서 업무가 ANALYST가 아닌 사원들을 표시(사원번호, 이름, 담당 업무, 급여)하시오.



-- 49. 부하직원이 없는 사원의 이름을 표시하시오.



-- 50. 부하직원이 있는 사원의 이름을 표시하시오.



-- 51. BLAKE와 동일한 부서에 속한 사원의 이름과 입사일을 표시하는 질의를 작성하시오. ( 단 BLAKE는 제외 )



-- 52. 급여가 평균 급여보다 많은 사원들의 사원 번호와 이름을 표시하되 결과를 급여에 대해서 오름차순으로 정렬하시오.



-- 53. 이름에 K가 포함된 사원과 같은 부서에서 일하는 사원의 사원 번호와 이름을 표시하시오.



-- 54. 부서위치가 DALLAS인 사원의 이름과 부서번호 및 담당업무를 표시하시오.



-- 55. KING에게 보고하는 사원의 이름과 급여를 표시하시오.



-- 56. RESEARCH 부서의 사원에 대한 부서번호, 사원이름 및 담당 업무를 표시하시오.



-- 57. 평균 월급보다 많은 급여를 받고 이름에 M이 포함된 사원과 같은 부서에서 근무하는 사원의 사원 번호, 이름, 급여를 표시하시오.



-- 58. 평균급여가 가장 적은 업무를 찾으시오.



-- 59. 담당업무가 MANAGER인 사원이 소속된 부서와 동일한 부서의 사원을 표시하시오.
select *
from emp e1
where e1.ename in (select e2.ename from emp e2 where job='MANAGER')
;







