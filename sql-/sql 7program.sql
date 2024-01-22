delimiter \\
drop table if exists singledelete2;\\
delimiter \\
drop table if exists singledelete4;\\
create procedure singledelete4 (
in tablename  varchar(50), 
in columnname  varchar(50) 
)
begin
set @statement= concat('alter table  ' ,tablename,' add column ',columnname,' varchar\(50\)');
prepare stm from  @statement;
execute stm;
end\\
delimiter ;
call singledelete4('srii_user_lists','address');
select *from srii_user_lists;
