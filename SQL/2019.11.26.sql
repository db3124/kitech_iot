/*
    2019.11.26
*/

-- CHECK 제약조건
drop table emp07;

create table emp07(
    empno number(4) CONSTRAINT emp07_empno_pk PRIMARY KEY,
    ename varchar2(20) CONSTRAINT ename_emp07_nn NOT NULL,
    sal number(7,2) CONSTRAINT sal_emp07_chk CHECK (sal BETWEEN 500 AND 5000),
    -- sal number(7,2) CONSTRAINT sal_emp07_chk CHECK (sal >= 500 and sal <= 5000),
    regdate DATE DEFAULT sysdate
);

create table emp07(
    empno number(4),
    ename varchar2(20) not null, -- not null은 컬럼 수준에서만 정의할 수 있다.
    sal number(7,2),
    regdate DATE DEFAULT sysdate,
    deptno number(2),
    CONSTRAINT emp07_empno_pk PRIMARY KEY (empno),
    CONSTRAINT emp07_sal_chk CHECK (sal between 500 and 5000),
    CONSTRAINT emp07_deptno_fk FOREIGN KEY (deptno) REFERENCES dept(deptno)  
);

desc emp07;

-- 입력
-- insert into 테이블 이름 (컬럼...) values (data...)
insert into emp07(empno, ename, sal) values (null, null, 300);
insert into emp07(empno, ename, sal) values (2000, null, 300);
insert into emp07(empno, ename, sal) values (2000, 'JANE', 300);
insert into emp07(empno, ename, sal) values (2000, 'JANE', 5100);
insert into emp07(empno, ename, sal) values (2000, 'JANE', 3100);
insert into emp07(empno, ename, sal) values (3000, 'JAKE', 3100);

select * from emp07;

-- 데이터 입력
-- insert into 테이블이 (행 단위 입력에서 입력하고자 하는 컬럼(들)을 기술) values (기술된 컬럼에 입력할 값 기술)
-- 입력할 컬럼의 개수, 타입과 입력할 데이터의 개수, 타입은 같아야 한다.
create table dept01
as
select * from dept where 1=0;

insert into dept01 (deptno, dname, loc)
            values (10, 'DEV', 'SEOUL');

desc dept01;

insert into dept01 values ('', 'HR', 'GYEONGGI');

select * from dept01;

-- 데이터의 변경
-- UPDATE 테이블 이름 SET 변경컬럼=새로운 데이터 WHERE 조건식(행 선택)
select * from emp01;
drop table emp01;
desc emp01;

create table emp01
as
select * from emp;

UPDATE emp01 SET sal = sal * 1.1 WHERE job = 'SALESMAN';
UPDATE emp01 SET hiredate = sysdate;
UPDATE emp01 SET hiredate = sysdate WHERE substr(hiredate, 1, 2) = '87';

-- 급여가 3000 이상인 사원만 급여를 10% 인상
UPDATE emp01
SET sal = sal*1.1
WHERE sal>=3000
;

-- 1987년에 입사한 사원의 입사일을 오늘 날짜로 변경
UPDATE emp01
SET hiredate = sysdate
WHERE substr(hiredate, 1,2) = '87'
--WHERE hiredate>='87/01/01' and hireadte>='87/12/31'
;

-- SCOTT 사원의 부서번호를 10으로 변경을, 직급을 MANAGER로 변경, 
-- 입사일을 오늘 날짜로 변경, 급여를 50, 커미션을 4000으로 변경
UPDATE emp01
SET deptno = 10, job = 'MANAGER', hiredate = sysdate, sal = 50, comm = 4000
WHERE ename = 'SCOTT'
;

-- 20번 부서의 지역명을 40번 부서의 지역명으로 변경
SELECT loc FROM dept01 WHERE deptno=40;
SELECT loc FROM dept01 WHERE deptno=20;

UPDATE dept01
SET loc = (SELECT loc FROM dept01 WHERE deptno = 40)
WHERE deptno = 20
;

drop table dept01;
create table dept01
as
select * from dept;

-- 20번 부서의 부서이름과 지역을 40번 부서의 이름과 지역명으로 변경
UPDATE dept01
--SET dname = (SELECT dname FROM dept01 WHERE deptno = 40), loc = (SELECT dname FROM dept01 WHERE deptno = 40)
SET (dname, loc) = (SELECT dname, loc FROM dept01 WHERE deptno = 40)
WHERE deptno = 20
;

select * from dept01;

-- 데이터의 삭제
-- DELETE FROM 테이블명 WHERE 행 선택 조건 : 행 단위 삭제
SELECT * from dept01;

DELETE from dept01 where deptno = 10;
delete from dept01;

rollback;

-- view : 기본 테이블을 기반으로 하는 가상 테이블(select의 결과를 테이블로 사용)
select empno, ename, deptno from emp where deptno = 30;

select * from emp_view30;

create or replace view emp_view30
as
select empno, ename, deptno from emp where deptno = 30
;-- view 만들 수 있는 권한 생성해야 함

drop view emp_view30;

-- 인라인 뷰
-- 입사일이 빠른 5명을 순서대로 출력
select rownum, ename, hiredate from emp order by hiredate;

create or replace view emp_view_hire
as
select ename, hiredate from emp order by hiredate
;

select rownum, ename, hiredate from emp_view_hire where rownum < 6;

select rownum, ename, hiredate
from (select * from emp order by hiredate)
where rownum<=5
;

-- sequence : 자동 숫자 생성기
-- currval : 현재 시퀀스의 값을 반환
-- nextval : 새로운 번호를 생성해서 반환

create sequence dept_deptno_seq
                start with 10
                increment by 10;

select dept_deptno_seq.nextval from dual;

drop sequence dept_deptno_seq;

create table dept03
as
select * from dept where 1=0
;

select * from dept03;

insert into dept03 values (dept_deptno_seq.nextval,'HR', 'SEOUL');
insert into dept03 values (dept_deptno_seq.nextval,'HR');

rollback;

-- 인덱스 : 물리적인 저장공간으로 따로 분리. 검색 속도 향상
create index idx_emp_ename
on emp(ename)
;










