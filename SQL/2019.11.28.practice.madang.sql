/*
    2019.11.28_Practice_madang
*/

select * from book;
select * from orders;
select * from customer;

--1 마당서점의고객이요구하는다음질문에대해SQL 문을작성하시오.
--(1) 도서번호가1인도서의이름
select bookname
from book
where bookid = 1
;

--(2) 가격이20,000원이상인도서의이름
select bookname
from book
where price >=20000
;

--(3) 박지성의총구매액(박지성의고객번호는1번으로놓고작성)
select custid, (select name from customer c where c.custid=o.custid) name, sum(saleprice)
from orders o
group by custid
having custid = 1
;

--(4) 박지성이구매한도서의수(박지성의고객번호는1번으로놓고작성)
select custid, (select name from customer c where c.custid=o.custid) name, count(*) bookcount
from orders o
group by custid
having custid = 1
;

--2 마당서점의운영자와경영자가요구하는다음질문에대해SQL 문을작성하시오.
--(1) 마당서점도서의총개수
select count(*) 총도서개수
from book
;


--(2) 마당서점에도서를출고하는출판사의총개수
select count(distinct(publisher)) 출판사수
from book
;

--(3) 모든고객의이름, 주소
select * from customer;

--(4) 2014년7월4일~7월7일사이에주문받은도서의주문번호
select orderid
from orders
where orderdate between '2014/07/04' and '2014/07/07'
;

--(5) 2014년7월4일~7월7일사이에주문받은도서를제외한도서의주문번호
select orderid
from orders
where orderdate < '2014/07/04' or orderdate > '2014/07/07'
;

--(6) 성이‘김’씨인고객의이름과주소
select name, address
from customer
where name like '김%'
;

--(7) 성이‘김’씨이고이름이‘아’로끝나는고객의이름과주소
select name, address
from customer
where name like '김%아'
;

--1 마당서점의고객이요구하는다음질문에대해SQL 문을작성하시오.
--(5) 박지성이구매한도서의출판사수
select count((select publisher from book b where b.bookid=park.bookid)) 출판사수
from (select bookid from orders where custid = (select custid from customer where name='박지성')) park
;

--(6) 박지성이구매한도서의이름, 가격, 정가와판매가격의차이
select b.bookname, b.price, price-saleprice
from book b, orders o
where b.bookid=o.bookid
      and o.custid = (select custid from customer where name='박지성')
;

--select (select name from customer c where c.custid=o.custid) name, b.bookname, b.price, price-saleprice
--from orders o, book b 
--where b.bookid=o.bookid
--;

--(7) 박지성이구매하지않은도서의이름
select bookname
from book
where bookid not in(select bookid from orders where custid=1)
;

select bookname
from book
where bookid not in(select bookid from orders 
                    where custid = (select custid from customer where name ='박지성'))
;

--2 마당서점의운영자와경영자가요구하는다음질문에대해SQL 문을작성하시오.
--(8) 주문하지않은고객의이름(부속질의사용)
select name
from customer c
where custid not in (select custid from orders o where c.custid = o.custid)
;

--(9) 주문금액의총액과주문의평균금액
select sum(saleprice), avg(saleprice)
from orders
;

--(10) 고객의이름과고객별구매액
select c.name, sum.sumprice
from customer c,
     (select custid, sum(saleprice) sumprice from orders group by custid) sum
where c.custid=sum.custid
;

--(11) 고객의이름과고객이구매한도서목록
select (select name from customer c where c.custid=o.custid) custname,
       (select bookname from book b where b.bookid=o.bookid) bookname
from orders o
order by custname
;

--(12) 도서의가격(Book 테이블)과판매가격(Orders 테이블)의차이가가장많은주문
select orderid, price-saleprice
from (select orderid, price-saleprice
      from book b, orders o
      where b.bookid=o.bookid
      order by price-saleprice desc)
where rownum =1
;

--(13) 도서의판매액평균보다자신의구매액평균이더높은고객의이름
select distinct((select name from customer c where c.custid=o.custid))
from orders o
where saleprice > (select avg(saleprice) from orders)
;













