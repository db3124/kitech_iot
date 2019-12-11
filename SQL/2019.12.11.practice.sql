/*
    2019. 12. 11 DDL º¹½À
*/

CREATE TABLE EMP01(
             EMPNO NUMBER(4),
             ENAME VARCHAR2(20),
             SAL NUMBER(5,2),
             deptno NUMBER(3));
             
CREATE TABLE EMP02
AS
SELECT * FROM EMP;

CREATE TABLE EMP03
AS
SELECT * FROM EMP02;

CREATE TABLE EMP04
AS
SELECT EMPNO, ENAME, SAL FROM EMP; 

CREATE TABLE EMP06
AS
SELECT EMPNO, ENAME, SAL FROM EMP where empno=20;

select * from emp06;
select * from emp05;

create table emp07
as
select * from emp where 1=0;

select * from emp07;

alter table emp01
add (job varchar2(10))
;

alter table emp01
modify (job varchar2(20))
;

alter table emp01
drop column job
;

drop table EMP02
;

truncate table emp04;

select * from emp;

rename emp01 to test;

DESC DEPT;

CREATE TABLE EMP02(
             EMPNO NUMBER(4) NOT NULL,
             ENAME VARCHAR2(20) NOT NULL,
             JOB VARCHAR2(10),
             DEPTNO NUMBER(3)
             );

CREATE TABLE EMP02(
             EMPNO NUMBER(4),
             ENAME VARCHAR2(20),
             JOB VARCHAR2(10),
             DEPTNO NUMBER(3),
             PRIMARY KEY(EMPNO),
             UNIQUE(JOB),
             FOREIGN KEY(DEPTNO) REFERENCES DEPT(DEPTNO)
             );             
             


CREATE TABLE EMP03(
             EMPNO NUMBER(4) UNIQUE,
             ENAME VARCHAR2(20) NOT NULL,
             JOB VARCHAR2(10),
             DEPTNO NUMBER(3)
             );

CREATE TABLE EMP04(
             EMPNO NUMBER(4) CONSTRAINT EMP04_EMPNO_UK UNIQUE,
             ENAME VARCHAR2(20) CONSTRAINT EMP04_ENAME_NN NOT NULL,
             JOB VARCHAR2(10),
             DEPTNO NUMBER(3)
             );
             
CREATE TABLE EMP05(
             EMPNO NUMBER(4) CONSTRAINT EMP05_EMPNO_PK PRIMARY KEY,
             ENAME VARCHAR2(20) CONSTRAINT EMP05_ENAME_NN NOT NULL,
             JOB VARCHAR2(10),
             DEPTNO NUMBER(3)
             );

CREATE TABLE EMP07(
             EMPNO NUMBER(4) CONSTRAINT EMP07_EMPNO_PK PRIMARY KEY,
             ENAME VARCHAR2(20) CONSTRAINT EMP07_ENAME_NN NOT NULL,
             JOB VARCHAR2(10),
             DEPTNO NUMBER(2),
             SAL NUMBER(5,2) CONSTRAINT EMP07_SAL_CK CHECK(SAL BETWEEN 500 AND 5000),
             FOREIGN KEY(DEPTNO) REFERENCES DEPT(DEPTNO)
             );

DESC DEPT;
DROP TABLE EMP07;
             
CREATE TABLE DEPT01(
             DEPTNO NUMBER(2) CONSTRAINT DEPT01_DEPTNO_PK PRIMARY KEY,
             DNAME VARCHAR2(20),
             LOC VARCHAR2(20) DEFAULT 'SEOUL'
             );
 
 
 
 
 
 
 
 
 
 
 
 