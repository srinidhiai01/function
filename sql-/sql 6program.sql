delimiter \\
drop table if exists singledelete22;\\
delimiter \\
drop table if exists singledelete22;\\
create procedure singledelete22 (
in tablename  varchar(50), 
in idname varchar(50),
in idparam int
)
begin
set @statement= concat('delete ' ,'from ',tablename,' where ',idname,'=',idparam);
prepare stm from  @statement;
execute stm;
end\\
delimiter ;
call singledelete22('srii_user_lists','sno',1);
select *from srii_user_lists;
