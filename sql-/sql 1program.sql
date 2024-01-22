show databases;
create database sri_user_details;
use sri_user_details;
create table sri_user_details(sno int not null ,name varchar(40) ,email varchar(90),phone_no long,address varchar(255),gender varchar(20));
show tables;

select * from sri_user_details;

insert into sri_user_details values(1,'s1','s1@gmail.com',12344567888,'trichy');
insert into sri_user_details values(2,'t1','tt@gmail.com',88990123456,'melur');
insert into sri_user_details values(3,'t2','t2@gmail.com',77665534368,'srirangam');
alter table  sri_user_details add column gender varchar(20);


update  sri_user_details set name='ss' 
where name='s1';
select * from sri_user_details order by address;
update sri_user_details set gender='female' where name ='t1';
update sri_user_details set gender='female' where name ='ss';
update sri_user_details set gender='female' where name ='t2';
update sri_user_details set email=
case sno
when 1 then 'snega@gmail'
when 3 then 'thaiyal@gmail.com'
when 2 then 'tamil@gmail.com'
end,

 name=
case sno
when 1 then 'snega'
when 3 then 'thaiyal'
when 2 then 'tamil'
end,
address=
case sno

when 2 then 'melur'
when 3 then 'illupur'
end 
where sno in(1);
 
drop database ai_batch01_list;



